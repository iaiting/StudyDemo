#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 简单的例子
#
################################################################################
# from ctypes import resize
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget,
)

# from PySide2.QtWidgets import QApplication, QWidget

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec_())
