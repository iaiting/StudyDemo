#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 3.4 表单布局QFormLayout
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QFormLayout, QHBoxLayout, QVBoxLayout,
)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        self.f_layout = QFormLayout()
        self.button_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.all_v_layout.addLayout(self.f_layout)
        self.all_v_layout.addLayout(self.button_h_layout)

        self.setLayout(self.all_v_layout)

        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)

        self.f_layout.addRow(self.user_label, self.user_line)
        self.f_layout.addRow(self.pwd_label, self.pwd_line)

        self.login_button = QPushButton('Log in')
        self.signin_button = QPushButton('Sign in')
        self.button_h_layout.addWidget(self.login_button)
        self.button_h_layout.addWidget(self.signin_button)


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
