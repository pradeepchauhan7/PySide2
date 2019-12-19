from PySide2.QtCore import QRect, Slot, qApp, QEvent
from PySide2.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView, QPushButton, QWidget
from PySide2.QtCore import Qt, QPoint
from PySide2.QtGui import QImage, QPainter, QPen
from PySide2 import QtCore
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Assignment")
        self.scene = QGraphicsScene()
        self.button = QPushButton("Draw Text Boxes")
#        self.image = QImage(self.size(), QImage.Format_RGB32)
#        self.image.fill(Qt.black)
        self.scene.addItem(self.image)
        self.scene.addWidget(self.button)

        self.view = QGraphicsView(self.scene)
        #        self.view.resize(800, 600)
        self.setCentralWidget(self.view)

        self.button.clicked.connect(self.buttonClicked)
        self.view.viewport().installEventFilter(self)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black
        self.lastPoint = QPoint()
        self.startPoint = QPoint()

        print('-----------------', self.startPoint, self.lastPoint)
    def mousePressEvent(self, event):
        #        super(MainWindow, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.startPoint = event.pos()

    def mouseReleaseEvent(self, event):
        if (Qt.LeftButton & self.drawing):
            self.lastPoint = event.pos()
            self.update()

    def paintEvent(self, event):
        print('===================', self.startPoint, self.lastPoint)
        painter = QPainter(self)
        painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawRect(QtCore.QRect(self.startPoint, self.lastPoint))
#            canvasPainter = QPainter(self)
#            canvasPainter.drawImage(self.rect())

    def buttonClicked(self):
        self.button.hide()

    def eventFilter(self, obj, event):
        if obj is self.view.viewport():
            if event.type() == QEvent.MouseButtonPress:
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
