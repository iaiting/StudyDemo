#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 1.2 程序运行起点，字符串中加上html代码，修改文本样式。
#
################################################################################
import sys
from PyQt5.QtWidgets import QApplication, QLabel

################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    lable = QLabel()
    lable.setText('<font color="red">Hello</font> <h1>World</h1>')
    lable.show()
    sys.exit(app.exec_())
