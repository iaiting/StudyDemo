#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 5.2 完善单行文本输入框和按钮功能
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QLineEdit, QWidget,
    QGridLayout, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QMessageBox
)

USER_PWD = {
    'user': 'password'
}

################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)

        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.user_label = QLabel('Username:', self)
        self.user_line = QLineEdit(self)

        self.pwd_label = QLabel('Password:', self)
        self.pwd_line = QLineEdit(self)

        self.login_button = QPushButton("Log in", self)
        self.signin_button = QPushButton("Sign in", self)

        self.layout_init()
        self.pushbutton_init()
        self.line_init()

    def layout_init(self):
        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)

        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.signin_button)

    def line_init(self):
        self.user_line.setPlaceholderText('Please enter your name')
        self.user_line.textChanged.connect(self.check_input_func)

        self.pwd_line.setPlaceholderText('Please enter your password')
        self.pwd_line.textChanged.connect(self.check_input_func)


    def pushbutton_init(self):
        self.login_button.setEnabled(False)
        self.login_button.clicked.connect(self.check_login_func)

    def check_input_func(self):
        print("check_input_func")
        if self.user_line.text() and self.pwd_line.text():
            self.login_button.setEnabled(True)
        else:
            self.login_button.setEnabled(False)

    def check_login_func(self):
        if USER_PWD.get(self.user_line.text()) == self.pwd_line.text():
            QMessageBox.information(self, 'Information', 'Log in Successfully!')
        else:
            QMessageBox.critical(self, 'Wrong', 'Wrong Username or Password')

        self.user_line.clear()
        self.pwd_line.clear()


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
