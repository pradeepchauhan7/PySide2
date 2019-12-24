from PySide2.QtCore import  QEvent
from PySide2.QtWidgets import (QMainWindow, QApplication, QGraphicsScene, QGraphicsView, QPushButton,
                               QWidget, QSizeGrip, QPlainTextEdit)
from PySide2.QtCore import Qt, QPoint
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
        self.view.setScene(self.scene)
        self.setCentralWidget(self.view)
        self.button.clicked.connect(self.buttonClicked)
        self.view.viewport().installEventFilter(self)

        self.drawing = False
        self.lastPoint = QPoint()
        self.startPoint = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.startPoint = self.view.mapToScene(event.pos())
            self.drawing = True

    def mouseReleaseEvent(self, event):
        if Qt.LeftButton and self.drawing:
            self.lastPoint = self.view.mapToScene(event.pos())
            self.update()

    def paintEvent(self, event):

        if self.drawing :

            self.view.le = QPlainTextEdit()
            width = QtCore.QRectF(self.startPoint, self.lastPoint).size().width()
            height = QtCore.QRectF(self.startPoint, self.lastPoint).size().height()
            x = self.startPoint.x()
            y = self.startPoint.y()
            if width > 1 and height > 1:
                self.view.le.setGeometry(x, y, width, height)
                self.qsizegrip = QSizeGrip(self.view.le)
                self.scene.addWidget(self.view.le)

    def buttonClicked(self):
        self.button.hide()

    def eventFilter(self, obj, event):
        if obj is self.view.viewport():
            if event.type() == QEvent.MouseButtonPress:
                pass
#                self.mousePressEvent(event)
            elif event.type() == QEvent.MouseButtonRelease:
                self.mouseReleaseEvent(event)
        return QWidget.eventFilter(self, obj, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
#    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
