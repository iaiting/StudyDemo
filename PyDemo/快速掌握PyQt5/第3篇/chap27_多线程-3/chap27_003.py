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
    QVBoxLayout, 
)

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.label = QLabel('0')

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        
        self.setLayout(self.v_layout)


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
