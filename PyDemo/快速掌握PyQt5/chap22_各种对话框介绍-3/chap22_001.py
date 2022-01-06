#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 22.1 颜色对话框和字体对话框
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QHBoxLayout, QPushButton, QTextEdit, QVBoxLayout, QWidget
)

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.textedit = QTextEdit(self)
        self.color_btn = QPushButton('Color', self)
        self.font_btn = QPushButton('Font', self)

        self.color_btn.clicked.connect(lambda: self.open_dialog_func(self.color_btn))
        self.font_btn.clicked.connect(lambda: self.open_dialog_func(self.font_btn))

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.color_btn)
        self.h_layout.addWidget(self.font_btn)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.textedit)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def open_dialog_func(self, btn):
        print('open_dialog_func: ', btn)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())