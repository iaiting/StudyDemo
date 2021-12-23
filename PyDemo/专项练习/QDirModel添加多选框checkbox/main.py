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
    print('**************t101: Enter CheckableDirModel')
    def __init__(self, parent=None):
        print("************************t101:")
        super().__init__(parent)
        self.checks = {}

    # 如果有QTreeView的clicked事件则不需要重载该函数
    # def flags(self, index):
    #     return super().flags(index) | Qt.ItemIsUserCheckable

    #  -> typing.Any:
    def data(self, index, role):
        if role == Qt.CheckStateRole and index.column() == 0:
            # print('\n\n**************t103: Enter data')
            # print('**************t103.1: index = {}, role = {}'.format(index, role))
            # print('**************t103.2: index.row = {}, index.col = {}, role = {}'.format(index.row(), index.column(), role))
            return self.get_checks(index)

        ret_data = super().data(index, role=role)
        return ret_data

    def setData(self, index, value, role) -> bool:
        if role == Qt.CheckStateRole:
            print('\n\n**************t102: Enter setData')
            print('**************t102.1: index = {}, value = {}, role = {}'.format(index,value, role))
            self.checks[index] = value
            self.recursiveCheck(index, value)
            self.dataChanged.emit(index, index)

        return super().setData(index, value, role=role)


    def recursiveCheck(self, index, value):
        if self.hasChildren(index):
            childrenCount = self.rowCount(index)
            for i in range(childrenCount):
                child = self.index(i, 0, index)
                print('***************x102:index = {}, child = {},value = {}, col = {}'.format(index, child, value, index.column()))
                self.checks[child] = value
                self.dataChanged.emit(child, child)
        else:
            print('该index是不是目录，没有子节点')


    def get_checks(self, index):
        return self.checks.get(index, Qt.Unchecked)



################################################################################
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

        self.tree_view.clicked.connect(self.tree_view_func)

    def tree_view_func(self):
        print('执行: tree_view_func')
        index = self.tree_view.currentIndex()
        if self.dir_model.get_checks(index) == Qt.Unchecked:
            self.dir_model.setData(index, Qt.Checked, Qt.CheckStateRole)
            
            self.get_files(index)
            # if self.dir_model.isDir(index):
            #     pass
            # else:
            #     file_name = self.dir_model.fileName(index)
            #     file_path = self.dir_model.filePath(index)
            #     file_info = 'File Name: {}\nFile Path: {}'.format(file_name, file_path)
            #     print(file_info)
        else:
            self.dir_model.setData(index, Qt.Unchecked, Qt.CheckStateRole)


    def get_files(self, index):
        if self.dir_model.hasChildren(index):
            childrenCount = self.dir_model.rowCount(index)
            for i in range(childrenCount):
                child = self.dir_model.index(i, 0, index)

                if self.dir_model.isDir(child):
                    pass
                else:
                    file_path = self.dir_model.filePath(child)
                    file_info = 'File Path: {}'.format(file_path)
                    print(file_info)
        else:
            file_path = self.dir_model.filePath(index)
            file_info = 'File Path: {}'.format(file_path)
            print(file_info)




    # def setData(self, index, value, role) -> bool:
    #     if role == Qt.CheckStateRole:        

################################################################################
def main():
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

################################################################################
if __name__ == '__main__':
    main()
