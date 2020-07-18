from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMessageBox
from mains import Ui_MainWindow1
import os
class Ui_MainWindow(object):
   #code to display the error message
    def showmessage(self):
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Login Error")
        msg.setText("Incorrect Credentials  ")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()
    #code to check the login validation
    def check_login(self):
        login_pass="1234"
        check_pass=self.password_enter.text()
        if check_pass==login_pass:          
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow1()           
            self.ui.setupUi(self.window)
            Login_prog.hide(self)
            self.window.showMaximized()
        else:
            self.showmessage()
            self.password_enter.setText("")                
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1341, 649)
        MainWindow.setStyleSheet("*{\n"
        "background:rgb(0, 0, 0)\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_logo = QtWidgets.QLabel(self.centralwidget)
        self.user_logo.setGeometry(QtCore.QRect(270, 160, 121, 111))
        self.user_logo.setAutoFillBackground(False)
        self.user_logo.setStyleSheet("*{\n"
        "color:red\n"
        "}\n"
        "")
        self.user_logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.user_logo.setText("")
        self.user_logo.setPixmap(QtGui.QPixmap("data/icon.png"))
        self.user_logo.setScaledContents(True)
        self.user_logo.setOpenExternalLinks(False)
        self.user_logo.setObjectName("user_logo")
        self.password_enter = QtWidgets.QLineEdit(self.centralwidget)
        self.password_enter.setGeometry(QtCore.QRect(230, 370, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.password_enter.setFont(font)
        self.password_enter.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.password_enter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.password_enter.setStyleSheet("*{\n"
        "background:transparent;\n"
        "border:1px solid white;\n"
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
        self.text_label.setGeometry(QtCore.QRect(250, 300, 171, 41))
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
        self.login_btn.setGeometry(QtCore.QRect(230, 470, 181, 51))
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
        self.login_btn.clicked.connect(lambda : self.check_login())
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setEnabled(True)
        self.btn0.setGeometry(QtCore.QRect(990, 480, 51, 41))
        self.btn0.setStyleSheet("QPushButton{\n"
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
        self.btn0.setObjectName("btn0")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setEnabled(True)
        self.btn2.setGeometry(QtCore.QRect(1060, 420, 51, 41))
        self.btn2.setStyleSheet("QPushButton{\n"
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
        self.btn2.setObjectName("btn2")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setEnabled(True)
        self.btn6.setGeometry(QtCore.QRect(1130, 360, 51, 41))
        self.btn6.setStyleSheet("QPushButton{\n"
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
        self.btn6.setObjectName("btn6")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setEnabled(True)
        self.btn1.setGeometry(QtCore.QRect(990, 420, 51, 41))
        self.btn1.setStyleSheet("QPushButton{\n"
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
        self.btn1.setObjectName("btn1")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setEnabled(True)
        self.btn5.setGeometry(QtCore.QRect(1060, 360, 51, 41))
        self.btn5.setStyleSheet("QPushButton{\n"
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
        self.btn5.setObjectName("btn5")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setEnabled(True)
        self.btn3.setGeometry(QtCore.QRect(1130, 420, 51, 41))
        self.btn3.setStyleSheet("QPushButton{\n"
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
        self.btn3.setObjectName("btn3")
        self.btnenter = QtWidgets.QPushButton(self.centralwidget)
        self.btnenter.setEnabled(True)
        self.btnenter.setGeometry(QtCore.QRect(1110, 480, 71, 41))
        self.btnenter.setStyleSheet("QPushButton{\n"
        "font-size:16px;\n"
        "color:white;\n"
        "font-weight:bold;\n"
        "background-color:crimson;\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: red;\n"
        "color: white;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "\n"
        "}")
        self.btnenter.setObjectName("btnenter")
        self.btnenter.clicked.connect(lambda : self.check_login())
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setEnabled(True)
        self.btn8.setGeometry(QtCore.QRect(1060, 300, 51, 41))
        self.btn8.setStyleSheet("QPushButton{\n"
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
        self.btn8.setObjectName("btn8")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setEnabled(True)
        self.btn7.setGeometry(QtCore.QRect(990, 300, 51, 41))
        self.btn7.setStyleSheet("QPushButton{\n"
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
        self.btn7.setObjectName("btn7")
        self.btnx = QtWidgets.QPushButton(self.centralwidget)
        self.btnx.setEnabled(True)
        self.btnx.setGeometry(QtCore.QRect(1060, 480, 51, 41))
        self.btnx.setStyleSheet("QPushButton{\n"
        "font-size:16px;\n"
        "color:white;\n"
        "font-weight:bold;\n"
        "background-color:crimson;\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: red;\n"
        "color: white;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "\n"
        "}")
        self.btnx.setObjectName("btnx")
        #self.btnx.clicked.connect(lambda : self.delete())
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setEnabled(True)
        self.btn9.setGeometry(QtCore.QRect(1130, 300, 51, 41))
        self.btn9.setStyleSheet("QPushButton{\n"
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
        self.btn9.setObjectName("btn9")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setEnabled(True)
        self.btn4.setGeometry(QtCore.QRect(990, 360, 51, 41))
        self.btn4.setStyleSheet("QPushButton{\n"
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
        self.btn4.setObjectName("btn4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1341, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Travel Easy"))
        self.password_enter.setPlaceholderText(_translate("MainWindow",     "P a s s w o r d"))
        self.text_label.setText(_translate("MainWindow", "  Travel Easy"))
        self.login_btn.setText(_translate("MainWindow", "L O G I N "))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btnenter.setText(_translate("MainWindow", "Enter"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btnx.setText(_translate("MainWindow", "X"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn4.setText(_translate("MainWindow", "4"))
#thread class to call init.py which runs every 5 seconds
class Thread0(QtCore.QThread):
    def __init__(self, *args, **kwargs):
        QtCore.QThread.__init__(self, *args, **kwargs)
    def run(self):
        os.system('python3 init.py')
#main class which calls the  Ui_mainwindow class
class Login_prog(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):        
        super().__init__()
        self.setupUi(self)
        self.th0=Thread0(self)
        #self.th0.start()
        # self.password_enter.setAlignment(QtCore.Qt.AlignCenter)
        # self.delete1()
        #code for pressing each button
        for n in range(0, 10):
            getattr(self, 'btn%s' % n).pressed.connect(lambda v=n: self.input_number(str(v)))
        #calling  the fucntion to clear the password
        self.btnx.clicked.connect(lambda : self.delete())
    #code to close the thread0
    def closeEvent(self, event):
        self.th0.stop()
        self.th0.wait()
        super().closeEvent(event)      
    #code to clear the password entererd
    def delete(self):
        self.password_enter.backspace()
    #function for displaying text   
    def input_number(self, v):
        self.password_enter.setAlignment(QtCore.Qt.AlignCenter)
        self.password_enter.insert(v)
        self.password_enter.setFocus()            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    prog=Login_prog()
    prog.showMaximized()
    sys.exit(app.exec_())
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    
    
