#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 5.2 完善单行文本输入框和按钮功能
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QVBoxLayout, QWidget
)

USER_PWD = {
    'user': 'password'
}

################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()

        self.user_label = QLabel("Username:", self)
        self.user_line = QLineEdit(self)

        self.pwd_label = QLabel("Password:", self)
        self.pwd_line = QLineEdit(self)

        self.login_button = QPushButton("Log in")
        self.signin_button = QPushButton("Sign in")

        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.layout_init()
        self.lineedit_init()
        self.pushbutton_init()

    def layout_init(self):
        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)

        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.signin_button)

        self.all_v_layout.addLayout(self.grid_layout)
        self.all_v_layout.addLayout(self.h_layout)
        self.setLayout(self.all_v_layout)

    def lineedit_init(self):
        self.user_line.setPlaceholderText('Please enter your username')
        self.pwd_line.setPlaceholderText('Please enter your password')

        self.user_line.textChanged.connect(self.check_input_func)
        self.pwd_line.textChanged.connect(self.check_input_func)

    def check_input_func(self):
        if self.user_line.text() and self.pwd_line.text():
            self.login_button.setEnabled(True)
        else:
            self.login_button.setEnabled(False)

    def pushbutton_init(self):
        self.login_button.setEnabled(False)
        self.login_button.clicked.connect(self.check_login_fucn)

    def check_login_fucn(self):
        if USER_PWD.get(self.user_line.text()) == self.pwd_line.text():
            QMessageBox.information(self, 'Information', 'Log in Successfully!')
        else:
            QMessageBox.critical(self, 'Wrong', 'Wrong Username or Password')


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
