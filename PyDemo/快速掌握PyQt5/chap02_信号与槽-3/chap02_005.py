#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
#
#
################################################################################
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
