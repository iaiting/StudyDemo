#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 24.5 多文档界面QMdiArea
#
################################################################################
from re import S
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, 
    QMdiArea, QAction
)
from PyQt5.QtGui import QIcon

################################################################################
class Demo(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)
        self.toolbar = self.addToolBar('Tool Bar')

        self.new_action = QAction(QIcon('images/new.ico'), 'New', self)
        self.close_action = QAction(QIcon('images/close.ico'), 'Close', self)
        self.close_all_action = QAction(QIcon('images/close_all.ico'), 'Close All', self)
        self.mode1_action = QAction(QIcon('images/cascade.ico'), 'Cascade', self)
        self.mode2_action = QAction(QIcon('images/tile.ico'), 'Tile', self)

        self.toolbar.addAction(self.new_action)
        self.toolbar.addAction(self.close_action)
        self.toolbar.addAction(self.close_all_action)
        self.toolbar.addAction(self.mode1_action)
        self.toolbar.addAction(self.mode2_action)


    def new_func(self):
        print('new_func')

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
