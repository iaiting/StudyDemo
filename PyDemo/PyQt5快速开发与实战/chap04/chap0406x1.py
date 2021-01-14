#!/usr/bin/env python3
# -*- coding:utf-8 -*-

################################################################################
#
# 显示气泡提示信息
#
################################################################################
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QToolTip
from PyQt5.QtGui import QFont


class Winform(QWidget):
    def __init__(self):
        super(Winform, self).__init__()
        self.initUI()

    def initUI(self):
        pass
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('这是一个<b>气泡提示</b>')
        self.setGeometry(200, 300, 400, 400)
        self.setWindowTitle('气泡提示demo')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())
