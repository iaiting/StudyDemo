#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 文件对话框
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget
)


################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.is_saved = True
        self.is_saved_first = True
        self.path = ''

        self.textedit = QTextEdit(self)

        self.save_btn = QPushButton('Save', self)
        self.open_btn = QPushButton('Open', self)

        self.textedit.textChanged.connect(self.on_textchanged_func)
        self.save_btn.clicked.connect(self.save_file_func)
        self.open_btn.clicked.connect(self.open_file_func)

        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        
        self.h_layout.addWidget(self.save_btn)
        self.h_layout.addWidget(self.open_btn)

        self.v_layout.addWidget(self.textedit)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def on_textchanged_func(self):
        print('on_textchanged_func')
        if self.textedit.toPlainText():
            self.is_saved = False
        else:
            self.is_saved = True

    def save_file_func(self):
        print("save_file_func")
        if self.is_saved_first:
            self.save_as_func(self.textedit.toPlainText())
        else:
            self.save_func(self.textedit.toPlainText())

    def save_func(self, text):
        with open(self.path, 'w') as f:
            f.write(text)

        self.is_saved = True

    def save_as_func(self, text):
        self.path, _ = QFileDialog.getSaveFileName(self, 'Save File', './', 'Files (*.txt *.log)')
        print(self.path)
        if self.path:
            with open(self.path, 'w') as f:
                print(text)
                f.write(text)

            self.is_saved = True
            self.is_saved_first = False

    def open_file_func(self):
        print('open_file_func')
        file, _ =  QFileDialog.getOpenFileName(self, 'Open File', './', 'Files (*.txt *.md *.py)')
        print(file)
        if file:
            with open(file, 'r') as f:
                self.textedit.clear()
                self.textedit.setText(f.read())

    def closeEvent(self, QCloseEvent) -> None:
        if not self.is_saved:
            choice = QMessageBox.question(self, '', 'Do you want to save the text?', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if choice == QMessageBox.Yes:
                self.save_file_func()
                QCloseEvent.accept()
            elif choice == QMessageBox.No:
                QCloseEvent.accept()
            else:
                QCloseEvent.ignore()


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
