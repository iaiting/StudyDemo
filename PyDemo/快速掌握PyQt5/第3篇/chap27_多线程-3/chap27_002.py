#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
#
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal

class MyThread(QThread):
    my_signal = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.count = 0

    def run(self):
        while True:
            self.sleep(1)
            print(self.count)
            self.my_signal.emit(str(self.count))

            self.count += 1

class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.label = QLabel('0')
        self.label.setAlignment(Qt.AlignCenter)
        self.button = QPushButton('Count')
        self.button.clicked.connect(self.count_func)

        self.my_thread = MyThread()
        self.my_thread.my_signal.connect(self.set_lable_func)

        self.v_layout = QVBoxLayout(self)
        self.setLayout(self.v_layout)
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.button)

    def count_func(self):
        print('count_func')
        self.my_thread.start()


    def set_lable_func(self, num):
        self.label.setText(num)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
