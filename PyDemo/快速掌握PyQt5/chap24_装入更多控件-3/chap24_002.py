#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 24.2 标签页窗口QTabWidget
#
################################################################################

import sys
from PyQt5.QtCore import qWarning
from PyQt5.QtWidgets import (
    QComboBox, QDateEdit, QGridLayout, QLabel, QLineEdit, QTabWidget, QTableView, QWidget, QApplication
)
from PyQt5.QtGui import (
    QIcon
)

################################################################################
class Demo(QTabWidget):
    def __init__(self) -> None:
        super().__init__()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, 'Basice Info')
        self.addTab(self.tab2, 'Contact Info')
        self.addTab(self.tab3, QIcon('../images/new.ico'), 'More Info')

        self.currentChanged.connect(lambda: print(self.currentIndex()))

        self.tab1_init()
        self.tab2_init()

    def tab1_init(self):
        print('tab1_init')
        
        name_label = QLabel('Name:')
        name_line = QLineEdit()

        gender_label = QLabel('Gender:', self.tab1)
        gender_combox = QComboBox()

        bd_label = QLabel('Birth Date')
        bd_dateedit = QDateEdit()

        grid_layout = QGridLayout()
        self.tab1.setLayout(grid_layout)

        grid_layout.addWidget(name_label, 0, 0, 1, 1)
        grid_layout.addWidget(name_line, 0, 1, 1, 1)
        grid_layout.addWidget(gender_label, 1, 0, 1, 1)
        grid_layout.addWidget(gender_combox, 1, 1, 1, 1)
        grid_layout.addWidget(bd_label, 3, 0, 1, 1)
        grid_layout.addWidget(bd_dateedit, 3, 1, 1, 1)

    def tab2_init(self):
        print('tab2_init')



################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

