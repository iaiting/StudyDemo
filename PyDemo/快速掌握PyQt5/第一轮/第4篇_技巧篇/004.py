#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 在线程中获取窗口控件内容
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QLabel,
)
from PyQt5.QtCore import QThread

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.line = QLineEdit()
        self.btn = QPushButton('开始爬取')
        self.btn.clicked.connect(self.start_slot)


        self.crawthread = CrawThread(self)

        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        self.setLayout(v_layout)

        h_layout.addWidget(QLabel('网址:'))
        h_layout.addWidget(self.line)

        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.btn)

    def start_slot(self):
        print('start_slot')
        self.crawthread.start()


################################################################################
class CrawThread(QThread):
    def __init__(self, demo) -> None:
        super().__init__()
        self.demo = demo

    def run(self):
        url = self.demo.line.text().strip()
        print(f'要爬取的网址为: {url}')

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())