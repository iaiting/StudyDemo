#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 28.4 伪状态
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QComboBox, QVBoxLayout
)

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.button1 = QPushButton('button1', self)
        self.button2 = QPushButton('button2', self)
        self.button2.setProperty('name', 'btn2')

        my_list = ['A', 'B', 'C', 'D']
        self.combox = QComboBox(self)
        self.combox.addItems(my_list)

        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)

        self.v_layout.addWidget(self.button1)
        self.v_layout.addWidget(self.button2)
        self.v_layout.addWidget(self.combox)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    qss = '''
    QPushButton:hover {background-color: red}
    QPushButton[name='btn2']:pressed {background-color: blue}
    QComboBox::drop-down:hover {background-color: green}
    '''
    demo.setStyleSheet(qss)
    demo.show()
    sys.exit(app.exec_())
