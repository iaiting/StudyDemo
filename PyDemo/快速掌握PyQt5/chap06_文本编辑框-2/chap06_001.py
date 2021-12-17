#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 6.1 同步显示文本
#
################################################################################
import sys

from PyQt5.QtWidgets import (
    QApplication, QHBoxLayout, QLabel, QVBoxLayout, QWidget
)
################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.edit_label = QLabel('QTextEdit', self)
        self.browser_label = QLabel('QTextBrowser', self)

        self.edit_v_layout = QVBoxLayout()
        self.browser_v_layout = QVBoxLayout()
        self.all_h_layout = QHBoxLayout()

        self.layout_init()

    def layout_init(self):
        self.all_h_layout.addLayout(self.edit_v_layout)
        self.all_h_layout.addLayout(self.browser_v_layout)
        self.setLayout(self.all_h_layout)

        self.edit_v_layout.addWidget(self.edit_label)
        self.browser_v_layout.addWidget(self.browser_label)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())