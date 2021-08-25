#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 23.1 记事本
#
###############################################################################
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QMimeData
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QAction, QTextEdit,
    QMessageBox, QFontDialog, QColorDialog,
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
        self.save_action = QAction('Save', self)
        self.save_as_action = QAction('Save As', self)
        self.close_action = QAction('Close', self)

        self.cut_action = QAction('Cut', self)
        self.copy_action = QAction('Copy', self)
        self.paste_action = QAction('Paste', self)
        self.font_action = QAction('Font', self)
        self.color_action = QAction('Color', self)

        self.about_action = QAction('Qt', self)

        self.text_edit = QTextEdit(self)
        self.mime_data = QMimeData()
        self.clipboard = QApplication.clipboard()

        self.setCentralWidget(self.text_edit)
        self.resize(450, 600)

        self.menu_init()
        self.toolbar_init()
        self.status_bar_init()
        self.action_init()


    def menu_init(self):
        self.file_menu.addAction(self.new_action)
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.save_as_action)
        self.file_menu.addAction(self.close_action)

        self.edit_menu.addAction(self.cut_action)
        self.edit_menu.addAction(self.copy_action)
        self.edit_menu.addAction(self.paste_action)
        self.edit_menu.addAction(self.font_action)
        self.edit_menu.addAction(self.color_action)

        self.help_menu.addAction(self.about_action)

    def toolbar_init(self):
        self.file_toolbar.addAction(self.new_action)
        self.file_toolbar.addAction(self.open_action)

    def action_init(self):
        self.new_action.setIcon(QIcon('../images/new.ico'))
        self.new_action.setShortcut('Ctrl + N')
        self.new_action.setToolTip('Create a new file')
        self.new_action.setStatusTip('Create a new file2')

        self.open_action.setIcon(QIcon('../images/open.ico'))
        self.open_action.setShortcut('Ctrl + O')
        self.open_action.setToolTip('Open an existing file')
        self.open_action.setStatusTip('Open an existing file')

        self.save_action.setIcon(QIcon('../images/save.ico'))
        self.save_action.setShortcut('Ctrl + S')
        self.save_action.setToolTip('Save the file')
        self.save_action.setStatusTip('Save the file')

        self.save_as_action.setIcon(QIcon('../images/save_as.ico'))
        self.save_as_action.setShortcut('Ctrl + S')
        self.save_as_action.setToolTip('Save the file')
        self.save_as_action.setStatusTip('Save the file')

        self.close_action.setIcon(QIcon('../images/close.ico'))
        self.close_action.setShortcut('Ctrl + S')
        self.close_action.setToolTip('Save the file')
        self.close_action.setStatusTip('Save the file')

        self.cut_action.setIcon(QIcon('../images/cut.ico'))
        self.cut_action.setShortcut('Ctrl+X')
        self.cut_action.setToolTip('Cut the text to clipboard')
        self.cut_action.setStatusTip('Cut the text to clipboard')
        self.cut_action.triggered.connect(self.cut_func)

        self.copy_action.setIcon(QIcon('../images/copy.ico'))
        self.copy_action.setShortcut('Ctrl+C')
        self.copy_action.setToolTip('Copy the text')
        self.copy_action.setStatusTip('Copy the text')
        self.copy_action.triggered.connect(self.copy_func)

        self.paste_action.setIcon(QIcon('../images/paste.ico'))
        self.paste_action.setShortcut('Ctrl+V')
        self.paste_action.setToolTip('Paste the text')
        self.paste_action.setStatusTip('Paste the text')
        self.paste_action.triggered.connect(self.paste_func)

        self.font_action.setIcon(QIcon('../images/font.ico'))
        self.font_action.setShortcut('Ctrl+T')
        self.font_action.setToolTip('Change the font')
        self.font_action.setStatusTip('Change the font')
        self.font_action.triggered.connect(self.font_func)

        self.color_action.setIcon(QIcon('../images/color.ico'))
        self.color_action.setShortcut('Ctrl+R')
        self.color_action.setToolTip('Change the color')
        self.color_action.setStatusTip('Change the color')
        self.color_action.triggered.connect(self.color_func)

        self.about_action.setIcon(QIcon('../images/about.ico'))
        self.about_action.setShortcut('Ctrl+q')
        self.about_action.setToolTip('What is Qt?')
        self.about_action.setStatusTip('What is Qt?')
        self.about_action.triggered.connect(self.about_func)

    def status_bar_init(self):
        self.status_bar.showMessage('Ready to compose')

    def cut_func(self):
        self.mime_data.setHtml(self.text_edit.textCursor().selection().toHtml())
        self.clipboard.setMimeData(self.mime_data)
        self.text_edit.textCursor().removeSelectedText()

    def copy_func(self):
        self.mime_data.setHtml(self.text_edit.textCursor().selection().toHtml())
        self.clipboard.setMimeData(self.mime_data)

    def paste_func(self):
        self.text_edit.insertHtml(self.clipboard.mimeData().html())

    def font_func(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text_edit.setFont(font)

    def color_func(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_edit.setTextColor(color)

    def about_func(self):
        QMessageBox.aboutQt(self, 'About Qt')


#############################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
