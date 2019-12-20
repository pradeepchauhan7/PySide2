from PySide2.QtCore import QRect, Slot, qApp, QEvent
from PySide2.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView, QPushButton, QWidget
from PySide2.QtCore import Qt, QPoint
from PySide2.QtGui import QImage, QPainter, QPen, QPixmap
from PySide2 import QtCore
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Assignment")
        self.scene = QGraphicsScene()
        self.resize(800, 600)
        self.button = QPushButton("Draw Text Boxes")
        self.scene.addWidget(self.button)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.black)



        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        self.button.clicked.connect(self.buttonClicked)
        self.view.viewport().installEventFilter(self)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.white
        self.lastPoint = QPoint()
        self.startPoint = QPoint()

    def mousePressEvent(self, event):
        #        super(MainWindow, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.startPoint = event.pos()
            self.drawing = True
    def mouseReleaseEvent(self, event):

        if (Qt.LeftButton & self.drawing):

            self.lastPoint = event.pos()
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawRect(QtCore.QRect(self.startPoint,self.lastPoint))
            print(QtCore.QRect(self.startPoint, self.lastPoint).size())
            self.update()


    def paintEvent(self, event):
        if (self.drawing):
            pixmap = QPixmap.fromImage(self.image)
            self.scene.addPixmap(pixmap)
        #    canvasPainter = QPainter(self)
        #    canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def buttonClicked(self):
        self.button.hide()

    def eventFilter(self, obj, event):
        if obj is self.view.viewport():
            if event.type() == QEvent.MouseButtonPress:
                self.mousePressEvent(event)
                print('mouse press event = ', event.pos())
            elif event.type() == QEvent.MouseButtonRelease:
                self.mouseReleaseEvent(event)
                print('mouse release event = ', event.pos())

        return QWidget.eventFilter(self, obj, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
