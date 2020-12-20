#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


################################################################################
class MainWidow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWidow, self).__init__(parent)


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWidow()
    form.show()
    sys.exit(app.exec_())
