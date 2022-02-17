#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 24.3 堆叠窗口QStackedWidget
#
################################################################################
from email.charset import add_alias
from re import S
import sys
from PyQt5.QtWidgets import (
    QWidget, QApplication, QTextEdit, 
    QStackedWidget, QHBoxLayout, QListWidget, 
    QLabel, QLineEdit, QComboBox, QGridLayout, 
    QDateEdit,
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
        self.stacked_widget.currentChanged.connect(lambda: print(self.stacked_widget.currentIndex()))

        self.list_widget = QListWidget()
        self.list_widget.addItem('Basic Info')
        self.list_widget.addItem('Contact Info')
        self.list_widget.addItem('More Info')
        self.list_widget.clicked.connect(self.change_func)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.list_widget)
        self.h_layout.addWidget(self.stacked_widget)
        self.setLayout(self.h_layout)

    def stack1_init(self):
        name_label = QLabel('Name:', self.stack1)
        name_line = QLineEdit()

        gender_label = QLabel('Gender:', self.stack1)
        gender_combox = QComboBox(self.stack1)
        items = ['Please choose your gender', 'Female', 'Male']
        gender_combox.addItems(items)

        bd_label = QLabel('Birth Date:')
        bd_dateedit = QDateEdit()

        g_layout = QGridLayout()
        self.stack1.setLayout(g_layout)

        g_layout.addWidget(name_label, 0, 0, 1, 1)
        g_layout.addWidget(name_line, 0, 1, 1, 1)
        g_layout.addWidget(gender_label, 1, 0, 1, 1)
        g_layout.addWidget(gender_combox, 1, 1, 1, 1)
        g_layout.addWidget(bd_label, 2, 0, 1, 1)
        g_layout.addWidget(bd_dateedit, 2, 1, 1, 1)

    def stack2_init(self):
        tel_label = QLabel('Tel:')
        tel_line = QLineEdit()

        mobile_label = QLabel('Mobile:')
        mobile_line = QLineEdit()

        add_label = QLabel('Address:')
        add_line = QLineEdit()


        g_layout = QGridLayout()
        self.stack2.setLayout(g_layout)

        g_layout.addWidget(tel_label, 0, 0, 1, 1)
        g_layout.addWidget(tel_line, 0, 1, 1, 1)

        g_layout.addWidget(mobile_label, 1, 0, 1, 1)
        g_layout.addWidget(mobile_line, 1, 1, 1, 1)

        g_layout.addWidget(add_label, 2, 0, 1, 1)
        g_layout.addWidget(add_line, 2, 1, 1, 1)

    def change_func(self):
        print('change_func')
        self.stacked_widget.setCurrentIndex(self.list_widget.currentIndex().row())

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
