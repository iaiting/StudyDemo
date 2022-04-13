#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# QTableWidget单元格文本居中
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, 
    QVBoxLayout,
)


################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.resize(500, 300)

        self.btn = QPushButton('文本居中')
    
        v_layout = QVBoxLayout()
        self.setLayout(v_layout)
        
        v_layout.addWidget(self.btn)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())