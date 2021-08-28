#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 3.1 垂直布局QVBoxLayout
#
################################################################################
import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel,
    QVBoxLayout,
)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)

        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)

        self.v_layout.addWidget(self.user_label)
        self.v_layout.addWidget(self.pwd_label)


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
