#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 菜单栏
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, qApp,
    QAction,
)

from PyQt5.QtGui import QIcon
################################################################################
class Example(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAct = QAction('Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')

        self.show()



################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
