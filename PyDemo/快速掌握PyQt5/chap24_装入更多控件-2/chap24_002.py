#!/usr/bin/env python3
# -*- codin: utf-8 -*-

################################################################################
#
# 24.2 标签页窗口QTabWidget
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QLabel, QTabWidget, QWidget, 
    QTextEdit, QLineEdit, QComboBox, 
    QGridLayout,
)

from PyQt5.QtGui import QIcon

################################################################################
class Demo(QTabWidget):
    def __init__(self):
        super().__init__()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QTextEdit()

        self.addTab(self.tab1, '111')
        self.addTab(self.tab2, '222')
        self.addTab(self.tab3, QIcon('../images/close.ico'), '333')

        self.tab1_init()

    def tab1_init(self):
        name_label = QLabel('Name:', self.tab1)
        name_line = QLineEdit(self.tab1)

        gender_label = QLabel('Gender:', self.tab1)
        items = ['Please choose your gender', 'Female', 'Male']
        gender_combo = QComboBox(self.tab1)
        gender_combo.addItems(items)

        bd_label = QLabel('Birth Date:', self.tab1)
        bd_dateedit = QTextEdit(self)

        g_layout = QGridLayout()
        self.tab1.setLayout(g_layout)
        
        g_layout.addWidget(name_label, 0, 0, 1, 1)
        g_layout.addWidget(name_line, 0, 1, 1, 1)

        g_layout.addWidget(gender_label, 1, 0, 1, 1)
        g_layout.addWidget(gender_combo, 1, 1, 1, 1)

        g_layout.addWidget(bd_label, 2, 0, 1, 1)
        g_layout.addWidget(bd_dateedit, 2, 1, 1, 1)

    def tab2_init(self):
        pass


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())