#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 23.1 记事本
#
###############################################################################
import sys


from PyQt5.QtWidgets import QMainWindow, QApplication


###############################################################################
class Demo(QMainWindow):

    def __init__(self):
        super(Demo, self).__init__()


###############################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
