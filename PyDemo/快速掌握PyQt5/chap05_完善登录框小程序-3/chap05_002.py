#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 5.2 完善单行文本输入框和按钮功能
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QLineEdit,
    QHBoxLayout, QVBoxLayout, QGridLayout
)

################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()

        self.user_label = QLabel('Username:', self)
        self.user_line = QLineEdit(self)

        self.pwd_label = QLabel('Password:', self)
        self.pwd_line = QLineEdit(self)

        self.all_v_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()

        self.layout_init()

    def layout_init(self):
        self.grid_layout.addWidget(self.user_label, 0, 0)
        self.grid_layout.addWidget(self.user_line, 0, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0)
        self.grid_layout.addWidget(self.pwd_line, 1, 1)

        self.all_v_layout.addLayout(self.grid_layout)
        self.setLayout(self.all_v_layout)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
