#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 22.3 文件对话框
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QPushButton, QMessageBox,
    QHBoxLayout, QVBoxLayout, QFontDialog, QFileDialog,
)

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        self.is_saved = True
        self.is_save_first = True
        self.path = ''


        self.textedit = QTextEdit(self)
        self.textedit.textChanged.connect(self.on_textchanged_func)

        self.button = QPushButton('Save', self)
        self.button.clicked.connect(self.on_clicked_func)

        self.button_2 = QPushButton('Open', self)
        self.button_2.clicked.connect(self.open_file_func)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.button)
        self.h_layout.addWidget(self.button_2)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.textedit)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def on_textchanged_func(self):
        print("on_textchanged_func")
        if self.textedit.toPlainText():
            self.is_saved = False
        else:
            self.is_saved = True

    def on_clicked_func(self):
        print("on_clicked_func")
        if self.is_save_first:
            self.save_as_func(self.textedit.toPlainText())
        else:
            self.save_func(self.textedit.toPlainText())

    def save_func(self, text):
        print("save_func")
        with open(self.path, 'w') as f:
            f.write(text)
        self.is_saved = True

    def save_as_func(self, text):
        print('save_as_func')
        self.path, _ = QFileDialog.getSaveFileName(self, 'Save File', './', 'Files (*.txt *.log)')
        if self.path:
            self.save_func(text)
            self.is_save_first = False

    def open_file_func(self):
        print("open_file_func")
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', 'Files (*.txt *.log *.py)')
        if file:
            with open(file, 'r') as f:
                self.textedit.clear()
                self.textedit.setText(f.read())

    def closeEvent(self, QCloseEvent):
        print("closeEvent")
        if not self.is_saved:
            print('请保存')
            choice = QMessageBox.question(self, '', 'Do you want to save the text?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

            if choice == QMessageBox.Yes:
                self.on_clicked_func()
                QCloseEvent.accept()
            elif choice == QMessageBox.No:
                QCloseEvent.accept()
            else:
                QCloseEvent.ignore()


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
