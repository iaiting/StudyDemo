#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 勾选菜单
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QMainWindow, QAction, QApplication
)


################################################################################
class Example(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.show()

################################################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
