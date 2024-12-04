#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
#
################################################################################
import sys
from PyQt5.QtCore import QMimeData
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QAction, QColorDialog, QFileDialog, QFontDialog, QMainWindow, QMessageBox, QTextEdit, QWidget, QApplication
)

################################################################################
class Demo(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.resize(450, 600)
        self.is_saved_first = True
        self.is_saved = True

        self.file_menu = self.menuBar().addMenu('File')
        self.edit_menu = self.menuBar().addMenu('Edit')
        self.help_menu = self.menuBar().addMenu('Help')

        self.file_toolbar = self.addToolBar('File')
        self.edit_toolbar = self.addToolBar('Edit')

        self.status_bar = self.statusBar()
        self.mime_data = QMimeData()
        self.clipboard = QApplication.clipboard()

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
        
        self.text_edit_init()
        self.menu_init()
        self.toolbar_init()
        self.status_bar_init()
        self.action_init()

    def text_edit_init(self):
        self.textedit.textChanged.connect(self.text_changed_func)

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
        self.save_action.setToolTip('Save the file')
        self.save_action.setStatusTip('Save the file')
        self.save_action.triggered.connect(lambda: self.save_func(self.textedit.toHtml()))

        self.save_as_action.setShortcut('Ctrl+A')
        self.save_as_action.setToolTip('Save the file to a specified location')
        self.save_as_action.setStatusTip('Save the file to a specified location')
        self.save_as_action.triggered.connect(lambda: self.save_as_func(self.textedit.toHtml()))

        self.close_action.setShortcut('Ctrl+E')
        self.close_action.setToolTip('Close the window')
        self.close_action.setStatusTip('Close the window')
        self.close_action.triggered.connect(self.close_func)

        self.cut_action.setShortcut('Ctrl+X')
        self.cut_action.setToolTip('Cut the text to clipboard')
        self.cut_action.setStatusTip('Cut the text')
        self.cut_action.triggered.connect(self.cut_func)

        self.copy_action.setShortcut('Ctrl+C')
        self.copy_action.setToolTip('Copy the text')
        self.copy_action.setStatusTip('Copy the text')
        self.copy_action.triggered.connect(self.copy_func)

        self.paste_action.setShortcut('Ctrl+P')
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
        self.about_action.setToolTip('What is Qt?')
        self.about_action.setStatusTip('What is Qt')
        self.about_action.triggered.connect(self.about_func)

    def text_changed_func(self):
        if self.textedit.toPlainText():
            self.is_saved = False
        else:
            self.is_saved = True

    def new_func(self):
        print('new_func')
        if self.is_saved:
            self.textedit.clear()
        else:
            choice = QMessageBox.question(self, '', 'Do you want to save the text?', QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
            if choice == QMessageBox.No:
                self.textedit.clear()
            elif choice == QMessageBox.Yes:
                self.save_func(self.textedit.toHtml())
                if self.is_saved_first == False:
                    self.textedit.clear()
            else:
                pass


    def open_file_func(self):
        print('open_file_func')

        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', 'Files (*.*)')
        if file:
            with open(file, 'r') as f:
                self.textedit.clear()
                self.textedit.setHtml(f.read())

    def save_func(self, text):
        print('save_func')
        if self.is_saved_first:
            self.save_as_func(text)
            
        else:
            with open(self.path, 'w') as f:
                f.write(text)

    def save_as_func(self, text):
        print('save_as_func')
        self.path, _ = QFileDialog.getSaveFileName(self, 'Save File', './', 'Files (*.html *.txt *.log)')
        if self.path:
            with open(self.path, 'w') as f:
                f.write(text)
                self.is_saved_first = False


    def close_func(self):
        print('close_func')
        if not self.is_saved:
            choice = QMessageBox.question(self, 'Save File', 'Do you want to save the text?', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if choice == QMessageBox.Yes:
                self.save_func(self.textedit.toHtml())
                self.close()
            elif choice == QMessageBox.No:
                self.close()
            else:
                pass
        else:
            self.close()

    def cut_func(self):
        print('cut_func')
        self.mime_data.setHtml(self.textedit.textCursor().selection().toHtml())
        self.clipboard.setMimeData(self.mime_data)
        self.textedit.textCursor().removeSelectedText()


    def copy_func(self):
        print('copy_func')
        self.mime_data.setHtml(self.textedit.textCursor().selection().toHtml())
        self.clipboard.setMimeData(self.mime_data)

    def paste_func(self):
        print('paste_func')
        self.textedit.insertHtml(self.clipboard.mimeData().html())

    def font_func(self):
        print('font_func')
        font, ok = QFontDialog.getFont()
        if ok:
            self.textedit.setFont(font)

    def color_func(self):
        print('color_func')
        color = QColorDialog.getColor()
        if color.isValid():
            self.textedit.setTextColor(color)

    def about_func(self):
        print('about_func')
        QMessageBox.aboutQt(self, 'About Qt')


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
