#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 24.1 拆分窗口QSplitter
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QDirModel, QListView, QTableView, QTreeView, QWidget, QSplitter
)

################################################################################
class Demo(QSplitter):
    def __init__(self):
        super().__init__()
        self.dir_model = QDirModel(self)

        self.list_view = QListView()
        self.list_view.setModel(self.dir_model)

        self.tree_view = QTreeView()
        self.tree_view.setModel(self.dir_model)
        self.tree_view.doubleClicked.connect(self.show_func)

        self.tabel_view = QTableView()
        self.tabel_view.setModel(self.dir_model)

        self.addWidget(self.list_view)
        self.addWidget(self.tree_view)

        self.insertWidget(0, self.tabel_view)
        self.setSizes([300, 200, 800])

    def show_func(self, index):
        print(index)
        self.list_view.setRootIndex(index)
        self.tabel_view.setRootIndex(index)


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
