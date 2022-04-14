#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 应用程序的图标
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget
)
from PyQt5.QtGui import QIcon

################################################################################
class Example(QWidget):
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

