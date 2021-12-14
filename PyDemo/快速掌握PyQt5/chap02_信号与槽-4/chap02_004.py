#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 2.4 一个信号连接多个槽
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton
)

################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton('Start', self)

        self.button.clicked.connect(self.change_text)
        self.button.clicked.connect(self.change_window_size)
        self.button.clicked.connect(self.change_window_title)
    
    def change_text(self):
        print('change text')

    def change_window_size(self):
        print('change window size')

    def change_window_title(self):
        print('change window title')

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
