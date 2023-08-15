#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 22.3 文件对话框
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QFileDialog, QHBoxLayout, QMessageBox, QPushButton, QTextEdit, QVBoxLayout, QWidget, QApplication
)

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.is_saved_first = True
        self.is_saved = True

        self.textedit = QTextEdit(self)
        self.textedit.textChanged.connect(self.on_textchanged_text_func)

        self.save_btn = QPushButton('Save', self)
        self.save_btn.clicked.connect(self.save_func)
    
        self.open_btn = QPushButton('Open', self)
        self.open_btn.clicked.connect(self.open_func)

        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()

        self.v_layout.addWidget(self.textedit)
        self.h_layout.addWidget(self.save_btn)
        self.h_layout.addWidget(self.open_btn)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def on_textchanged_text_func(self):
        print('on_textchanged_text_func')
        if self.textedit.toPlainText():
            self.is_saved = False
        else:
            self.is_saved = True


    def save_file(self, text):
        with open(self.path, 'w') as f:
            f.write(text)
            self.is_saved = True

    def save_func(self):
        print('save_func')
        text = self.textedit.toPlainText()
        
        if self.is_saved_first:
            self.path, _ = QFileDialog.getSaveFileName(self, 'Save File', './', 'Files (*.txt *.log)')
            if self.path:
                self.save_file(text)
                self.is_saved_first = False
        else:
            self.save_file(text)

    def open_func(self):
        print('open_func')
        import os
        # file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', "All Files (*);; Text Files (*.txt *.log)")
        file, _ = QFileDialog.getExistingDirectory(None, 'aaa', os.getcwd())#选择文件目录

        print(file)
        if file:
            with open(file, 'r', encoding='utf-8') as f:
                self.textedit.clear()
                self.textedit.setText(f.read())

    def closeEvent(self, QCloseEvent) -> None:

        if not self.is_saved:
            choice = QMessageBox.question(self, '', 'Do you want to save the text', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            
            if choice == QMessageBox.Yes:
                print('Yes')
                self.save_func()
                QCloseEvent.accept()
            elif choice == QMessageBox.No:
                print('No')
                QCloseEvent.accept()
            else:
                print('Cancel')
                QCloseEvent.ignore()

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
