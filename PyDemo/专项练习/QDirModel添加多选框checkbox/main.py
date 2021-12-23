#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
#
#
################################################################################
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

################################################################################
#
# 重载QDirModel类，使其增加个checkbox
#
################################################################################
class CheckableDirModel(QDirModel):
    pass
    print(11111111)
    def __init__(self, parent=None):
        print("************************t101:")
        super().__init__(parent)


    def flags(self, index):
        print("************************t102:")
        return super().flags(index)
    # def flags(self, index):
    #     return super().flags(index)

    # def data(self, index, role):
    #     return super().data(index, role=role)

    # def setData(self, index, value, role):
    #     return super().setData(index, value, role=role)

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.dir_model = CheckableDirModel()
        self.tree_view = QTreeView()
        self.all_v_layout = QVBoxLayout()

        self.ui_init()

    def ui_init(self):
        self.layout_init()
        self.tree_view_init()

    def layout_init(self):
        self.setLayout(self.all_v_layout)
        self.all_v_layout.addWidget(self.tree_view)

    def tree_view_init(self):
        self.tree_view.setModel(self.dir_model)
        self.tree_view.setColumnWidth(0, 320)
        # 隐藏文件类型
        self.tree_view.setColumnHidden(2, True)


def main():
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

################################################################################
if __name__ == '__main__':
    main()
