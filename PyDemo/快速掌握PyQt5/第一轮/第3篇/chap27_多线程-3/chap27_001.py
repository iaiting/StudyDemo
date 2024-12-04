#!/usr/bin/env python3
#-*- coding: utf-8 -*-

################################################################################
#
# 非多线程，ui（app.exec_()）线程界面卡顿
#
################################################################################
import sys
import time
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
)
from PyQt5.QtCore import Qt


################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.count = 0

        self.button = QPushButton('Count')
        self.button.clicked.connect(self.count_func)
        
        self.label = QLabel('0')
        self.label.setAlignment(Qt.AlignCenter)

        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)

        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.button)

    def count_func(self):
        print('Enter count_func:')
        while True:
            self.count += 1
            print(self.count)
            self.label.setText(str(self.count))
            time.sleep(1)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
