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
    QApplication, QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout
)

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.resize(1000, 600)

        self.back_btn = QPushButton()
        self.forward_btn = QPushButton()
        self.refresh_btn = QPushButton()

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.layout_init()

    def layout_init(self):
        self.setLayout(self.v_layout)
        self.v_layout.addLayout(self.h_layout)

        self.h_layout.addWidget(self.back_btn)
        self.h_layout.addWidget(self.forward_btn)
        self.h_layout.addWidget(self.refresh_btn)


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
