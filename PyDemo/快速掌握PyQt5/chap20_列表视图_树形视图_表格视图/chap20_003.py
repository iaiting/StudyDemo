#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 20.3 表格视图QTableView
#
################################################################################
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from PyQt5.QtWidgets import (
    QApplication, QWidget, QTableView,
    QVBoxLayout, QLabel, QAbstractItemView,
)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(650, 300)

        self.model = QStandardItemModel(6, 6, self)

        for row in range(6):
            for column in range(6):
                item = QStandardItem('({}, {})'.format(row, column))
                self.model.setItem(row, column, item)

        self.item_list = [QStandardItem('(6, {})'.format(column)) for column in range(6)]
        self.model.appendRow(self.item_list)

        self.item_list = [QStandardItem('(7, {})'.format(column)) for column in range(6)]
        self.model.insertRow(7, self.item_list)

        self.table = QTableView(self)
        self.table.setModel(self.model)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.clicked.connect(self.show_info)

        self.info_label = QLabel(self)
        self.info_label.setAlignment(Qt.AlignCenter)


        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.table)
        self.v_layout.addWidget(self.info_label)
        self.setLayout(self.v_layout)

    def show_info(self):
        print('show_info')
        row = self.table.currentIndex().row()
        column = self.table.currentIndex().column()
        print('({}, {})'.format(row, column))
        data = self.table.currentIndex().data()
        self.info_label.setText(data)


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
