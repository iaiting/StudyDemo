#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 2.5 自定义信号
#
################################################################################
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


################################################################################
class Demo(QWidget):
    my_signal = pyqtSignal()

    def __init__(self):
        super(Demo, self).__init__()
        self.label = QLabel('Hello World', self)
        self.my_signal.connect(self.change_text)

    def change_text(self):
        if self.label.text() == 'Hello World':
            self.label.setText('Hello PyQt5')
        else:
            self.label.setText('Hello World')


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
