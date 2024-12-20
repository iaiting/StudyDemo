#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QDockWidget,
    QTextEdit
)


class Demo(QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        self.dock1 = QDockWidget('Dock Window 1', self)
        self.dock2 = QDockWidget('Dock Window 2', self)
        self.dock3 = QDockWidget('Dock Window 3', self)

        self.dock1.setAllowedAreas(Qt.RightDockWidgetArea | Qt.LeftDockWidgetArea)
        self.dock2.setAllowedAreas(Qt.RightDockWidgetArea | Qt.TopDockWidgetArea)
        self.dock3.setAllowedAreas(Qt.NoDockWidgetArea)

        self.dock1.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self.dock2.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetClosable)
        self.dock3.setFeatures(QDockWidget.DockWidgetClosable)

        self.text1 = QTextEdit()
        self.text2 = QTextEdit()
        self.text3 = QTextEdit()

        self.dock1.setWidget(self.text1)
        self.dock2.setWidget(self.text2)
        self.dock3.setWidget(self.text3)

        self.addDockWidget(Qt.RightDockWidgetArea, self.dock1)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock2)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock3)

        self.center_text = QTextEdit()
        self.setCentralWidget(self.center_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
