#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# # 1.2 程序运行起点, 用HTML设置QLabel的样式
#
################################################################################
import sys

from PyQt5.QtWidgets import (
    QApplication, QLabel
)

################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel('<font color="red">Hello</font> <h1>Hello World</h1>')
    label.show()
    sys.exit(app.exec_())
