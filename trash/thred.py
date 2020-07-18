from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import PyCapture2
import numpy as np


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(600, 400)
        scene = QtWidgets.QGraphicsScene()
        graphicsView = QtWidgets.QGraphicsView(scene)
        self.setCentralWidget(graphicsView)
        self._item = QtWidgets.QGraphicsPixmapItem()
        scene.addItem(self._item)
        thread = CapThread(self)
        thread.imageChanged.connect(self.on_imageChanged)
        thread.start()     

    @QtCore.pyqtSlot(QtGui.QImage)
    def on_imageChanged(self, image):
        pixmap = QtGui.QPixmap.fromImage(image)
        self._item.setPixmap(pixmap)


class CapThread(QtCore.QThread):
    imageChanged = QtCore.pyqtSignal(QtGui.QImage)

    def run(self):
        bus = PyCapture2.BusManager()
        uid = bus.getCameraFromIndex(0)
        c = PyCapture2.Camera()
        c.connect(uid)        

        while True:
            c.startCapture()
            img = c.retrieveBuffer()
            c.stopCapture()

            cv_img1 = np.array(img.getData(), dtype="uint8").reshape((img.getRows(), img.getCols()))
            cv_img = cv2.cvtColor(cv_img1, cv2.COLOR_BAYER_BG2BGR)
            cv_img = cv2.resize(cv_img, (380,270))

            height, width, dim = cv_img.shape
            bytesPerLine = dim * width
            image = QtGui.QImage(cv_img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
            self.imageChanged.emit(image)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())