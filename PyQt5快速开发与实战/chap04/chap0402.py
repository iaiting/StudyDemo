#!/usr/bin/env python3
# -*- coding:utf-8 -*-

################################################################################
#
# 案例 4-2 主窗口居中显示
#
################################################################################
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow
import sys


################################################################################
class Winform(QMainWindow):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())
