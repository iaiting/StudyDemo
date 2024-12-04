#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 1.2 程序运行起点
#
################################################################################
import sys
from PyQt5.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel('Hello World')
    label.show()
    sys.exit(app.exec_())
