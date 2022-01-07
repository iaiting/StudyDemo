#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
#
################################################################################
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QAction, QMainWindow, QTextEdit, QWidget, QApplication
)

################################################################################
class Demo(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.resize(450, 600)

        self.file_menu = self.menuBar().addMenu('File')
        self.edit_menu = self.menuBar().addMenu('Edit')
        self.help_menu = self.menuBar().addMenu('Help')

        self.file_toolbar = self.addToolBar('File')
        self.edit_toolbar = self.addToolBar('Edit')

        self.status_bar = self.statusBar()

        self.new_action = QAction('New', self)
        self.open_action = QAction('Open', self)
        self.save_action = QAction('Save', self)
        self.save_as_action = QAction('Save As', self)
        self.close_action = QAction('Close', self)
        self.cut_action = QAction('Cut', self)
        self.copy_action = QAction('Copy', self)
        self.paste_action = QAction('Paste', self)
        self.font_action = QAction('Font', self)
        self.color_action = QAction('Color', self)
        self.about_action = QAction('Qt', self)

        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        
        self.menu_init()
        self.toolbar_init()
        self.status_bar_init()
        self.action_init()

    def menu_init(self):
        self.file_menu.addAction(self.new_action)
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.save_as_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.close_action)

        self.edit_menu.addAction(self.cut_action)
        self.edit_menu.addAction(self.copy_action)
        self.edit_menu.addAction(self.paste_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.font_action)
        self.edit_menu.addAction(self.color_action)

        self.help_menu.addAction(self.about_action)

    def toolbar_init(self):
        self.file_toolbar.addAction(self.new_action)
        self.file_toolbar.addAction(self.open_action)
        self.file_toolbar.addAction(self.save_action)
        self.file_toolbar.addAction(self.save_as_action)

        self.edit_toolbar.addAction(self.cut_action)
        self.edit_toolbar.addAction(self.copy_action)
        self.edit_toolbar.addAction(self.paste_action)
        self.edit_toolbar.addAction(self.font_action)
        self.edit_toolbar.addAction(self.color_action)

    def status_bar_init(self):
        self.status_bar.showMessage('Ready to compose')

    def action_init(self):
        # self.new_action.setIcon(QIcon('../images/new.ico'))
        self.new_action.setShortcut('Ctrl+N')
        self.new_action.setToolTip('Create a new file')
        self.new_action.setStatusTip('Create a new file')
        self.new_action.triggered.connect(self.new_func)


    def new_func(self):
        print('new_func')
################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
