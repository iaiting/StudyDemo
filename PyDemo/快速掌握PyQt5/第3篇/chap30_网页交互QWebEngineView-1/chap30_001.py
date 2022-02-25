#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 30.1 制作简单浏览器
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, 
    QLineEdit,
)
from PyQt5.QtWebEngineWidgets import QWebEngineView

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.resize(1000, 600)

        self.back_btn = QPushButton()
        self.forward_btn = QPushButton()
        self.refresh_btn = QPushButton()
        self.zoom_in_btn = QPushButton()
        self.zoom_out_btn = QPushButton()
        self.url_line = QLineEdit()

        self.browser = QWebEngineView()

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.layout_init()
        self.line_init()

    def layout_init(self):
        self.setLayout(self.v_layout)

        self.h_layout.addWidget(self.url_line)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.browser)

    def line_init(self):
        self.url_line.setFixedWidth(400)


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
