#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 3.3 混合使用QVBoxLayout和QHBoxLayout, 第二种方法
#
################################################################################
import sys
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QApplication, QLabel, QLineEdit, QPushButton

################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        self.user_label = QLabel('Username', self)
        self.user_line = QLineEdit(self)

        self.pwd_label = QLabel('Password', self)
        self.pwd_line = QLineEdit(self)

        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        self.user_h_layout = QHBoxLayout()
        self.pwd_h_layout = QHBoxLayout()
        self.button_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()
        self.all_v_layout.addLayout(self.user_h_layout)
        self.all_v_layout.addLayout(self.pwd_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)
        self.setLayout(self.all_v_layout)

        self.user_h_layout.addWidget(self.user_label)
        self.user_h_layout.addWidget(self.user_line)

        self.pwd_h_layout.addWidget(self.pwd_label)
        self.pwd_h_layout.addWidget(self.pwd_line)

        self.button_h_layout.addWidget(self.login_button)
        self.button_h_layout.addWidget(self.signin_button)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
