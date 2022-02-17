#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 非多线程，ui（app.exec_()）线程界面卡顿
#
################################################################################
import sys
import time
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
)

################################################################################
class Demo0(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.count = 0

        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignCenter)

        self.button = QPushButton('Count', self)
        self.button.clicked.connect(self.count_func)


        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.button)

        self.setLayout(self.v_layout)

    def count_func(self):
        while True:
            print(self.count)
            self.count += 1
            self.label.setText(str(self.count))
            time.sleep(1)



################################################################################
#
# 27.1 QThread类
#
################################################################################
class MyThread(QThread):
    my_signal = pyqtSignal(str)

    def __init__(self):
        super(MyThread, self).__init__()
        self.count = 0
        self.is_on = True

    def run(self):
        while self.is_on:
            print(self.count)
            self.count += 1
            self.my_signal.emit(str(self.count))
            self.sleep(1)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignCenter)

        self.button = QPushButton('Count', self)
        self.button.clicked.connect(self.count_func)

        self.button2 = QPushButton('Stop', self)
        self.button2.clicked.connect(self.stop_count_func)

        self.my_thread = MyThread()
        self.my_thread.my_signal.connect(self.set_label_func)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.button)
        self.v_layout.addWidget(self.button2)
        self.setLayout(self.v_layout)

    def count_func(self):
        self.my_thread.is_on = True
        self.my_thread.start()

    def stop_count_func(self):
        self.my_thread.is_on = False
        self.my_thread.count = 0

        pass

    def set_label_func(self, num):
        self.label.setText(num)

################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

