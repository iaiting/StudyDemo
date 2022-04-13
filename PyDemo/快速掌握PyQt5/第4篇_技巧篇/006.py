#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 浏览框滑动条自动下滑到底
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, 
    QTextEdit, QTextBrowser, QPushButton,
)
from PyQt5.QtGui import QTextCursor

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.edit = QTextEdit()
        self.browser = QTextBrowser()
        self.add_btn = QPushButton('添加')
        self.add_btn.clicked.connect(self.add_text)


        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        h_layout.addWidget(self.edit)
        h_layout.addWidget(self.browser)

        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.add_btn)
        self.setLayout(v_layout)

    def add_text(self):
        text = self.edit.toPlainText()
        self.browser.append(text)
        self.browser.moveCursor(QTextCursor.End)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

