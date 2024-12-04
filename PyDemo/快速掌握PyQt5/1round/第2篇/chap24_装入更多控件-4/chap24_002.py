#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 24.2 标签页窗口QTabWidget
#
################################################################################
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QDateEdit,
    QGridLayout,
    QLabel,
    QLineEdit,
    QTabWidget,
    QTextEdit,
    QWidget
)

################################################################################
class Demo(QTabWidget):
    def __init__(self) -> None:
        super().__init__()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QTextEdit()

        self.addTab(self.tab1, 'Baseic Info')
        self.addTab(self.tab2, 'Contact Info')
        self.addTab(self.tab3, 'More Info')

        self.tab1_init()
        self.tab2_init()

    def tab1_init(self):
        name_label = QLabel('Name:', self.tab1)
        name_line = QLineEdit(self.tab1)

        gender_label = QLabel('Gender:', self.tab1)
        gender_combox = QComboBox(self.tab1)
        items = ['Please choose your gender', 'Female', 'Male']
        gender_combox.addItems(items)

        brid_label = QLabel('Birth Date:', self.tab1)
        brid_dateedit = QDateEdit(self.tab1)

        grid_layout = QGridLayout()
        self.tab1.setLayout(grid_layout)
        grid_layout.addWidget(name_label, 0, 0, 1, 1)
        grid_layout.addWidget(name_line, 0, 1, 1, 1)
        grid_layout.addWidget(gender_label, 2, 0, 1, 1)
        grid_layout.addWidget(gender_combox, 2, 1, 1, 1)
        grid_layout.addWidget(brid_label, 3, 0, 1, 1)
        grid_layout.addWidget(brid_dateedit, 3, 1, 1, 1)

    def tab2_init(self):
        tel_label = QLabel('Tel:', self.tab2)
        tel_line = QLineEdit()

        mobile_label = QLabel('Mobile:', self.tab2)
        mobile_line = QLineEdit()

        add_label = QLabel('Address:')
        add_line = QLineEdit()

        grid_layout = QGridLayout()
        self.tab2.setLayout(grid_layout)
        grid_layout.addWidget(tel_label, 0, 0, 1, 1)
        grid_layout.addWidget(tel_line, 0, 1, 1, 1)
        grid_layout.addWidget(mobile_label, 1, 0, 1, 1)
        grid_layout.addWidget(mobile_line, 1, 1, 1, 1)
        grid_layout.addWidget(add_label, 2, 0, 1, 1)
        grid_layout.addWidget(add_line, 2, 1, 1, 1)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
