#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#################################################################################
#
#
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QVBoxLayout, QHBoxLayout,
)

################################################################################
from PyQt5.QtCore import (
    Qt, QThread, pyqtSignal
)

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.label = QLabel('0')
        self.label.setAlignment(Qt.AlignCenter)

        self.button = QPushButton('Start')
        self.button.clicked.connect(self.count_func)

        self.button_2 = QPushButton('Stop')
        self.button_2.clicked.connect(self.stop_count_func)

        self.my_thread = MyThread()
        self.my_thread.my_signal.connect(self.set_label_func)

        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)

        self.v_layout.addWidget(self.label)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.button)
        self.h_layout.addWidget(self.button_2)
        self.v_layout.addLayout(self.h_layout)


    def count_func(self):
        self.my_thread.is_on = True
        self.my_thread.start()

    def stop_count_func(self):
        self.my_thread.is_on = False
        self.my_thread.count = 0
        self.label.setText(str(self.my_thread.count))


    def set_label_func(self, num):
        self.label.setText(num)
################################################################################
class MyThread(QThread):
    my_signal = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.count = 0
        self.is_on = True

    def run(self):
        print('run')
        while self.is_on:
            print(self.count)
            self.sleep(1)
            self.my_signal.emit(str(self.count))
            self.count += 1
            
            
            


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
