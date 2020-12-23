#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        label1 = QLabel('邮箱账号')
        label2 = QLabel("邮件列表")
        label3 = QLabel("邮件详情")

        layout1 = QVBoxLayout()

        layout = QHBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())