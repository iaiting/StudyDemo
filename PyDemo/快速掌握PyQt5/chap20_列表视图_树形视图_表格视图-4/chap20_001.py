#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 20.1 列表视图QListView
#
################################################################################
import sys
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import (
    QAbstractItemView, QApplication, QHBoxLayout, QLabel, QListView, QWidget
)

################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()

        self.item_list = ['item {}'.format(i) for i in range(11) ]
        self.model_1 = QStringListModel()
        self.model_1.setStringList(self.item_list)


        self.listview_1 = QListView()
        self.listview_1.setModel(self.model_1)
        self.listview_1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listview_1.doubleClicked.connect(lambda: self.change_func(self.listview_1))

        self.listview_2 = QListView()
        self.model_2 = QStringListModel()
        self.listview_2.setModel(self.model_2)
        self.listview_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listview_2.doubleClicked.connect(lambda: self.change_func(self.listview_2))
    
        self.h_layout = QHBoxLayout()
        self.setLayout(self.h_layout)
        self.h_layout.addWidget(self.listview_1)
        self.h_layout.addWidget(QLabel('图片'))
        self.h_layout.addWidget(self.listview_2)

    def change_func(self, listview):
        print('change_func')
        if listview == self.listview_1:
            print(1)
            self.model_2.insertRows(self.model_2.rowCount(), 1)
            data = self.listview_1.currentIndex().data()
            print(data)
            index = self.model_2.index(self.model_2.rowCount() -1)
            print(index)
            self.model_2.setData(index, data)
        else:
            self.model_2.removeRows(self.listview_2.currentIndex().row(), 1)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
