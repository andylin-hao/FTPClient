from socket import *
from ui import *
from PyQt5.QtCore import *
import re
import threading
import sys
import time


class Client(QObject):
    progress_update = pyqtSignal(int)
    transfer_complete = pyqtSignal(int)
    recv_msg = pyqtSignal(str)
    pwd_signal = pyqtSignal(str)
    insert_file = pyqtSignal(str, str, str, str)

    def __init__(self):
        super().__init__()
        self.socket_command = socket(AF_INET, SOCK_STREAM)
        self.socket_command.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.socket_data = socket(AF_INET, SOCK_STREAM)
        self.socket_data.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.ip = ''
        self.port = 0
        self.dataMode = 0
        self.transferMode = 0
        self.transferType = 0
        self.restPos = 0
        self.response = ''
        self.returnValue = True
        self.local_path = ''
        self.server_path = ''

    def dispatch(self, command, content):
        if hasattr(Client, command):
            if self.transferMode == 1:
                self.returnValue = True
                return
            self.returnValue = getattr(Client, command)(self, content)
        else:
            self.returnValue = False

    def sendCommand(self, command, content):
        if content != '':
            content = ' ' + content
        data = command + content + '\r\n'
        self.socket_command.send(data.encode())

    def recvRes(self):
        res = self.socket_command.recv(1024, MSG_PEEK).decode()
        pos = res.find('\r\n')
        if pos == -1:
            pos = 1024
        else:
            pos += 2
        res = self.socket_command.recv(pos + 2)
        self.recv_msg.emit(res.decode()[:-2])
        return res.decode()

    def recvData(self,socket, decode=True):
        if decode:
            res = socket.recv(1024, MSG_PEEK).decode()
            pos = res.find('\r\n')
        else:
            res = socket.recv(1024, MSG_PEEK)
            pos = res.find('\r\n'.encode())
        if pos == -1:
            pos = 1024
        else:
            pos += 2
        res = socket.recv(pos)
        if decode:
            return res.decode()
        else:
            return res

    def connect(self, content):
        self.socket_command = socket(AF_INET, SOCK_STREAM)
        self.socket_command.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.socket_data = socket(AF_INET, SOCK_STREAM)
        self.socket_data.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        content = content.split()
        if len(content) != 2:
            return False
        self.ip = content[0]
        self.port = content[1]
        try:
            self.port = int(self.port)
        except ValueError:
            return False
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', self.ip) is None:
            return False
        try:
            self.socket_command.connect((self.ip, self.port))
        except Exception:
            return False
        self.recvRes()
        return True

    def user(self, content):
        self.sendCommand('user', content)
        res = self.recvRes()
        if not res.startswith('331'):
            return False
        return True

    def password(self, content):
        self.sendCommand('pass', content)
        res = self.recvRes()
        if not res.startswith('230'):
            return False
        return True

    def pasv(self, content):
        self.sendCommand('pasv', content)
        res = self.recvRes()
        if not res.startswith('227'):
            return False
        pattern = r'(\d{1,3},\d{1,3},\d{1,3},\d{1,3},\d{1,3},\d{1,3})'
        ip_port = re.search(pattern, res)
        if ip_port:
            ip_port = ip_port.group(1)
            ip_port = ip_port.split(',')
            if len(ip_port) == 6:
                self.ip = '.'.join(ip_port[:4])
                self.port = int(ip_port[4]) * 256 + int(ip_port[5])
                self.socket_data = socket(AF_INET, SOCK_STREAM)
                self.socket_data.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
                try:
                    self.socket_data.connect((self.ip, self.port))
                except:
                    return False
                self.dataMode = 1
        return True

    def port(self, content):
        ip_port = content.split()
        if len(ip_port) == 2:
            ip = ip_port[0]
            try:
                port = int(ip_port[1])
            except ValueError:
                return False
            self.socket_data = socket(AF_INET, SOCK_STREAM)
            self.socket_data.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            try:
                self.socket_data.bind((ip, port))
                self.socket_data.listen(1)
            except Exception as e:
                print(e)
                return False
            content = ip.replace('.', ',')+','
            content += str(int(port/256))+','
            content += str(port%256)
            self.sendCommand('port', content)
            res = self.recvRes()
            if not res.startswith('200'):
                self.socket_data.shutdown(SHUT_RDWR)
                self.socket_data.close()
                return False
            self.dataMode = 2
            return True
        return False

    def pwd(self, content):
        self.sendCommand('pwd', content)
        res = self.recvRes()
        if not res.startswith('257'):
            return False
        else:
            self.pwd_signal.emit(res.split()[1][1:-1])
            return True

    def cwd(self, content):
        self.sendCommand('cwd', content)
        res = self.recvRes()
        if not res.startswith('250'):
            return False
        return True

    def mkd(self, content):
        self.sendCommand('mkd', content)
        res = self.recvRes()
        if not res.startswith('257'):
            return False
        return True

    def rmd(self, content):
        self.sendCommand('rmd', content)
        res = self.recvRes()
        if not res.startswith('250'):
            return False
        return True

    def rnfr(self, content):
        self.sendCommand('rnfr', content)
        res = self.recvRes()
        if not res.startswith('350'):
            return False
        return True

    def rnto(self, content):
        self.sendCommand('rnto', content)
        res = self.recvRes()
        if not res.startswith('250'):
            return False
        return True

    def syst(self, content):
        self.sendCommand('syst', content)
        self.response = ' '.join(self.recvRes().split()[1:])
        return True

    def type(self, content):
        self.sendCommand('type', content)
        self.response = ' '.join(self.recvRes().split()[1:])
        return True

    def list(self, content):
        self.sendCommand('list', content)
        res = self.recvRes()
        if not res.startswith('150'):
            return False
        else:
            thread = threading.Thread(target=self.readList)
            thread.start()
            return True

    def rest(self, content):
        self.sendCommand('rest', content)
        res = self.recvRes()
        if not res.startswith('350'):
            return False
        self.restPos = int(content)
        return True

    def retr(self, content):
        self.sendCommand('retr', content)
        res = self.recvRes()
        if not res.startswith('150'):
            return False
        else:
            self.transferType = 1
            thread = threading.Thread(target=self.readFile)
            thread.start()
            return True


    def stor(self, content):
        self.sendCommand('stor',content)
        res = self.recvRes()
        if not res.startswith('150'):
            return False
        else:
            self.transferType = 2
            thread = threading.Thread(target=self.sendFile)
            thread.start()
            return True

    def quit(self, content):
        self.sendCommand('quit', content)
        self.recvRes()
        self.socket_command.close()
        self.socket_data.close()

    def sendFile(self):
        if self.dataMode == 0:
            return
        if self.dataMode == 1:
            self.transferMode = 1
            try:
                with open(self.local_path, "rb") as file:
                    file.seek(self.restPos)
                    while True:
                        time.sleep(0.00000000000001)
                        if self.transferMode == -1:
                            break
                        data = file.read(1024)
                        self.socket_data.send(data)
                        if len(data) == 0:
                            break
                        self.restPos += len(data)
                        self.progress_update.emit(self.restPos)
            except IOError as e:
                print(e)
            try:
                self.socket_data.shutdown(SHUT_RDWR)
                self.socket_data.close()
            except:
                print(1)
            self.dataMode = 0
        if self.dataMode == 2:
            conn_data, address = self.socket_data.accept()
            self.transferMode = 1
            try:
                with open(self.local_path, "rb") as file:
                    file.seek(self.restPos)
                    while True:
                        time.sleep(0.00000000000001)
                        if self.transferMode == -1:
                            break
                        data = file.read(1024)
                        conn_data.send(data)
                        if len(data) == 0:
                            break
                        self.restPos += len(data)
                        self.progress_update.emit(self.restPos)
            except IOError as e:
                print(e)
            try:
                conn_data.shutdown(SHUT_RDWR)
                conn_data.close()
                self.socket_data.shutdown(SHUT_RDWR)
                self.socket_data.close()
            except:
                pass
            self.dataMode = 0

        self.recvRes()
        if self.transferMode != -1:
            self.restPos = 0
            self.transferMode = 0
            self.transfer_complete.emit(1)
        self.transferMode = 0


    def readFile(self):
        if self.restPos:
            mode = 'ab'
        else:
            mode = 'wb'
        if self.dataMode == 0:
            return False
        if self.dataMode == 1:
            self.transferMode = 1
            try:
                with open(self.local_path, mode) as file:
                    while True:
                        data = self.recvData(socket=self.socket_data,decode=False)
                        if len(data) == 0:
                            break
                        file.write(data)
                        self.restPos += len(data)
                        self.progress_update.emit(self.restPos)
                        if self.transferMode == -1:
                            break
            except IOError as e:
                print(e)
            try:
                self.socket_data.shutdown(SHUT_RDWR)
                self.socket_data.close()
            except:
                pass
            self.dataMode = 0
        if self.dataMode == 2:
            conn_data, address = self.socket_data.accept()
            self.transferMode = 1
            try:
                with open(self.local_path, mode) as file:
                    while True:
                        data = self.recvData(socket=conn_data, decode=False)
                        if len(data) == 0:
                            break
                        file.write(data)
                        self.restPos += len(data)
                        self.progress_update.emit(self.restPos)
                        if self.transferMode == -1:
                            break
            except IOError as e:
                print(e)
            try:
                conn_data.shutdown(SHUT_RDWR)
                conn_data.close()
                self.socket_data.shutdown(SHUT_RDWR)
                self.socket_data.close()
            except:
                pass
            self.dataMode = 0

        self.recvRes()
        if self.transferMode != -1:
            self.transferMode = 0
            self.restPos = 0
            self.transfer_complete.emit(1)
        self.transferMode = 0

    def readList(self):
        if self.dataMode == 0:
            return False
        if self.dataMode == 1:
            while True:
                data = self.recvData(socket=self.socket_data, decode=False)
                if len(data) == 0:
                    break
                self.parseList(data.decode())
            try:
                self.socket_data.shutdown(SHUT_RDWR)
                self.socket_data.close()
            except:
                print(2)
            self.dataMode = 0
        if self.dataMode == 2:
            conn_data, address = self.socket_data.accept()
            while True:
                data = self.recvData(socket=conn_data, decode=False)
                if len(data) == 0:
                    break
                self.parseList(data.decode())
            try:
                conn_data.shutdown(SHUT_RDWR)
                conn_data.close()
                self.socket_data.shutdown(SHUT_RDWR)
                self.socket_data.close()
            except:
                pass
            self.dataMode = 0
        self.recvRes()

    def parseList(self, data):
        data = data.split()
        if data[0][0] == 'd':
            type = 'Directory'
        else:
            type = 'File'
        name = ''.join(data[8:])
        time = ' '.join(data[5:8])
        size = int(data[4])
        size = self.bytes(size)

        self.insert_file.emit(name, type, size, time)

    def bytes(self, byte):
        if byte < 1024:
            byte = str(round(byte, 2)) + ' B'
        elif byte < 1024 * 1024:
            byte = str(round(byte / 1024, 2)) + ' KB'
        elif byte < 1024 * 1024 * 1024:
            byte = str(round(byte / 1024 / 1024, 2)) + ' MB'
        elif byte < 1024 * 1024 * 1024 * 1024:
            byte = str(round(byte / 1024 / 1024 / 1024, 2)) + ' GB'
        else:
            byte = str(round(byte / 1024 / 1024 / 1024 / 1024, 2)) + ' TB'
        return byte
