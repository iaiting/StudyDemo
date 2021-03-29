#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 20.2 树形视图QTreeView
#
################################################################################
import sys
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTreeWidget, QDirModel, QLabel, QVBoxLayout,
    QTreeView,
)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 300)
        self.modle = QDirModel(self)
        self.modle.setReadOnly(False)
        self.modle.setSorting(QDir.Name | QDir.IgnoreCase)

        self.tree = QTreeView(self)
        self.tree.setModel(self.modle)
        self.tree.clicked.connect(self.show_info)
        self.index = self.modle.index(QDir.currentPath())
        self.tree.expand(self.index)
        self.tree.scrollTo(self.index)

        self.info_label = QLabel(self)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.tree)
        self.v_layout.addWidget(self.info_label)
        self.setLayout(self.v_layout)

    def show_info(self):
        print('show info')
        index = self.tree.currentIndex()
        file_name = self.modle.fileName(index)
        file_path = self.modle.filePath(index)
        file_info = 'File Name: {}\nFile Path: {}'.format(file_name, file_path)
        self.info_label.setText(file_info)


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
