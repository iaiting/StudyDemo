#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 24.1 拆分窗口QSplitter
#
################################################################################
import sys

from PyQt5.QtWidgets import (
    QDirModel, QListView, QTabBar, QTableView, QTreeView, QWidget, QApplication, QSplitter
)

################################################################################
class Demo(QSplitter):
    def __init__(self):
        super().__init__()
        
        self.dir_model = QDirModel(self)

        self.list_view = QListView()
        self.tree_view = QTreeView()
        self.table_view = QTableView()


        self.list_view.setModel(self.dir_model)
        self.tree_view.setModel(self.dir_model)
        self.table_view.setModel(self.dir_model)

        self.addWidget(self.list_view)
        self.addWidget(self.tree_view)
        self.addWidget(self.table_view)


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())