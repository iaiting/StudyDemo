#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 24.1 拆分窗口QSplitter
#
################################################################################
import sys

from PyQt5.QtWidgets import (
    QWidget, QApplication
)

class Demo(QWidget):
    pass

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())