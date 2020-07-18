from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_MainWindow1

class Ui_MainWindow(object):

    # function to call main window from login window
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        #self.window.show()
        self.window.showMaximized()
    
    
        

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1058, 741)
        MainWindow.setStyleSheet("*{\n"
        "background:rgb(0, 0, 0)\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_logo = QtWidgets.QLabel(self.centralwidget)
        self.user_logo.setGeometry(QtCore.QRect(860, 220, 180, 180))
        self.user_logo.setAutoFillBackground(False)
        self.user_logo.setStyleSheet("*{\n"
        "color:red\n"
        "}\n"
        "")
        self.user_logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.user_logo.setText("")
        self.user_logo.setPixmap(QtGui.QPixmap("../../Downloads/FAVPNG_avatar-user-software-developer_SGhqDNkZ.png"))
        self.user_logo.setScaledContents(True)
        self.user_logo.setOpenExternalLinks(False)
        self.user_logo.setObjectName("user_logo")
        self.password_enter = QtWidgets.QLineEdit(self.centralwidget)
        self.password_enter.setGeometry(QtCore.QRect(860, 500, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.password_enter.setFont(font)
        self.password_enter.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.password_enter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.password_enter.setStyleSheet("*{\n"
        "background:transparent;\n"
        "border:1px solid white;\n"
        "border-radious:20px;\n"
        "font-size:16px;\n"
        "color:white;\n"
        "text-align:center;\n"
        "}\n"
        "\n"
        "QLineEdit:hover{\n"
        "border: 1px solid #44A08D;\n"
        "color:white;\n"
        "}")
        self.password_enter.setText("")
        self.password_enter.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_enter.setClearButtonEnabled(False)
        self.password_enter.setObjectName("password_enter")
        self.text_label = QtWidgets.QLabel(self.centralwidget)
        self.text_label.setGeometry(QtCore.QRect(870, 440, 171, 41))
        self.text_label.setStyleSheet("QLabel{\n"
        "font-size:24px;\n"
        "\n"
        "font-weight:bold;\n"
        "color:white;\n"
        "}\n"
        "\n"
        "QLabel:hover{\n"
        "background:transparent;\n"
        "color:#03bb85;\n"
        "}")
        self.text_label.setObjectName("text_label")
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setEnabled(True)
        self.login_btn.setGeometry(QtCore.QRect(860, 600, 181, 51))
        self.login_btn.setStyleSheet("QPushButton{\n"
        "font-size:16px;\n"
        "color:white;\n"
        "font-weight:bold;\n"
        "background-color:#44A08D;\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: #03bb85;\n"
        "color: white;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "\n"
        "}")
        self.login_btn.setObjectName("login_btn")
        #=================== code that button is clicked ==========

        self.login_btn.clicked.connect(self.openWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1058, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.password_enter.setPlaceholderText(_translate("MainWindow", "       P a s s w o r d"))
        self.text_label.setText(_translate("MainWindow", "  Travel Easy"))
        self.login_btn.setText(_translate("MainWindow", "L O G I N "))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.showMaximized()
    sys.exit(app.exec_())
