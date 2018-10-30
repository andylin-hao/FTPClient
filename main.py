from socket import *
import re


class Client:
    def __init__(self):
        self.socket_command = socket(AF_INET, SOCK_STREAM)
        self.socket_data = socket(AF_INET, SOCK_STREAM)
        self.ip = "127.0.0.1"
        self.port = 21
        self.dataMode = 0
        self.msg = ''
        self.command = ''
        self.response = ''

        self.socket_command.connect((self.ip, self.port))

    def pasv_read(self, res):
        pattern = r'(\d{1,3},\d{1,3},\d{1,3},\d{1,3},\d{1,3},\d{1,3})'
        ip_port = re.search(pattern, res).group(1)
        ip_port = ip_port.split(',')
        ip = '.'.join(ip_port[:4])
        port = int(ip_port[4]) * 256 + int(ip_port[5])
        self.socket_data = socket(AF_INET, SOCK_STREAM)
        self.socket_data.connect((ip, port))
        self.dataMode = 1

    def port_write(self, msg, response):
        ip_port = msg.split()[1]
        ip_port = ip_port.split(',')
        ip = '.'.join(ip_port[:4])
        port = int(ip_port[4]) * 256 + int(ip_port[5])
        self.socket_data = socket(AF_INET, SOCK_STREAM)
        self.socket_data.bind((ip, port))
        self.socket_data.listen(1)
        self.dataMode = 2

    def list_write(self, msg, response):
        if not response.startswith('150'):
            return
        if self.dataMode == 0:
            return
        if self.dataMode == 1:
            while True:
                data = self.socket_data.recv(1024)
                if len(data) == 0:
                    break
                print(data.decode('utf-8'))
            self.socket_data.close()
            self.dataMode = 0
        if self.dataMode == 2:
            conn_data, address = self.socket_data.accept()
            while True:
                data = conn_data.recv(1024)
                if len(data) == 0:
                    break
                print(data.decode('utf-8'))
            self.socket_data.close()
            self.dataMode = 0
        res = self.socket_command.recv(1024)
        print(res.decode('utf-8'))

    def retr_write(self, msg, response):
        if not response.startswith('150'):
            return
        fileName = msg.split()[1].replace('\r\n', '')
        if self.dataMode == 0:
            return
        if self.dataMode == 1:
            with open(fileName, "w", encoding='utf-8') as file:
                while True:
                    data = self.socket_data.recv(1024)
                    if len(data) == 0:
                        break
                    file.write(data.decode('utf-8'))
                self.socket_data.close()
                self.dataMode = 0
        if self.dataMode == 2:
            conn_data, address = self.socket_data.accept()
            with open(fileName, "w", encoding='utf-8') as file:
                while True:
                    data = conn_data.recv(1024)
                    if len(data) == 0:
                        break
                    file.write(data.decode('utf-8'))
                self.socket_data.close()
                self.dataMode = 0
        res = self.socket_command.recv(1024)
        print(res.decode('utf-8'))

    def stor_write(self, msg, response):
        if not response.startswith('150'):
            return
        fileName = msg.split()[1].replace('\r\n', '')
        if self.dataMode == 0:
            return
        if self.dataMode == 1:
            with open(fileName, "r", encoding='utf-8') as file:
                while True:
                    data = file.read(1024)
                    if len(data) == 0:
                        break
                    self.socket_data.send(data.encode('utf-8'))
                self.socket_data.close()
                self.dataMode = 0
        if self.dataMode == 2:
            conn_data, address = self.socket_data.accept()
            with open(fileName, "r", encoding='utf-8') as file:
                while True:
                    data = file.read(1024)
                    if len(data):
                        break
                    conn_data.send(data.encode('utf-8'))
                self.socket_data.close()
                self.dataMode = 0
        res = self.socket_command.recv(1024)
        print(res.decode('utf-8'))

    def processWriteCommand(self, msg, command, response):
        command += "_write"
        if hasattr(Client, command):
            getattr(Client, command)(self, msg, response)
            return False
        return True

    def processReadMsg(self, res, command):
        command += "_read"
        if hasattr(Client, command):
            getattr(Client, command)(self, res)
            return False
        return True

    def start(self):
        while True:
            self.response = self.socket_command.recv(1024)
            print(self.response.decode('utf-8'))
            self.processWriteCommand(self.msg, self.command, self.response.decode('utf-8'))
            self.processReadMsg(self.response.decode('utf-8'), self.command)
            self.msg = input()
            self.msg += '\r\n'
            self.socket_command.send(self.msg.encode('utf-8'))
            self.command = self.msg.split()[0].lower()


if __name__ == '__main__':
    client = Client()
    client.start()
