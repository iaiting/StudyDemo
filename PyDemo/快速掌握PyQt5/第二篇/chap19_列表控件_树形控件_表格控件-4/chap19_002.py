#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 19.2 树形控件QTreeWidget
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QHBoxLayout, QTreeWidget, QTreeWidgetItem, QWidget,
)

################################################################################
class Demo(QWidget):
    pass
    def __init__(self):
        super().__init__()

        self.resize(500, 300)

        self.tree = QTreeWidget(self)
        self.preview = QTreeWidgetItem(self.tree)

        self.qt5112 = QTreeWidgetItem()
        self.qt5112.setText(0, 'Qt 5.11.2 snapshot')
        self.preview.addChild(self.qt5112)

        choice_list = ['macOS', 'Android x86', 'Android ARMv7']
        for i, c in enumerate(choice_list):
            print(i, c)
            item = QTreeWidgetItem(self.qt5112)
            item.setText(0, c)

        self.test_item = QTreeWidgetItem(self.qt5112)
        self.test_item.setText(0, 'test1')
        self.test_item.setText(1, 'test2')

        self.tree.expandAll()

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.tree)

        self.setLayout(self.h_layout)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())