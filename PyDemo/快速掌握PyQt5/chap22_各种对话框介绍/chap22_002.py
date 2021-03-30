#!/usr/bine/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 22.2 输入对话框
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QGridLayout,
)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.name_btn = QPushButton('Name', self)
        self.gender_btn = QPushButton('Gender', self)
        self.age_btn = QPushButton('Age', self)
        self.score_btn = QPushButton('Score', self)
        self.info_btn = QPushButton('Info', self)

        self.g_layout = QGridLayout()
        self.g_layout.addWidget(self.name_btn, 0, 0, 1, 1)
        self.g_layout.addWidget(self.gender_btn, 0, 1, 1, 1)
        self.g_layout.addWidget(self.age_btn, 1, 0, 1, 1)
        self.g_layout.addWidget(self.score_btn, 1, 1, 1, 1)
        self.g_layout.addWidget(self.info_btn, 2, 0, 1, 1)

        self.setLayout(self.g_layout)


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

