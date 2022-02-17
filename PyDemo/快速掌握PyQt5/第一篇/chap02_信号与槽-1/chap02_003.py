#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
#
# 2.3 一个信号与另外一个信号连接
#
###############################################################################
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Start', self)

        self.button.pressed.connect(self.button.released)
        self.button.released.connect(self.change_text)

    def change_text(self):
        if self.button.text() == 'Start':
            self.button.setText('Stop')
        else:
            self.button.setText('Start')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    app.exec_()

