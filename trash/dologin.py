from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox

from login import Ui_MainWindow
from main import Ui_MainWindow1

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
              
        # Setup numbers.
        for n in range(0, 10):
            getattr(self, 'btn%s' % n).pressed.connect(lambda v=n: self.input_number(str(v)))

        self.login_btn.clicked.connect(lambda : self.check_login())

    # def display(self):
    #     self.password_enter.display(self.stack[-1])
    
    def input_number(self, v):
        self.password_enter.setText(v)
       
            
    def showmessage(self):
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Login Error")
        msg.setText("Incorrect Credentials  ")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()

    def check_login(self):
        login_pass="123"
        check_pass=self.password_enter.text()
        if check_pass==login_pass:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow1()
            self.ui.setupUi(self.window)
            MainWindow.hide()
            #self.window.show()
            self.window.showMaximized()
        else:
            #QMessageBox.about(self,"Login Error","Incorrect Credentials")
            #QMessageBox.question(self,'Login Error',"Incorrect Password",QMessageBox.Ok,QMessageBox.Cancel)
            self.showmessage()
            self.password_enter.setText("")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    prog=MainWindow()
    prog.show()
    prog.showMaximized()
    sys.exit(app.exec_())
