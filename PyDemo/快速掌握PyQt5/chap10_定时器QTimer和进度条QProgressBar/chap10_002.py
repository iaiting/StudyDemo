#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 10.2 QProgressBar
#
################################################################################
import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (
    QApplication, QWidget, QProgressBar, QPushButton, QHBoxLayout, QVBoxLayout
)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.progressbar = QProgressBar(self)
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)

        self.step = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_func)

        self.ss_button = QPushButton('Start', self)
        self.ss_button.clicked.connect(self.start_stop_func)

        self.reset_button = QPushButton('Reset', self)
        self.reset_button.clicked.connect(self.reset_func)

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout.addWidget(self.ss_button)
        self.h_layout.addWidget(self.reset_button)

        self.v_layout.addWidget(self.progressbar)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)


    def start_stop_func(self):
        print("start_stop_func")
        if self.ss_button.text() == 'Start':
            self.ss_button.setText('Stop')
            self.timer.start(100)

        else:
            self.ss_button.setText('Start')
            self.timer.stop()

    def reset_func(self):
        print("reset_func")
        self.progressbar.reset()
        self.ss_button.setText('Start')
        self.timer.stop()
        self.step = 0

    def update_func(self):
        print("update_func")
        self.step += 1
        self.progressbar.setValue(self.step)
        if self.step >= 100:
            self.ss_button.setText('Start')
            self.timer.stop()
            self.step = 0

################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
