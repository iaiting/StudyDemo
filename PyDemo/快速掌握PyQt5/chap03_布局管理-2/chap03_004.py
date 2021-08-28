#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 3.4 表单布局QFormLayout
#
################################################################################
import sys

from PyQt5.QtWidgets import (
    QApplication, QHBoxLayout, QWidget, QFormLayout, 
    QLabel, QLineEdit,
    QVBoxLayout, QPushButton,
)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()

        self.all_v_layout = QVBoxLayout()
        self.setLayout(self.all_v_layout)

        self.f_layout = QFormLayout()
        self.button_h_layout = QHBoxLayout()
        self.all_v_layout.addLayout(self.f_layout)
        self.all_v_layout.addLayout(self.button_h_layout)

        self.user_label = QLabel('Username:', self)
        self.user_line = QLineEdit(self)
        self.f_layout.addRow(self.user_label, self.user_line)

        self.pwd_label = QLabel('Passwd:', self)
        self.pwd_line = QLineEdit(self)
        self.f_layout.addRow(self.pwd_label, self.pwd_line)

        self.login_btn = QPushButton('Log in', self)
        self.sign_btn = QPushButton('Sign in', self)
        self.button_h_layout.addWidget(self.login_btn)
        self.button_h_layout.addWidget(self.sign_btn)


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
