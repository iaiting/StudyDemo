#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 24.1 拆分窗口QSplitter
#
################################################################################
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QSplitter, QListView, QTreeView, QTableView,
    QDirModel
)


################################################################################
class Demo(QSplitter):
    def __init__(self):
        super(Demo, self).__init__()
        self.dir_model = QDirModel(self)

        self.list_view = QListView(self)
        self.tree_view = QTreeView(self)
        self.table_view = QTableView(self)

        self.list_view.setModel(self.dir_model)
        self.tree_view.setModel(self.dir_model)
        self.table_view.setModel(self.dir_model)

        self.tree_view.doubleClicked.connect(self.show_func)

        self.addWidget(self.list_view)
        self.addWidget(self.tree_view)
        self.insertWidget(0, self.table_view)
        self.setSizes([300, 200, 200])
        print(self.count())

    def show_func(self, index):
        self.list_view.setRootIndex(index)
        self.table_view.setRootIndex(index)


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
