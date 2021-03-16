#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 2.1 通过按钮来改变文本（一个信号连接一个槽）
#
################################################################################
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

