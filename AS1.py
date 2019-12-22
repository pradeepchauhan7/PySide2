from PySide2.QtCore import QRect, Slot, qApp, QEvent
from PySide2.QtWidgets import (QMainWindow, QApplication, QGraphicsScene, QGraphicsView, QPushButton,
                               QWidget, QLineEdit, QHBoxLayout, QGroupBox, QSizeGrip, QSplitter, QPlainTextEdit)
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

        self.view = QGraphicsView()
        self.scene.setBackgroundBrush(Qt.blue)
        self.view.setScene(self.scene)
        self.setCentralWidget(self.view)
        self.button.clicked.connect(self.buttonClicked)
        self.view.viewport().installEventFilter(self)

        self.drawing = False
        self.lastPoint = QPoint()
        self.startPoint = QPoint()

    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton):
            self.startPoint = event.pos()
            self.drawing = True

    def mouseReleaseEvent(self, event):

        if (Qt.LeftButton and self.drawing ):
            self.lastPoint = event.pos()
            self.update()

    def paintEvent(self, event):
        if (self.drawing and self.button.click()):

            le = QPlainTextEdit()
            width = QtCore.QRect(self.startPoint, self.lastPoint).size().width()
            height = QtCore.QRect(self.startPoint, self.lastPoint).size().height()
            x = self.startPoint.x()
            y = self.startPoint.y()
            print(x)
            if (width > 1 and height > 1):
                le.setGeometry(x, y, width, height)
                self.scene.addWidget(le)

    def buttonClicked(self):
        self.button.hide()

    def eventFilter(self, obj, event):
        if obj is self.view.viewport():
            if event.type() == QEvent.MouseButtonPress:
                self.mousePressEvent(event)
            elif event.type() == QEvent.MouseButtonRelease:
                self.mouseReleaseEvent(event)
        return QWidget.eventFilter(self, obj, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
#    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
