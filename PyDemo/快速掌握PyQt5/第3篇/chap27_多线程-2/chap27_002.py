#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 27.1 QThread类
#
################################################################################

from re import S
import sys
from PyQt5.QtCore import Qt, QThread

from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
)

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.button = QPushButton('Count', self)
        self.button.clicked.connect(self.count_func)

        self.my_thread = MyThread()

        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.button)


    def count_func(self):
        self.my_thread.start()


class MyThread(QThread):
    def __init__(self) -> None:
        super().__init__()
        self.count = 0

    def run(self):
        print('run')
        while True:
            print(self.count)
            self.count += 1
            self.sleep(1)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


