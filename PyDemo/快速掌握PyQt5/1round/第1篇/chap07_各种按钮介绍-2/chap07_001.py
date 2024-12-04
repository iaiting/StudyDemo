#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 7.1 QPushButton
#
################################################################################
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication, QPushButton, QWidget
)

################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.test_button = QPushButton('Test', self)
        self.test_button.setIcon(QIcon('win.png'))
        self.test_button.setCheckable(True)
        self.test_button.toggled.connect(self.button_state_func)

    def button_state_func(self):
        print(self.test_button.isChecked())

################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
