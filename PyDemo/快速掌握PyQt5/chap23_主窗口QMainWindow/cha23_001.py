#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 23.1 记事本
#
###############################################################################
import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QAction, QTextEdit,
)


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
        self.open_action = QAction('Open', self)

        self.text_edit = QTextEdit(self)

        self.setCentralWidget(self.text_edit)
        self.resize(450, 600)

        self.menu_init()
        self.toolbar_init()
        self.status_bar_init()

    def menu_init(self):
        self.file_menu.addAction(self.new_action)
        self.file_menu.addAction(self.open_action)

    def toolbar_init(self):
        self.file_toolbar.addAction(self.new_action)
        self.file_toolbar.addAction(self.open_action)

    def status_bar_init(self):
        self.status_bar.showMessage('Ready to compose')
        pass


#############################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
