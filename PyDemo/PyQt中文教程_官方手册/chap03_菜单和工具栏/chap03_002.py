#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 菜单栏
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication
)

from PyQt5.QtGui import QIcon
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
