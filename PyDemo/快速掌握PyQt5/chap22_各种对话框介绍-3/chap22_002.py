#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 22.2 输入对话框
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QGridLayout, QLineEdit, QPushButton, QWidget
)

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.name_btn = QPushButton('Name', self)
        self.name_line = QLineEdit(self)

        self.gender_btn = QPushButton('Gender', self)
        self.gender_line = QLineEdit(self)

        self.age_btn = QPushButton('Age', self)
        self.age_line = QLineEdit(self)

        self.score_btn = QPushButton('Score', self)
        self.score_line = QLineEdit(self)

        self.name_btn.clicked.connect(lambda: self.open_dialog_func(self.name_btn))
        self.gender_btn.clicked.connect(lambda: self.open_dialog_func(self.gender_btn))
        self.age_btn.clicked.connect(lambda: self.open_dialog_func(self.age_btn))
        self.score_btn.clicked.connect(lambda: self.open_dialog_func(self.score_btn))

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.name_btn, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.name_line, 0, 1, 1, 1)

        self.grid_layout.addWidget(self.gender_btn, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.gender_line, 1, 1, 1, 1)

        self.grid_layout.addWidget(self.age_btn, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.age_line, 2, 1, 1, 1)

        self.grid_layout.addWidget(self.score_btn, 3, 0, 1, 1)
        self.grid_layout.addWidget(self.score_line, 3, 1, 1, 1)


    def open_dialog_func(self, btn):
        if btn == self.name_btn:
            print('name_btn')
        elif btn == self.gender_btn:
            print('gender_btn')
        elif btn == self.age_btn:
            print('age_btn')
        elif btn == self.score_btn:
            print('score_btn')
        else:
            print('else')

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
