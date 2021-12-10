#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 1.2 程序运行起点，在字符串中加上html代码，修改文本样式
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QLabel
)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel('<h1>Hello World</h1>')
    label.show()
    sys.exit(app.exec_())
