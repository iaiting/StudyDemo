#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
#
# 17.1 窗口关闭事件
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMessageBox, QTextEdit,
    QPushButton, QVBoxLayout
)

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        self.is_saved = True

        self.textedit = QTextEdit(self)
        self.textedit.textChanged.connect(self.on_textchanged_func)

        self.button = QPushButton('Save', self)
        self.button.clicked.connect(self.on_clicked_func)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.textedit)
        self.v_layout.addWidget(self.button)

        self.setLayout(self.v_layout)

    def on_textchanged_func(self):
        print('on_textchanged_func')
        self.is_saved = False

    def on_clicked_func(self):
        print("on_clicked_func")
        self.save_func(self.textedit.toPlainText())
        self.is_saved = True

    def save_func(self, text):
        with open('saved.txt', 'w') as f:
            f.write(text)

    def closeEvent(self, QCloseEvent):
        if not self.is_saved:
            print('未保存')
            choice = QMessageBox.question(self, '', 'Do you want to save the text?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if choice == QMessageBox.Yes:
                print("y")
                self.save_func(self.textedit.toPlainText())
                QCloseEvent.accept()
            elif choice == QMessageBox.No:
                print("N")
                QCloseEvent.accept()
            else:
                print("cancel")
                QCloseEvent.ignore()


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())