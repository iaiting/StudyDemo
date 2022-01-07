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

        self.open_action.setShortcut('Ctrl+O')
        self.open_action.setToolTip('Open an existing file')
        self.open_action.setStatusTip('Open an existing file')
        self.open_action.triggered.connect(self.open_file_func)

        self.save_action.setShortcut('Ctrl+s')
        self.save_action.triggered.connect(self.save_func)

        self.save_as_action.setShortcut('Ctrl+A')
        self.save_as_action.triggered.connect(self.save_as_func)

        self.close_action.triggered.connect(self.close_func)

        self.cut_action.triggered.connect(self.cut_func)

        self.copy_action.triggered.connect(self.copy_func)

        self.paste_action.triggered.connect(self.paste_func)

        self.font_action.triggered.connect(self.font_func)

        self.color_action.triggered.connect(self.color_func)

    def new_func(self):
        print('new_func')

    def open_file_func(self):
        print('open_file_func')

    def save_func(self):
        print('save_func')

    def save_as_func(self):
        print('save_as_func')

    def close_func(self):
        print('close_func')

    def cut_func(self):
        print('cut_func')

    def copy_func(self):
        print('copy_func')

    def paste_func(self):
        print('paste_func')

    def font_func(self):
        print('font_func')

    def color_func(self):
        print('color_func')

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
