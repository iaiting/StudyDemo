#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 24.2 标签页窗口QTabWidget
#
################################################################################

import sys
from PyQt5.QtWidgets import (
    QWidget, QApplication
)

class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

