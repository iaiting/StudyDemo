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

from PyQt5.QtCore import Qt
################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.label = QLabel('0')
        self.label.setAlignment(Qt.AlignCenter)

        self.button = QPushButton('Start')
        self.button_2 = QPushButton('Stop')

        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)

        self.v_layout.addWidget(self.label)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.button)
        self.h_layout.addWidget(self.button_2)
        self.v_layout.addLayout(self.h_layout)
        
        


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
