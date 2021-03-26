#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 19.3 表格控件QTableWidget
#
################################################################################
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTableWidget, QTableWidgetItem
)

################################################################################
class Demo(QTableWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.setRowCount(6)
        self.setColumnCount(6)

        self.setColumnWidth(0, 300)
        self.setRowHeight(0, 300)

        self.setHorizontalHeaderLabels(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        self.setVerticalHeaderLabels(['t1', 't2', 't3', 't4', 't5', 't6'])

        self.item_1 = QTableWidgetItem('Hi')
        self.setItem(0, 0, self.item_1)

        self.item_2 = QTableWidgetItem('Bye')
        self.item_2.setTextAlignment(Qt.AlignCenter)
        self.setItem(2, 2, self.item_2)

        self.setSpan(2, 2, 2, 2)

################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
