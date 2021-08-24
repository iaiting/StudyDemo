#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 23.1 记事本
#
###############################################################################
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction


###############################################################################
class Demo(QMainWindow):
    is_saved = True
    is_saved_first = True
    path = ''

    def __init__(self):
        super(Demo, self).__init__()

        self.file_menu = self.menuBar().addMenu('File')
        self.edit_menu = self.menuBar().addMenu('Edit')
        self.help_menu = self.menuBar().addMenu('Help')

        self.file_toolbar = self.addToolBar('File')
        self.edit_toolbar = self.addToolBar('Edit')

        self.status_bar = self.statusBar()

        self.new_action = QAction('New', self)


#############################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
