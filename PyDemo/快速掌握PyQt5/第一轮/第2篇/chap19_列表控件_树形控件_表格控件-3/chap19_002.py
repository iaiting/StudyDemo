#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 19.2 树形控件QTreeWidget
#
################################################################################
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QHBoxLayout, QLabel, QTreeWidget, QTreeWidgetItem, QWidget
)
################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 300)

        self.tree = QTreeWidget(self)
        self.tree.setColumnCount(2)
        self.tree.setColumnWidth(0, 300)
        self.tree.setHeaderLabels(['Install Components', 'Test'])
        self.tree.itemClicked.connect(self.change_func)

        self.preview = QTreeWidgetItem(self.tree)
        self.preview.setText(0, 'Preview')

        self.qt5112 = QTreeWidgetItem()
        self.qt5112.setText(0, 'Qt 5.11.2 snapshot')
        self.qt5112.setCheckState(0, Qt.Unchecked)
        self.preview.addChild(self.qt5112)

        choice_list = ['macOS', 'Android x86', 'Android ARMv7', 'Sources', 'IOS']

        self.item_list = []
        for i, c in enumerate(choice_list):
            item = QTreeWidgetItem(self.qt5112)
            item.setText(0, c)
            item.setCheckState(0, Qt.Unchecked)
            self.item_list.append(item)

        self.test_item = QTreeWidgetItem(self.qt5112)
        self.test_item.setText(0, 'test1')
        self.test_item.setText(1, 'test2')
        self.tree.expandAll()

        self.label = QLabel('No Click')

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.tree)
        self.h_layout.addWidget(self.label)
        self.setLayout(self.h_layout)

    def change_func(self, item, column):
        print(column)
        print(item.text(column))
        self.label.setText(item.text(column))

        if item == self.qt5112:
            if self.qt5112.checkState(0) == Qt.Checked:
                print('全选')
                for x in self.item_list:
                    x.setCheckState(0, Qt.Checked)
            else:
                print('全不选')
                for x in self.item_list:
                    x.setCheckState(0, Qt.Unchecked)
        else:
            check_cout = 0
            for x in self.item_list:
                if x.checkState(0) == Qt.Checked:
                    check_cout += 1
            if check_cout == 5:
                self.qt5112.setCheckState(0, Qt.Checked)
            elif 0 < check_cout < 5:
                self.qt5112.setCheckState(0, Qt.PartiallyChecked)
            else:
                self.qt5112.setCheckState(0, Qt.Unchecked)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
