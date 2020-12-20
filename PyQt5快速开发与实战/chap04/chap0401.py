#!/usr/bin/env python3
# -*- coding:utf-8 -*-


################################################################################
#
# 案例 4-1 创建主窗口
#
################################################################################
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


################################################################################
class MainWidow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWidow, self).__init__(parent)
        self.resize(400, 200)
        self.status = self.statusBar()
        self.status.showMessage("这是状态栏提示", 5000)
        self.setWindowTitle("PyQt MainWidows例子")


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/cartoon1.ico"))
    form = MainWidow()
    form.show()
    sys.exit(app.exec_())
