from ui import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow(None)
    window.setWindowTitle('FTP')
    window.setWindowIcon(QIcon('res/ftp.png'))
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

