#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 24.3 堆叠窗口QStackedWidget
#
################################################################################
import sys
from unicodedata import name
from PyQt5.QtWidgets import (
    QApplication, QWidget, QListWidget, 
    QHBoxLayout,
    QTextEdit, QLabel, QStackedWidget
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
        self.list_widget.clicked.connect(self.change_func)

        self.h_layout = QHBoxLayout()
        self.setLayout(self.h_layout)
        self.h_layout.addWidget(self.list_widget)
        self.h_layout.addWidget(self.stacked_widget)

    def stack1_init(self):
        print('stack1_init')
        name_label = QLabel('Name:', self.stack1)

    def stack2_init(self):
        print('stack2_init')
        name_label = QLabel('Name2:', self.stack2)


    def change_func(self):
        self.stacked_widget.setCurrentIndex(self.list_widget.currentIndex().row())


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
