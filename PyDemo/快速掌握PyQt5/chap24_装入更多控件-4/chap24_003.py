#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 24.3 堆叠窗口QStackedWidget
#
################################################################################
from re import S
import sys
from PyQt5.QtWidgets import (
    QWidget, QApplication, QTextEdit, 
    QStackedWidget, QHBoxLayout, QListWidget
)

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QTextEdit()

        self.stack1_init()
        self.stack2_init()

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.stack1)
        self.stacked_widget.addWidget(self.stack2)
        self.stacked_widget.addWidget(self.stack3)

        self.list_widget = QListWidget()
        self.list_widget.addItem('Basic Info')
        self.list_widget.addItem('Contact Info')
        self.list_widget.addItem('More Info')

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.list_widget)
        self.h_layout.addWidget(self.stacked_widget)
        self.setLayout(self.h_layout)

    def stack1_init(self):
        pass

    def stack2_init(self):
        pass

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
