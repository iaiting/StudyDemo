#!/usr/bin/env python3
# -*- coding: utf-8 -*-


################################################################################
#
# 23.1 记事本应用
#
################################################################################
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QMimeData
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox,
    QFontDialog, QColorDialog,
)


################################################################################
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
        self.toobar_init()
        self.status_bar_init()
        self.action_init()
        self.text_edit_init()

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


    def toobar_init(self):
        self.file_toolbar.addAction(self.new_action)
        self.file_toolbar.addAction(self.open_action)
        self.file_toolbar.addAction(self.save_action)
        self.file_toolbar.addAction(self.save_as_action)

        self.edit_toolbar.addAction(self.cut_action)
        self.edit_toolbar.addAction(self.copy_action)
        self.edit_toolbar.addAction(self.paste_action)
        self.edit_toolbar.addAction(self.font_action)
        self.edit_toolbar.addAction(self.color_action)

        pass

    def status_bar_init(self):
        self.status_bar.showMessage('Ready to compose')
        pass

    def action_init(self):
        self.new_action.setShortcut('Ctrl+N')
        self.new_action.setToolTip('Create a new file')
        self.new_action.setStatusTip('Create a new file')
        self.new_action.triggered.connect(self.new_func)

        self.open_action.setShortcut('Ctrl+O')
        self.open_action.setToolTip('Open an existing file')
        self.open_action.setStatusTip('Open an existing file')
        self.open_action.triggered.connect(self.open_file_func)

        self.save_action.setShortcut('Ctrl+S')
        self.save_action.setToolTip('Save the file')
        self.save_action.setStatusTip('Save the file')
        # self.save_action.triggered.connect()

        self.save_as_action.setShortcut('Ctrl+A')
        self.save_as_action.setToolTip('Save the file to a specified location')
        self.save_as_action.setStatusTip('Save the file to a specified location')

        self.close_action.setShortcut('Ctrl+E')
        self.close_action.setToolTip('Close the window')
        self.close_action.setStatusTip('Close the window')
        self.close_action.triggered.connect(self.close_func)

        self.cut_action.setShortcut('Ctrl+X')
        self.cut_action.setToolTip('Cut the text to clipboard')
        self.cut_action.setStatusTip('Cut the text to clipboard')
        self.cut_action.triggered.connect(self.cut_func)

        self.copy_action.setShortcut('Ctrl+C')
        self.copy_action.setToolTip('Copy the text')
        self.copy_action.setStatusTip('Copy the text')
        self.copy_action.triggered.connect(self.copy_func)

        self.paste_action.setShortcut('Ctrl+V')
        self.paste_action.setToolTip('Paste the text')
        self.paste_action.setStatusTip('Paste the text')
        self.paste_action.triggered.connect(self.paste_func)

        self.font_action.setShortcut('Ctrl+T')
        self.font_action.setToolTip('Change the font')
        self.font_action.setStatusTip('Change the font')
        self.font_action.triggered.connect(self.font_func)


        self.color_action.setShortcut('Ctrl+R')
        self.color_action.setToolTip('Change the color')
        self.color_action.setStatusTip('Change the color')
        self.color_action.triggered.connect(self.color_func)

        self.about_action.setShortcut('Ctrl+Q')
        self.about_action.setToolTip('What is Qt')
        self.about_action.setStatusTip('What is Qt')
        self.about_action.triggered.connect(self.about_func)


    def text_edit_init(self):
        self.text_edit.textChanged.connect(self.text_changed_func)

    def text_changed_func(self):
        print("text_changed_func")
        if self.text_edit.toPlainText():
            self.is_saved = False
        else:
            self.is_saved = True

    def new_func(self):
        print("new_func")
        if not self.is_saved and self.text_edit.toPlainText():
            choice = QMessageBox.question(self, '', 'Do you want to save the text?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if choice == QMessageBox.Yes:
                self.save_func(self.text_edit.toHtml())
                self.text_edit.clear()
                self.is_saved_first = True
            elif choice == QMessageBox.No:
                self.text_edit.clear()
            else:
                pass

        else:
            self.text_edit.clear()
            self.is_saved = False
            self.is_saved_first = True

    def open_file_func(self):
        print("open_file_func")

    def save_func(self, text):
        if self.is_saved_first:
            self.save_as_func(text)
        else:
            with open(self.path, 'w') as f:
                f.write(text)
            self.is_saved = True

    def save_as_func(self, text):
        self.path, _ = QFileDialog.getSaveFileName(self, 'Save File', './', 'Files (*.html *.txt *.log)')
        if self.path:
            with open(self.path, 'w') as f:
                f.write(text)

            self.is_saved = True
            self.is_saved_first = False


    def close_func(self):
        if not self.is_saved:
            choice = QMessageBox.question(self, 'Save File', 'Do you want to save the text?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if choice == QMessageBox.Yes:
                self.save_func(self.text_edit.toHtml())
                self.close()
            elif choice == QMessageBox.No:
                self.close()
            else:
                pass

    def closeEvent(self, QCloseEvent):
        if not self.is_saved:
            choice = QMessageBox.question(self, 'Save File', 'Do you want to save the text?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if choice == QMessageBox.Yes:
                self.save_func(self.text_edit.toHtml())
                QCloseEvent.accept()
            elif choice == QMessageBox.No:
                QCloseEvent.accept()
            else:
                QCloseEvent.ignore()

    def cut_func(self):
        print("cut_func")
        self.mime_data.setHtml(self.text_edit.textCursor().selection().toHtml())
        self.clipboard.setMimeData(self.mime_data)
        self.text_edit.textCursor().removeSelectedText()

    def copy_func(self):
        print("copy func")
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
        print("about_func")
        QMessageBox.aboutQt(self, 'About Qt')

################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
