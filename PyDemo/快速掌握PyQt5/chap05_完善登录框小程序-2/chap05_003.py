#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 5.3 完善注册界面布局及功能
#
################################################################################
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout

################################################################################
class SigninPage(QDialog):
    def __init__(self):
        super().__init__()
        self.signin_user_label = QLabel('Username', self)
        self.signin_user_line = QLineEdit(self)

        self.signin_pwd_label = QLabel('Password', self)
        self.signin_pwd_line = QLineEdit(self)

        self.signin_pwd2_label = QLabel('Password', self)
        self.signin_pwd2_line = QLineEdit(self)

        self.signin_button = QPushButton('Sign in', self)

        self.user_h_layout = QHBoxLayout()
        self.pwd_h_layout = QHBoxLayout()
        self.pwd2_h_layout = QHBoxLayout()
        self.all_v_layout= QVBoxLayout()

        self.layout_init()

    def layout_init(self):
        self.user_h_layout.addWidget(self.signin_user_label)
        self.user_h_layout.addWidget(self.signin_user_line)

        self.pwd_h_layout.addWidget(self.signin_pwd_label)
        self.pwd_h_layout.addWidget(self.signin_pwd_line)

        self.pwd2_h_layout.addWidget(self.signin_pwd2_label)
        self.pwd2_h_layout.addWidget(self.signin_pwd2_line)

        self.all_v_layout.addLayout(self.user_h_layout)
        self.all_v_layout.addLayout(self.pwd_h_layout)
        self.all_v_layout.addLayout(self.pwd2_h_layout)
        self.all_v_layout.addWidget(self.signin_button)

        self.setLayout(self.all_v_layout)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = SigninPage()
    demo.show()
    sys.exit(app.exec_())
