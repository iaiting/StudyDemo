#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 19.1 列表控件QListWidget
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem
)
from PyQt5.QtGui import QPixmap


################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.pic_label = QLabel(self)
        self.pic_label.setPixmap(QPixmap('../images/splash.jpg'))

        self.listwidget_1 = QListWidget(self)
        self.listwidget_2 = QListWidget(self)

        self.listwidget_1.doubleClicked.connect(lambda : self.change_func(self.listwidget_1))
        self.listwidget_2.doubleClicked.connect(lambda: self.change_func(self.listwidget_2))

        for i in range(6):
            text = 'Item {}'.format(i)
            self.item = QListWidgetItem(text)
            self.listwidget_1.addItem(text)

        self.item6 = QListWidgetItem('Item 6', self.listwidget_1)
        self.listwidget_1.addItem('Item 7')

        str_list = ['Item 9', 'Item 10']
        self.listwidget_1.addItems(str_list)

        self.item_8 = QListWidgetItem('Item 8')
        # self.listwidget_1.insertItem(8, self.item_8)
        self.listwidget_1.insertItem(8, 'Item 8')

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.listwidget_1)
        self.h_layout.addWidget(self.pic_label)
        self.h_layout.addWidget(self.listwidget_2)
        self.setLayout(self.h_layout)

    def change_func(self, listwidget):
        if listwidget == self.listwidget_1:
            item = QListWidgetItem(self.listwidget_1.currentItem())
            self.listwidget_2.addItem(item)
            print("listwidget_1")
        else:
            self.listwidget_2.takeItem(self.listwidget_2.currentRow())
            print("listwidget_2")


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
