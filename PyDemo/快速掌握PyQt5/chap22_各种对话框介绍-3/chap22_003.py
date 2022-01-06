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

        self.textedit = QTextEdit(self)
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

    def save_func(self):
        print('save_func')

    def open_func(self):
        print('open_func')
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', "All Files (*);; Text Files (*.txt *.log)")
        print(file)
        if file:
            with open(file, 'r', encoding='utf-8') as f:
                self.textedit.clear()
                self.textedit.setText(f.read())

    def closeEvent(self, QCloseEvent) -> None:
        choice = QMessageBox.question(self, '', 'Do you want to save the text', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        
        if choice == QMessageBox.Yes:
            print('Yes')
        elif choice == QMessageBox.No:
            print('No')
        else:
            print('Cancel')

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
