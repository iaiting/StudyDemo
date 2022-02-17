#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 5.3 完善注册界面布局及功能 & 5.4 整合登录界面和注册界面
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QVBoxLayout, QWidget
)

USER_PWD = {
    'user': 'password'
}
################################################################################
class SigninPage(QDialog):
    def __init__(self):
        super().__init__()
        self.signin_user_label = QLabel('Username:',self)
        self.signin_user_line = QLineEdit(self)

        self.signin_pwd1_label = QLabel('Password:')
        self.signin_pwd1_line = QLineEdit(self)

        self.signin_pwd2_label = QLabel('Password:')
        self.signin_pwd2_line = QLineEdit(self)

        self.signin_button = QPushButton('Sign in', self)

        self.user_h_layout = QHBoxLayout()
        self.pwd_h_layout = QHBoxLayout()
        self.pwd2_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.layout_init()
        self.lineedit_init()
        self.pushbutton_init()

    def layout_init(self):
        self.user_h_layout.addWidget(self.signin_user_label)
        self.user_h_layout.addWidget(self.signin_user_line)

        self.pwd_h_layout.addWidget(self.signin_pwd1_label)
        self.pwd_h_layout.addWidget(self.signin_pwd1_line)

        self.pwd2_h_layout.addWidget(self.signin_pwd2_label)
        self.pwd2_h_layout.addWidget(self.signin_pwd2_line)

        self.all_v_layout.addLayout(self.user_h_layout)
        self.all_v_layout.addLayout(self.pwd_h_layout)
        self.all_v_layout.addLayout(self.pwd2_h_layout)
        self.all_v_layout.addWidget(self.signin_button)

        self.setLayout(self.all_v_layout)

    def lineedit_init(self):
        self.signin_user_line.textChanged.connect(self.check_input_func)
        self.signin_pwd1_line.textChanged.connect(self.check_input_func)
        self.signin_pwd2_line.textChanged.connect(self.check_input_func)

    def check_input_func(self):
        if self.signin_user_line.text() and self.signin_pwd1_line.text() and self.signin_pwd2_line.text():
            self.signin_button.setEnabled(True)
        else:
            self.signin_button.setEnabled(False)


    def pushbutton_init(self):
        self.signin_button.setEnabled(False)
        self.signin_button.clicked.connect(self.check_signin_func)

    def check_signin_func(self):
        if self.signin_pwd1_line.text() != self.signin_pwd2_line.text():
            QMessageBox.critical(self, 'Wrong', 'Two Passwords Typed Are Not Same!')
        elif self.signin_user_line.text() not in USER_PWD:
            QMessageBox.information(self, 'Information', 'Register Successfully')
            self.close()
        else:
            QMessageBox.critical(self, 'Wrong', 'This Username Has Been Registered!')
        
        self.signin_user_line.clear()
        self.signin_pwd1_line.clear()
        self.signin_pwd2_line.clear()

################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 100)
        
        self.user_label = QLabel("Username:", self)
        self.user_line = QLineEdit(self)

        self.pwd_label = QLabel("Password:", self)
        self.pwd_line = QLineEdit(self)

        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        self.user_h_layout = QHBoxLayout()
        self.pwd_h_layout = QHBoxLayout()
        self.button_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.layout_init()
        self.lineedit_init()
        self.pushbutton_init()

        self.signin_page = SigninPage()

    def layout_init(self):
        self.setLayout(self.all_v_layout)
        self.all_v_layout.addLayout(self.user_h_layout)
        self.all_v_layout.addLayout(self.pwd_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)

        self.user_h_layout.addWidget(self.user_label)
        self.user_h_layout.addWidget(self.user_line)

        self.pwd_h_layout.addWidget(self.pwd_label)
        self.pwd_h_layout.addWidget(self.pwd_line)

        self.button_h_layout.addWidget(self.login_button)
        self.button_h_layout.addWidget(self.signin_button)

    def lineedit_init(self):
        self.user_line.setPlaceholderText('Please enter your username')
        self.pwd_line.setPlaceholderText('Please enter your password')
        self.pwd_line.setEchoMode(QLineEdit.Password)

        self.user_line.textChanged.connect(self.check_input_func)
        self.pwd_line.textChanged.connect(self.check_input_func)

    def pushbutton_init(self):
        self.login_button.setEnabled(False)
        self.login_button.clicked.connect(self.check_login_func)
        self.signin_button.clicked.connect(self.show_signin_page_func)

    def check_input_func(self):
        pass

    def check_login_func(self):
        pass

    def show_signin_page_func(self):
        self.signin_page.exec_()

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
