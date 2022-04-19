#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 状态栏
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow,
)

################################################################################
class Example(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.show()

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
