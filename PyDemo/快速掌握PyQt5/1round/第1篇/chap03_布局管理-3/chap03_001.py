#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
#
# 3.1 垂直布局QVBoxLayout
#
################################################################################
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.user_label)
        self.v_layout.addWidget(self.pwd_label)

        self.setLayout(self.v_layout)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
