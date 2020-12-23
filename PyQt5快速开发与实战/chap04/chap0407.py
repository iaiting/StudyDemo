#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMainWindow


class WindowDemo(QWidget):
    def __init__(self):
        super(WindowDemo, self).__init__()
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        # 1 初始化标签控件
        label1.setText("这是一个文本标签。1")
        label2.setText("这是一个文本标签2。2")
        label3.setText("这是一个文本标签3。3")
        label4.setText("4这是一个文本标签4。4")

        # 2 在窗口布局中添加控件
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel 例子")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WindowDemo()
    win.show()
    sys.exit(app.exec_())
