#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 3.3 混合使用QVBoxLayout和QHBoxLayout
#
################################################################################

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout
)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)

        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)

        self.login_button = QPushButton('Log in', self)
        self.sigin_button = QPushButton('Sign in', self)

        self.label_v_layout = QVBoxLayout()
        self.line_v_layout = QVBoxLayout()
        self.label_line_h_layout = QHBoxLayout()
        self.button_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.label_v_layout.addWidget(self.user_label)
        self.label_v_layout.addWidget(self.pwd_label)

        self.line_v_layout.addWidget(self.user_line)
        self.line_v_layout.addWidget(self.pwd_line)

        self.button_h_layout.addWidget(self.login_button)
        self.button_h_layout.addWidget(self.sigin_button)

        self.label_line_h_layout.addLayout(self.label_v_layout)
        self.label_line_h_layout.addLayout(self.line_v_layout)

        self.all_v_layout.addLayout(self.label_line_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)

        self.setLayout(self.all_v_layout)




################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
