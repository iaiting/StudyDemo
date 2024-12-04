#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 3.5 网格布局QGridLayout
#
################################################################################
import sys

from PyQt5.QtWidgets import (
    QApplication, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget,
    QHBoxLayout, QVBoxLayout, QGridLayout, 
)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()

        self.user_label = QLabel('Username:', self)
        self.user_line = QLineEdit(self)

        self.pwd_label = QLabel('Password:', self)
        self.pwd_line = QLineEdit(self)

        self.login_btn = QPushButton('Log in', self)
        self.signin_btn = QPushButton('Sign in', self)

        self.v_layout = QVBoxLayout()
        self.g_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout.addLayout(self.g_layout)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

        self.g_layout.addWidget(self.user_label, 0, 0, 1, 1)
        self.g_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.g_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.g_layout.addWidget(self.pwd_line, 1, 1, 1, 1)

        self.h_layout.addWidget(self.login_btn)
        self.h_layout.addWidget(self.signin_btn)
        

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
