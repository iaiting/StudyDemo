#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 程序中加入QLabel和QLineEdit控件看下效果
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout
)
from PyQt5.QtCore import Qt


################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.button = QPushButton('button', self)
        self.label = QLabel('label', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.line_edit = QLineEdit(self)

        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)
        self.v_layout.addWidget(self.button)
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.line_edit)


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    qss = 'QPushButton, QLabel, QLineEdit { color: red}'
    demo.setStyleSheet(qss)
    demo.show()
    sys.exit(app.exec_())
