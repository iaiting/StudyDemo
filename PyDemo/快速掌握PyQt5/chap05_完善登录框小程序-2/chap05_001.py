#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 5.1 登录界面布局
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QLabel, QLineEdit, QWidget, 
    QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton
)

################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 100)

        self.user_label = QLabel('Username:', self)
        self.user_line = QLineEdit(self)

        self.pwd_label = QLabel('Password', self)
        self.pwd_line = QLineEdit(self)

        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.layout_init()

    def layout_init(self):

        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)

        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)

        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.signin_button)

        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        pass

################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())