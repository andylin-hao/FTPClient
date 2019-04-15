# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from view import *
import os
import time


class Ui_MainWindow(QObject):
    command_signal = pyqtSignal(str, str)

    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.port_label = QtWidgets.QLabel(self.centralWidget)
        self.port_label.setObjectName("port_label")
        self.gridLayout.addWidget(self.port_label, 0, 2, 1, 1)
        self.host_label = QtWidgets.QLabel(self.centralWidget)
        self.host_label.setObjectName("host_label")
        self.gridLayout.addWidget(self.host_label, 0, 0, 1, 1)
        self.host_edit = QtWidgets.QLineEdit(self.centralWidget)
        self.host_edit.setObjectName("host_edit")
        self.gridLayout.addWidget(self.host_edit, 0, 1, 1, 1)
        self.connect_btn = QtWidgets.QPushButton(self.centralWidget)
        self.connect_btn.setObjectName("connect_btn")
        self.gridLayout.addWidget(self.connect_btn, 0, 11, 1, 1)
        self.user_label = QtWidgets.QLabel(self.centralWidget)
        self.user_label.setObjectName("user_label")
        self.gridLayout.addWidget(self.user_label, 0, 4, 1, 1)
        self.port_edit = QtWidgets.QLineEdit(self.centralWidget)
        self.port_edit.setObjectName("port_edit")
        self.gridLayout.addWidget(self.port_edit, 0, 3, 1, 1)
        self.password_label = QtWidgets.QLabel(self.centralWidget)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 0, 8, 1, 1)
        self.password_edit = QtWidgets.QLineEdit(self.centralWidget)
        self.password_edit.setObjectName("password_edit")
        self.gridLayout.addWidget(self.password_edit, 0, 9, 1, 1)
        self.user_edit = QtWidgets.QLineEdit(self.centralWidget)
        self.user_edit.setObjectName("user_edit")
        self.gridLayout.addWidget(self.user_edit, 0, 5, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.message_label = QtWidgets.QLabel(self.centralWidget)
        self.message_label.setObjectName("message_label")
        self.gridLayout_2.addWidget(self.message_label, 4, 0, 1, 1)
        self.file_widget = FileTableWidget(self.centralWidget)
        self.file_widget.setObjectName("file_widget")
        self.file_widget.setColumnCount(4)
        self.gridLayout_2.addWidget(self.file_widget, 1, 0, 1, 1)
        self.current_path_label = QtWidgets.QLabel(self.centralWidget)
        self.current_path_label.setText("")
        self.current_path_label.setObjectName("current_path_label")
        self.gridLayout_2.addWidget(self.current_path_label, 3, 0, 1, 1)
        self.load_widget = LoadTableWidget(self.centralWidget)
        self.load_widget.setObjectName("load_widget")
        self.load_widget.setColumnCount(6)
        self.gridLayout_2.addWidget(self.load_widget, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuOption = QtWidgets.QMenu(self.menuBar)
        self.menuOption.setObjectName("menuOption")
        self.menuType = QtWidgets.QMenu(self.menuBar)
        self.menuType.setObjectName("menuType")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_system = QtWidgets.QAction(MainWindow)
        self.action_system.setObjectName("action_system")
        self.action_type = QtWidgets.QAction(MainWindow)
        self.action_type.setObjectName("action_type")
        self.action_port = QtWidgets.QAction(MainWindow)
        self.action_port.setCheckable(True)
        self.action_port.setObjectName("action_port")
        self.action_pasv = QtWidgets.QAction(MainWindow)
        self.action_pasv.setCheckable(True)
        self.action_pasv.setObjectName("action_pasv")
        self.menuOption.addAction(self.action_system)
        self.menuOption.addAction(self.action_type)
        self.menuType.addAction(self.action_port)
        self.menuType.addAction(self.action_pasv)
        self.menuBar.addAction(self.menuOption.menuAction())
        self.menuBar.addAction(self.menuType.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.client = Client()
        self.host_edit.setText('166.111.80.237')
        self.port_edit.setText('8279')
        self.user_edit.setText('cn2018')
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.action_pasv.setChecked(True)
        self.file_widget.setEnabled(False)
        self.load_widget.setEnabled(False)
        self.action_type.setEnabled(False)
        self.action_system.setEnabled(False)
        self.action_port.setEnabled(False)
        self.action_pasv.setEnabled(False)

        self.setupFileWidget()
        self.setupLoadWidget()
        self.setupSignal()

        self.port_ip = ''
        self.port_port = ''

        self.ROOT = ''

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.port_label.setText(_translate("MainWindow", "Port:"))
        self.host_label.setText(_translate("MainWindow", "Host:"))
        self.connect_btn.setText(_translate("MainWindow", "Connect"))
        self.user_label.setText(_translate("MainWindow", "User:"))
        self.password_label.setText(_translate("MainWindow", "Password:"))
        self.message_label.setText(_translate("MainWindow", "No message"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.menuType.setTitle(_translate("MainWindow", "Mode"))
        self.action_system.setText(_translate("MainWindow", "System"))
        self.action_type.setText(_translate("MainWindow", "Type"))
        self.action_port.setText(_translate("MainWindow", "Port"))
        self.action_pasv.setText(_translate("MainWindow", "Pasv"))

    def setupSignal(self):
        self.command_signal.connect(self.client.dispatch)
        self.client.insert_file.connect(self.insertFileItem)
        self.client.recv_msg.connect(self.message_label.setText)
        self.client.pwd_signal.connect(self.refreshDirectory)
        self.client.transfer_complete.connect(self.transferComplete)

        self.connect_btn.clicked.connect(self.connectClicked)
        self.action_port.triggered.connect(self.actionPortTriggered)
        self.action_pasv.triggered.connect(self.actionPasvTriggered)
        self.action_system.triggered.connect(self.actionSystemTriggered)
        self.action_type.triggered.connect(self.actionTypeTriggered)

        self.file_widget.double_clicked.connect(self.fileWidgetItemDoubleClicked)
        self.file_widget.action_refresh.triggered.connect(self.refreshFileWidget)
        self.file_widget.action_new_folder.triggered.connect(self.actionNewFolderTriggered)
        self.file_widget.action_delete.triggered.connect(self.actionDeleteTriggered)
        self.file_widget.action_rename.triggered.connect(self.actionRenameTriggered)
        self.file_widget.action_cut.triggered.connect(self.actionCutTriggered)
        self.file_widget.action_paste.triggered.connect(self.actionPasteTriggered)
        self.file_widget.action_download.triggered.connect(self.actionDownloadTriggered)
        self.file_widget.action_upload.triggered.connect(self.actionUploadTriggered)

        self.load_widget.action_control.triggered.connect(self.actionControlTriggered)
        self.load_widget.action_cancel.triggered.connect(self.actionCancelTriggered)

    def setupFileWidget(self):
        font = self.file_widget.horizontalHeader().font()
        font.setBold(True)
        self.file_widget.horizontalHeader().setFont(font)

        self.file_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.file_widget.verticalHeader().setDefaultSectionSize(20)
        self.file_widget.setFrameShape(QFrame.NoFrame)
        self.file_widget.setShowGrid(False)
        self.file_widget.verticalHeader().setVisible(False)
        self.file_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.file_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.file_widget.setHorizontalHeaderLabels(('File Name', 'File Type', 'File Size', 'Create Time'))

    def setupLoadWidget(self):
        font = self.load_widget.horizontalHeader().font()
        font.setBold(True)
        self.load_widget.horizontalHeader().setFont(font)

        self.load_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.load_widget.verticalHeader().setDefaultSectionSize(20)
        self.load_widget.setFrameShape(QFrame.NoFrame)
        self.load_widget.setShowGrid(False)
        self.load_widget.verticalHeader().setVisible(False)
        self.load_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.load_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.load_widget.setHorizontalHeaderLabels(
            ('File Name', 'Server Path', 'Local Path', 'Size', 'Type', 'Progress'))

    def connectClicked(self):
        if self.connect_btn.text() == 'Connect':
            host = self.host_edit.text()
            port = self.port_edit.text()
            username = self.user_edit.text()
            password = self.password_edit.text()
            warning = QMessageBox()

            self.command_signal.emit('connect', host + ' ' + port)
            if self.client.returnValue is False:
                warning.warning(self.window, 'Connection Warning', 'Host or Port error, connection refused',
                                QMessageBox.Yes)
                return
            self.command_signal.emit('user', username)
            if self.client.returnValue is False:
                warning.warning(self.window, 'Connection Warning', 'Username error, connection refused',
                                QMessageBox.Yes)
                return
            self.command_signal.emit('password', password)
            if self.client.returnValue is False:
                warning.warning(self.window, 'Connection Warning', 'Password error, connection refused',
                                QMessageBox.Yes)
                return
            self.command_signal.emit('type', 'I')
            self.command_signal.emit('pwd', '')
            if self.client.returnValue is False:
                warning.warning(self.window, 'Address error', 'The current directory is inaccessible',
                                QMessageBox.Yes)
                return

            self.ROOT = self.current_path_label.text()
            self.refreshFileWidget()

            self.connect_btn.setText('Disconnect')
            self.host_edit.setEnabled(False)
            self.port_edit.setEnabled(False)
            self.user_edit.setEnabled(False)
            self.password_edit.setEnabled(False)
            self.file_widget.setEnabled(True)
            self.load_widget.setEnabled(True)
            self.action_type.setEnabled(True)
            self.action_system.setEnabled(True)
            self.action_port.setEnabled(True)
            self.action_pasv.setEnabled(True)
        elif self.connect_btn.text() == 'Disconnect':
            self.command_signal.emit('quit', '')

            self.connect_btn.setText('Connect')
            self.host_edit.setEnabled(True)
            self.port_edit.setEnabled(True)
            self.user_edit.setEnabled(True)
            self.password_edit.setEnabled(True)
            self.action_pasv.setChecked(True)
            self.action_port.setChecked(False)
            self.file_widget.setEnabled(False)
            self.load_widget.setEnabled(False)
            self.action_type.setEnabled(False)
            self.action_system.setEnabled(False)
            self.action_port.setEnabled(False)
            self.action_pasv.setEnabled(False)
        elif self.connect_btn.text() == 'Port':
            self.port_ip = self.host_edit.text()
            self.port_port = self.port_edit.text()
            self.host_edit.setEnabled(False)
            self.port_edit.setEnabled(False)
            self.connect_btn.setText('Disconnect')
            self.file_widget.setEnabled(True)

    def actionSystemTriggered(self):
        self.command_signal.emit('syst', '')
        QMessageBox().information(self.window, 'System', self.client.response, QMessageBox.Ok)

    def actionTypeTriggered(self):
        self.command_signal.emit('type', 'I')
        QMessageBox().information(self.window, 'Type', self.client.response, QMessageBox.Ok)

    def actionPortTriggered(self):
        self.action_port.setChecked(True)
        self.action_pasv.setChecked(False)
        self.host_edit.setEnabled(True)
        self.port_edit.setEnabled(True)
        self.connect_btn.setText('Port')
        self.file_widget.setEnabled(False)

    def actionPasvTriggered(self):
        self.action_port.setChecked(False)
        self.action_pasv.setChecked(True)
        self.host_edit.setEnabled(False)
        self.port_edit.setEnabled(False)
        self.connect_btn.setText('Disconnect')
        self.file_widget.setEnabled(True)

    def fileWidgetItemDoubleClicked(self, row):
        warning = QMessageBox()
        if row != -1:
            file_type = self.file_widget.itemFromIndex(self.file_widget.model().index(row, 1)).text()
            file_name = self.file_widget.itemFromIndex(self.file_widget.model().index(row, 0)).text()
            if file_type == 'Directory':
                self.command_signal.emit('cwd', file_name)
                if self.client.returnValue is False:
                    warning.warning(self.window, 'Address error', 'The current directory is inaccessible',
                                    QMessageBox.Yes)
                    return
                self.command_signal.emit('pwd', '')
                if self.client.returnValue is False:
                    warning.warning(self.window, 'Address error', 'The current directory is inaccessible',
                                    QMessageBox.Yes)
                self.refreshFileWidget()

    def actionNewFolderTriggered(self):
        warning = QMessageBox()
        name, ok = QInputDialog.getText(self.window, 'New Folder', 'Folder Name', QLineEdit.Normal, 'New Folder')
        if ok:
            self.command_signal.emit('mkd', name)
            if self.client.returnValue is False:
                warning.warning(self.window, 'Creation Warning', 'Unable to create file here',
                                QMessageBox.Yes)
                return
            self.refreshFileWidget()

    def actionDeleteTriggered(self):
        warning = QMessageBox()
        row = self.file_widget.selected_row
        if row != -1:
            file_name = self.file_widget.itemFromIndex(self.file_widget.model().index(row, 0)).text()
            self.command_signal.emit('rmd', file_name)
            if self.client.returnValue is False:
                warning.warning(self.window, 'Creation Warning', 'Unable to delete this file',
                                QMessageBox.Yes)
                return
            self.refreshFileWidget()

    def actionRenameTriggered(self):
        warning = QMessageBox()
        row = self.file_widget.selected_row
        if row != -1:
            file_name = self.file_widget.itemFromIndex(self.file_widget.model().index(row, 0)).text()
            new_name, ok = QInputDialog.getText(self.window, 'Rename', 'New Name', QLineEdit.Normal,
                                                file_name)
            if ok:
                self.command_signal.emit('rnfr', file_name)
                self.command_signal.emit('rnto', new_name)
                if self.client.returnValue is False:
                    warning.warning(self.window, 'Warning', 'Unable to rename this file',
                                    QMessageBox.Yes)
                    return
            self.refreshFileWidget()

    def actionCutTriggered(self):
        row = self.file_widget.selected_row
        if row != -1:
            file_name = self.file_widget.itemFromIndex(self.file_widget.model().index(row, 0)).text()
            self.cut_file = os.path.join(self.current_path_label.text(), file_name)
            self.file_widget.action_paste.setEnabled(True)

    def actionPasteTriggered(self):
        warning = QMessageBox()
        if self.cut_file is not None:
            file_name = self.cut_file.split('/')[-1]
            self.command_signal.emit('rnfr', self.cut_file)
            self.command_signal.emit('rnto', file_name)
            if self.client.returnValue is False:
                warning.warning(self.window, 'Warning', 'Unable to paste here',
                                QMessageBox.Yes)
                return
            self.refreshFileWidget()

    def actionDownloadTriggered(self):
        warning = QMessageBox()
        row = self.file_widget.selected_row
        if row != -1:
            name = self.file_widget.itemFromIndex(self.file_widget.model().index(row, 0)).text()
            path = QFileDialog().getExistingDirectory(self.window, 'Select a download directory', os.getcwd())
            if not path:
                return
            file_name = os.path.join(path, name)

            if self.action_pasv.isChecked():
                self.command_signal.emit('pasv', '')
                if self.client.returnValue is False:
                    warning.warning(self.window, 'Connection Warning', 'Data connection refused',
                                    QMessageBox.Yes)
            if self.action_port.isChecked():
                if self.port_ip == '' and self.port_port == '':
                    warning.warning(self.window, 'Connection Warning', 'Please specify IP and Port first',
                                    QMessageBox.Yes)
                    return
                self.command_signal.emit('port', self.port_ip + ' ' + self.port_port)
                if self.client.returnValue is False:
                    warning.warning(self.window, 'Connection Warning', 'Data connection refused',
                                    QMessageBox.Yes)
                    return

            self.client.local_path = file_name
            self.client.server_path = os.path.join(self.current_path_label.text(), name)
            file_size = self.file_widget.itemFromIndex(self.file_widget.model().index(row, 2)).text()
            if not self.insertLoadItem(name, self.current_path_label.text(), path, file_size, 'download'):
                return
            self.client.restPos = 0

            self.command_signal.emit('retr', self.client.server_path)
            if self.client.returnValue is False:
                warning.warning(self.window, 'Download Warning', 'Unable to download this file',
                                QMessageBox.Yes)
                self.load_widget.removeRow(self.load_widget.rowCount() - 1)
                return
            self.file_widget.setEnabled(False)
            self.file_widget.setEnabled(False)
            self.file_widget.action_upload.setEnabled(False)
            self.file_widget.action_download.setEnabled(False)

    def actionUploadTriggered(self):
        warning = QMessageBox()
        file_name, file_type = QFileDialog().getOpenFileName(self.window, 'Select a file to upload', os.getcwd())
        if not file_name:
            return

        if self.action_pasv.isChecked():
            self.command_signal.emit('pasv', '')
            if self.client.returnValue is False:
                warning.warning(self.window, 'Connection Warning', 'Data connection refused',
                                QMessageBox.Yes)
        if self.action_port.isChecked():
            if self.port_ip == '' and self.port_port == '':
                warning.warning(self.window, 'Connection Warning', 'Please specify IP and Port first',
                                QMessageBox.Yes)
                return
            self.command_signal.emit('port', self.port_ip + ' ' + self.port_port)
            if self.client.returnValue is False:
                warning.warning(self.window, 'Connection Warning', 'Data connection refused',
                                QMessageBox.Yes)
                return

        self.client.local_path = file_name
        self.client.server_path = os.path.join(self.current_path_label.text(), file_name.split('/')[-1])
        file_size = self.client.bytes(os.path.getsize(file_name))
        if not self.insertLoadItem(file_name.split('/')[-1], self.current_path_label.text(),
                            '/'.join(file_name.split('/')[:-1]), file_size,
                            'upload'):
            return
        self.client.restPos = 0

        self.command_signal.emit('stor', self.client.server_path)
        if self.client.returnValue is False:
            warning.warning(self.window, 'Upload Warning', 'Unable to upload this file',
                            QMessageBox.Yes)
            self.load_widget.removeRow(self.load_widget.rowCount() - 1)
            return
        self.file_widget.setEnabled(False)
        self.connect_btn.setEnabled(False)
        self.file_widget.action_upload.setEnabled(False)
        self.file_widget.action_download.setEnabled(False)

    def actionControlTriggered(self):
        if self.load_widget.action_control.text() == 'Pause':
            self.client.transferMode = -1
            self.file_widget.setEnabled(True)
            self.file_widget.action_download.setEnabled(True)
            self.file_widget.action_upload.setEnabled(True)
            self.connect_btn.setEnabled(True)
            self.load_widget.action_control.setText('Resume')
            self.client.progress_update.disconnect(
                self.load_widget.cellWidget(self.load_widget.transfer_row, 5).setValue)
            self.load_widget.transfer_row = -1
        elif self.load_widget.action_control.text() == 'Resume':
            self.command_signal.emit('rest', str(self.load_widget.cellWidget(self.load_widget.selected_row, 5).value()))

            row = self.load_widget.selected_row
            server_path = self.load_widget.itemFromIndex(self.load_widget.model().index(row, 1)).text()
            local_path = self.load_widget.itemFromIndex(self.load_widget.model().index(row, 2)).text()
            name = self.load_widget.itemFromIndex(self.load_widget.model().index(row, 0)).text()
            server_path = os.path.join(server_path, name)
            local_path = os.path.join(local_path, name)
            transfer_type = self.load_widget.itemFromIndex(self.load_widget.model().index(row, 4)).text()

            if self.action_pasv.isChecked():
                self.command_signal.emit('pasv', '')
                if self.client.returnValue is False:
                    QMessageBox().warning(self.window, 'Connection Warning', 'Data connection refused',
                                          QMessageBox.Yes)
            if self.action_port.isChecked():
                if self.port_ip == '' and self.port_port == '':
                    QMessageBox().warning(self.window, 'Connection Warning', 'Please specify IP and Port first',
                                          QMessageBox.Yes)
                    return
                self.command_signal.emit('port', self.port_ip + ' ' + self.port_port)
                if self.client.returnValue is False:
                    QMessageBox().warning(self.window, 'Connection Warning', 'Data connection refused',
                                          QMessageBox.Yes)
                    return

            self.client.server_path = server_path
            self.client.local_path = local_path
            if transfer_type == 'download':
                self.command_signal.emit('retr', self.client.server_path)
                if self.client.returnValue is False:
                    QMessageBox().warning(self.window, 'Download Warning', 'Unable to download this file',
                                          QMessageBox.Yes)
                    return
            elif transfer_type == 'upload':
                self.command_signal.emit('stor', self.client.server_path)
                if self.client.returnValue is False:
                    QMessageBox().warning(self.window, 'Upload Warning', 'Unable to upload this file',
                                          QMessageBox.Yes)
                    return
            self.file_widget.setEnabled(False)
            self.connect_btn.setEnabled(False)
            self.load_widget.action_control.setText('Pause')
            self.load_widget.transfer_row = row
            self.client.progress_update.connect(self.load_widget.cellWidget(row, 5).setValue)

    def actionCancelTriggered(self):
        row = self.load_widget.selected_row
        self.client.transferMode = -1
        self.file_widget.setEnabled(True)
        self.file_widget.action_download.setEnabled(True)
        self.file_widget.action_upload.setEnabled(True)
        self.connect_btn.setEnabled(True)
        try:
            self.client.progress_update.disconnect(self.load_widget.cellWidget(row, 5).setValue)
        except:
            pass
        self.load_widget.transfer_row = -1
        self.load_widget.removeRow(row)

    def refreshFileWidget(self):
        path = self.current_path_label.text()
        warning = QMessageBox()
        if self.action_pasv.isChecked():
            self.command_signal.emit('pasv', '')
            if self.client.returnValue is False:
                warning.warning(self.window, 'Connection Warning', 'Data connection refused',
                                QMessageBox.Yes)
                return
        if self.action_port.isChecked():
            if self.port_ip == '' and self.port_port == '':
                warning.warning(self.window, 'Connection Warning', 'Please specify IP and Port first',
                                QMessageBox.Yes)
                return
            self.command_signal.emit('port', self.port_ip + ' ' + self.port_port)
            if self.client.returnValue is False:
                warning.warning(self.window, 'Connection Warning', 'Data connection refused',
                                QMessageBox.Yes)
                return

        for i in range(self.file_widget.rowCount()):
            self.file_widget.removeRow(0)

        if self.current_path_label.text() != self.ROOT:
            self.insertFileItem('..', 'Directory', '', '')

        self.command_signal.emit('list', path)

    def refreshDirectory(self, path):
        self.current_path_label.setText(path)

    def insertFileItem(self, name, type, size, time):
        row = self.file_widget.rowCount()
        self.file_widget.insertRow(row)

        file_name = QTableWidgetItem(name)
        file_type = QTableWidgetItem(type)
        file_size = QTableWidgetItem(size)
        file_time = QTableWidgetItem(time)

        if type == 'Directory':
            icon = QIcon(QFileIconProvider().icon(QFileInfo('..')))
        else:
            icon = QIcon(QFileIconProvider().icon(QFileInfo(name)))
        file_name.setIcon(icon)

        self.file_widget.setItem(row, 0, file_name)
        self.file_widget.setItem(row, 1, file_type)
        self.file_widget.setItem(row, 2, file_size)
        self.file_widget.setItem(row, 3, file_time)

    def insertLoadItem(self, name, server_path, local_path, size, type):
        for row in range(self.load_widget.rowCount()):
            row_name = self.load_widget.itemFromIndex(self.load_widget.model().index(row, 0)).text()
            row_server = self.load_widget.itemFromIndex(self.load_widget.model().index(row, 1)).text()
            row_local = self.load_widget.itemFromIndex(self.load_widget.model().index(row, 2)).text()
            row_type = self.load_widget.itemFromIndex(self.load_widget.model().index(row, 4)).text()
            if name == row_name and type == row_type and ((server_path == row_server and type == 'upload') or (
                    local_path == row_local and type == 'download')):
                msg = QMessageBox(self.window)
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Warning')
                msg.setText('Task already exists, will you resume or restart?')
                resume = msg.addButton('Resume', QMessageBox.YesRole)
                restart = msg.addButton('Restart', QMessageBox.NoRole)
                msg.exec()
                if msg.clickedButton() == resume:
                    self.load_widget.action_control.setText('Resume')
                    self.load_widget.selected_row = row
                    self.load_widget.action_control.trigger()
                    return False
                if msg.clickedButton() == restart:
                    self.load_widget.cellWidget(row, 5).setValue(0)
                    self.load_widget.action_control.setText('Resume')
                    self.load_widget.selected_row = row
                    self.load_widget.action_control.trigger()
                    return False

        row = self.load_widget.rowCount()
        self.load_widget.insertRow(row)

        file_name = QTableWidgetItem(name)
        file_server_path = QTableWidgetItem(server_path)
        file_local_path = QTableWidgetItem(local_path)
        file_size = QTableWidgetItem(size)
        transfer_type = QTableWidgetItem(type)

        size = self.byte(size.split()[0], size.split()[1])
        progress_bar = QProgressBar()
        progress_bar.setMaximum(size)
        progress_bar.setValue(0)
        self.client.progress_update.connect(progress_bar.setValue)

        self.load_widget.setItem(row, 0, file_name)
        self.load_widget.setItem(row, 1, file_server_path)
        self.load_widget.setItem(row, 2, file_local_path)
        self.load_widget.setItem(row, 3, file_size)
        self.load_widget.setItem(row, 4, transfer_type)
        self.load_widget.setCellWidget(row, 5, progress_bar)
        self.load_widget.transfer_row = row
        return True

    def transferComplete(self, type):
        time.sleep(0.5)
        if type:
            self.refreshFileWidget()
        self.file_widget.setEnabled(True)
        self.connect_btn.setEnabled(True)
        self.file_widget.action_upload.setEnabled(True)
        self.file_widget.action_download.setEnabled(True)
        self.load_widget.removeRow(self.load_widget.transfer_row)
        self.load_widget.transfer_row = -1

    def byte(self, size, unit):
        if unit == 'B':
            bytes = float(size)
        elif unit == 'KB':
            bytes = float(size) * 1024
        elif unit == 'MB':
            bytes = float(size) * 1024 * 1024
        elif unit == 'GB':
            bytes = float(size) * 1024 * 1024 * 1024
        else:
            bytes = float(size) * 1024 * 1024 * 1024 * 1024
        return int(bytes)


class FileTableWidget(QTableWidget):
    double_clicked = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__(parent)
        self.setupRightClickedMenu()

    def setupRightClickedMenu(self):
        self.menu = QMenu()
        self.action_delete = QAction('Delete', self)
        self.action_new_folder = QAction('New Folder', self)
        self.action_download = QAction('Download', self)
        self.action_upload = QAction('Upload Here', self)
        self.action_rename = QAction('Rename', self)
        self.action_cut = QAction('Cut', self)
        self.action_paste = QAction('Paste', self)
        self.action_refresh = QAction('Refresh', self)

        icon = QIcon(QFileIconProvider().icon(QFileInfo('..')))
        self.action_new_folder.setIcon(icon)

        self.action_paste.setEnabled(False)

    def mouseDoubleClickEvent(self, QMouseEvent):
        pos = QMouseEvent.pos()
        item = self.itemAt(pos)
        if item is not None:
            row = item.row()
            self.double_clicked.emit(row)
        else:
            self.double_clicked.emit(-1)

    def contextMenuEvent(self, QContextMenuEvent):
        self.menu.clear()
        pos = QContextMenuEvent.pos()
        item = self.itemAt(pos)
        if item is not None:
            row = item.row()
            self.selected_row = row
            file_type = self.itemFromIndex(self.model().index(row, 1)).text()
            self.menu.addAction(self.action_new_folder)
            self.menu.addAction(self.action_delete)
            self.menu.addAction(self.action_rename)
            self.menu.addAction(self.action_cut)
            self.menu.addAction(self.action_paste)
            self.menu.addAction(self.action_refresh)
            self.menu.addAction(self.action_upload)
            if file_type == 'File':
                self.menu.addAction(self.action_download)
        else:
            self.selected_row = -1
            self.menu.addAction(self.action_new_folder)
            self.menu.addAction(self.action_paste)
            self.menu.addAction(self.action_refresh)
            self.menu.addAction(self.action_upload)

        self.menu.exec(QCursor().pos())
        QContextMenuEvent.accept()


class LoadTableWidget(QTableWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupRightClickedMenu()

    def setupRightClickedMenu(self):
        self.menu = QMenu()
        self.action_control = QAction('Pause', self)
        self.action_cancel = QAction('Cancel', self)
        self.transfer_row = -1

    def contextMenuEvent(self, QContextMenuEvent):
        self.menu.clear()
        pos = QContextMenuEvent.pos()
        item = self.itemAt(pos)
        if item is not None:
            row = item.row()
            self.selected_row = row
            self.menu.addAction(self.action_control)
            self.menu.addAction(self.action_cancel)
            if row != self.transfer_row:
                self.action_control.setText('Resume')
                self.action_control.setEnabled(False)
                self.action_cancel.setEnabled(False)
            if row == self.transfer_row:
                self.action_control.setText('Pause')
                self.action_control.setEnabled(True)
                self.action_cancel.setEnabled(True)
            if self.transfer_row == -1:
                self.action_control.setText('Resume')
                self.action_control.setEnabled(True)
                self.action_cancel.setEnabled(True)

        self.menu.exec(QCursor().pos())
        QContextMenuEvent.accept()
