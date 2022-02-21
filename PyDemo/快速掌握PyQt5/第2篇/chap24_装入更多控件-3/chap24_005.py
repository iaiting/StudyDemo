#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 24.5 多文档界面QMdiArea
#
################################################################################
from cgitb import text
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QMdiArea, QAction, QMdiSubWindow,
    QTextEdit
)

################################################################################
class Demo(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.mdi_area = QMdiArea(self)
        self.setCentralWidget(self.mdi_area)

        self.toolbar = self.addToolBar('Tool Bar')

        self.new_action = QAction('New', self)
        self.close_action = QAction('Close', self)
        self.close_all_action = QAction('Close All', self)
        self.mode1_action = QAction('Cascade', self)
        self.mode2_action = QAction('Tile', self)

        self.new_action.triggered.connect(self.new_func)
        self.close_action.triggered.connect(self.mdi_area.closeActiveSubWindow)
        self.close_all_action.triggered.connect(self.mdi_area.closeAllSubWindows)
        self.mode1_action.triggered.connect(self.mdi_area.cascadeSubWindows)
        self.mode2_action.triggered.connect(self.mdi_area.tileSubWindows)

        self.toolbar.addAction(self.new_action)
        self.toolbar.addAction(self.close_action)
        self.toolbar.addAction(self.close_all_action)
        self.toolbar.addAction(self.mode1_action)
        self.toolbar.addAction(self.mode2_action)

    def new_func(self):
        print('new_func')
        text = QTextEdit()
        sub = QMdiSubWindow()
        sub.setWidget(text)
        self.mdi_area.addSubWindow(sub)
        sub.show()

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
