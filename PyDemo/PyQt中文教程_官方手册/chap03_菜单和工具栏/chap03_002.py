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
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.show()



################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
