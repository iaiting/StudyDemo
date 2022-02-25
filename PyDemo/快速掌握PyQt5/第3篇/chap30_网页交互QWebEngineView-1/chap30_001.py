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

        self.back_btn = QPushButton('后退')
        self.forward_btn = QPushButton('前进')
        self.refresh_btn = QPushButton('刷新')
        self.zoom_in_btn = QPushButton('缩小')
        self.zoom_out_btn = QPushButton('放大')
        self.url_line = QLineEdit()

        self.browser = QWebEngineView()

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.layout_init()
        self.btn_init()
        self.line_init()

    def layout_init(self):
        self.setLayout(self.v_layout)
        self.h_layout.setSpacing(0)

        self.h_layout.addWidget(self.back_btn)
        self.h_layout.addWidget(self.forward_btn)
        self.h_layout.addWidget(self.refresh_btn)

        self.h_layout.addStretch(2)

        self.h_layout.addWidget(self.url_line)

        self.h_layout.addStretch(2)

        self.h_layout.addWidget(self.zoom_in_btn)
        self.h_layout.addWidget(self.zoom_out_btn)

        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.browser)

    def btn_init(selfs):
        pass

    def line_init(self):
        self.url_line.setFixedWidth(400)
        self.url_line.setPlaceholderText('Search or enter website name')


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
