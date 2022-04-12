#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
#
#
#
################################################################################
import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit,
    QHBoxLayout, QVBoxLayout
)

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.resize(1000, 600)

        self.back_btn = QPushButton('后退')
        self.forward_btn = QPushButton('前进')
        self.refresh_btn = QPushButton('刷新')

        self.url_le = QLineEdit()
        self.zoom_in_btn = QPushButton('放大')
        self.zoom_out_btn = QPushButton('缩小')

        self.browser = QWebEngineView()

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.layout_init()
        self.btn_init()
        self.le_init()

    def layout_init(self):

        self.h_layout.setSpacing(0)
        self.h_layout.addWidget(self.back_btn)
        self.h_layout.addWidget(self.forward_btn)
        self.h_layout.addWidget(self.refresh_btn)

        self.h_layout.addStretch(2)
        self.h_layout.addWidget(self.url_le)
        self.h_layout.addStretch(2)

        self.h_layout.addWidget(self.zoom_in_btn)
        self.h_layout.addWidget(self.zoom_out_btn)

        self.setLayout(self.v_layout)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.browser)

    def btn_init(self):
        pass

    def le_init(self):
        self.url_le.setFixedWidth(400)
        self.url_le.setPlaceholderText('Search or enter website name')
        pass


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
