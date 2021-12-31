#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 9.2 QDial
#
################################################################################
import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QDial,
    QHBoxLayout,
    QLabel,
    QWidget
)

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('QDial')
        
        self.dial = QDial()
        self.dial.setFixedSize(100, 100)
        self.dial.setRange(10, 50)
        self.dial.setNotchesVisible(True)
        self.dial.valueChanged.connect(self.on_change_func)

        self.label = QLabel('0')
        self.label.setFont(QFont('Arial Black', 20))
        # self.label.setFixedWidth(20)

        self.h_layout = QHBoxLayout()
        self.setLayout(self.h_layout)
    
        self.h_layout.addWidget(self.dial)
        self.h_layout.addWidget(self.label)

    def on_change_func(self):
        self.label.setText(str(self.dial.value()))

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

