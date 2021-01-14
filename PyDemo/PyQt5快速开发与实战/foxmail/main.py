#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QMainWindow, QPushButton


class CTopWidget(QWidget):
    pass


class CLeftWidget(QWidget):
    def __init__(self):
        super(CLeftWidget, self).__init__()
        layout = QVBoxLayout()

        btn1 = QPushButton("111")
        btn2 = QPushButton("112")
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setLayout(layout)


class CMiddleWidget(QWidget):
    def __init__(self):
        super(CMiddleWidget, self).__init__()
        layout = QVBoxLayout()
        mail1 = QLabel('111')
        mail2 = QLabel('112')
        layout.addWidget(mail1)
        layout.addWidget(mail2)
        self.setLayout(layout)


class CRightWidget(QWidget):
    pass


class CContenWidget(QWidget):
    def __init__(self):
        super(CContenWidget, self).__init__()
        layout = QHBoxLayout()
        layout.addWidget(CLeftWidget())
        layout.addWidget(CMiddleWidget())
        layout.addWidget(CRightWidget())
        self.setLayout(layout)


class CMainAppWindow(QMainWindow):
    def __init__(self):
        super(CMainAppWindow, self).__init__()

        main_frame = CContenWidget()
        self.setCentralWidget(main_frame)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = CMainAppWindow()
    # mainwindow = CLeftWidget()
    mainwindow.show()
    sys.exit(app.exec_())
