import os , sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt 
class Ui_MainWindow1(object):                
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1360, 613)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setEnabled(True)
        self.start_btn.setGeometry(QtCore.QRect(1070, 10, 91, 41))
        self.start_btn.setStyleSheet("QPushButton{\n"
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
        "")
        self.start_btn.setObjectName("start_btn")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setEnabled(True)
        self.stop_btn.setGeometry(QtCore.QRect(1160, 10, 91, 41))
        self.stop_btn.setStyleSheet("QPushButton{\n"
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
        "")
        self.stop_btn.setObjectName("stop_btn")
        self.logout_btn = QtWidgets.QPushButton(self.centralwidget)
        self.logout_btn.setEnabled(True)
        self.logout_btn.setGeometry(QtCore.QRect(1250, 10, 101, 41))
        self.logout_btn.setStyleSheet("QPushButton{\n"
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
        "")
        self.logout_btn.setObjectName("logout_btn")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 211, 791))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dashboard = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dashboard.setStyleSheet("QLabel{\n"
        "background:#263238;\n"
        "color:white;\n"
        "font-size:24px;\n"
        "\n"
        "}\n"
        "QLabel:hover{\n"
        "color:#44A08D;\n"
        "}")
        self.dashboard.setText("")
        self.dashboard.setObjectName("dashboard")
        self.verticalLayout.addWidget(self.dashboard)
        self.camera1 = QtWidgets.QLabel(self.centralwidget)
        self.camera1.setGeometry(QtCore.QRect(240, 180, 500, 400))
        self.camera1.setStyleSheet("")
        self.camera1.setText("")
        self.camera1.setObjectName("camera1")
        self.camera2 = QtWidgets.QLabel(self.centralwidget)
        self.camera2.setGeometry(QtCore.QRect(840, 180, 500, 400))
        self.camera2.setStyleSheet("")
        self.camera2.setText("")
        self.camera2.setObjectName("camera2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 100, 101, 41))
        self.label_2.setStyleSheet("QLabel{\n"
        "color:#263238;\n"
        "\n"
        "font-size:14px;\n"
        "\n"
        "}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1050, 100, 121, 41))
        self.label_3.setStyleSheet("QLabel{\n"
        "color:#263238;\n"
        "\n"
        "font-size:14px;\n"
        "\n"
        "}")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 0, 1151, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(99)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("QLabel{\n"
        "background:#263238;\n"
        "color:white;\n"
        "font-size:24px;\n"
        "\n"
        "}\n"
        "QLabel:hover{\n"
        "color:#44A08D;\n"
        "}")
        self.label.setObjectName("label")
        self.verticalLayoutWidget.raise_()
        self.camera1.raise_()
        self.camera2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.start_btn.raise_()
        self.stop_btn.raise_()
        self.logout_btn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1360, 27))
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuExit = QtWidgets.QMenu(self.menuBar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menuBar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actioncamer_I = QtWidgets.QAction(MainWindow)
        self.actioncamer_I.setObjectName("actioncamer_I")
        self.actioncamera_ii = QtWidgets.QAction(MainWindow)
        self.actioncamera_ii.setObjectName("actioncamera_ii")
        self.actioncheck_our_sites = QtWidgets.QAction(MainWindow)
        self.actioncheck_our_sites.setObjectName("actioncheck_our_sites")
        self.actionUpdates = QtWidgets.QAction(MainWindow)
        self.actionUpdates.setObjectName("actionUpdates")
        self.menuMenu.addAction(self.actionClose)
        self.menuMenu.addAction(self.actionExit)
        self.menuMenu.addSeparator()
        self.menuSettings.addAction(self.actioncamer_I)
        self.menuSettings.addAction(self.actioncamera_ii)
        self.menuHelp.addAction(self.actioncheck_our_sites)
        self.menuHelp.addAction(self.actionUpdates)
        self.menuBar.addAction(self.menuMenu.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuBar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Travel Easy"))
        self.start_btn.setText(_translate("MainWindow", "S T A R T"))
        self.stop_btn.setText(_translate("MainWindow", "S T O P"))
        self.logout_btn.setText(_translate("MainWindow", "L O G O U T"))
        self.label_2.setText(_translate("MainWindow", "C A M E R A - I"))
        self.label_3.setText(_translate("MainWindow", "C A M E R A - II"))
        self.label.setText(_translate("MainWindow", "       Travel Easy  "))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actioncamer_I.setText(_translate("MainWindow", "camera I"))
        self.actioncamera_ii.setText(_translate("MainWindow", "camera II"))
        self.actioncheck_our_sites.setText(_translate("MainWindow", "our sites"))
        self.actionUpdates.setText(_translate("MainWindow", "updates"))
    
    # def logout_func(self):
    #     print("call")
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_MainWindow()           
    #     self.ui.setupUi(self.window)
    #     mprog.hide()
    #     #self.window.show()
    #     self.window.showMaximized()
class Thread1(QtCore.QThread):
    def __init__(self, *args, **kwargs):
        QtCore.QThread.__init__(self, *args, **kwargs)
        super().__init__() 
    def run(self):
        os.system('python3 cam1.py')
class Thread2(QtCore.QThread):
    def __init__(self, *args, **kwargs):
        QtCore.QThread.__init__(self, *args, **kwargs)
        super().__init__() 
    def run(self):
        os.system('python3 cam2.py')
class Main_prog(QtWidgets.QMainWindow, Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint) 
        self.th1=Thread1(self)
        self.th2=Thread2(self)
        self.th1.start()
        self.th2.start() 
    def closeEvent(self, event):        
        self.th1.stop()
        self.th1.wait()
        self.th2.stop()
        self.th2.wait()
        super().closeEvent(event)    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mprog=Main_prog()
    mprog.showMaximized()
    sys.exit(app.exec_())


