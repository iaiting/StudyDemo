#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class WindowDemo(QWidget):
    def __init__(self):
        super(WindowDemo, self).__init__()
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        # 1 初始化标签控件
        label1.setText("这是一个文本标签。1")

        label2.setText("<a href='#'>欢迎使用Python GUI 应用</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("./images/python.jpg"))

        label4.setText("<a href='htttp://www.baidu.com'>欢迎访问百度</a>")
        label4.setToolTip('这是一个超级连接标签')

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
