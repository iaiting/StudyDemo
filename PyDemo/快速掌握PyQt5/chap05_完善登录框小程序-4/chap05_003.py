#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 5.3 完善注册界面布局及功能
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
    pass

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = SigninPage()
    demo.show()
    sys.exit(app.exec_())
