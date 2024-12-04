#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 28.1 基本规则
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QHBoxLayout
)

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.button1 = QPushButton('super class', self)
        self.button2 = SubButton()

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.button1)
        self.h_layout.addWidget(self.button2)
        self.setLayout(self.h_layout)


################################################################################
class SubButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText('sub class')

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    qss = 'QPushButton {color: red; background: blue}'
    demo.setStyleSheet(qss)
    demo.show()
    sys.exit(app.exec_())