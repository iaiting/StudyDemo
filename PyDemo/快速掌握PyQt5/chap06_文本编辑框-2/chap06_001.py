#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 6.1 同步显示文本
#
################################################################################
import sys

from PyQt5.QtWidgets import (
    QApplication, QHBoxLayout, QLabel, QTextBrowser, QTextEdit, QVBoxLayout, QWidget
)
################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.text_edit_label = QLabel('QTextEdit', self)
        self.text_browser_label = QLabel('QTextBrowser', self)

        self.text_edit = QTextEdit()
        self.text_browser = QTextBrowser()

        self.textedit_v_layout = QVBoxLayout()
        self.textbrowser_v_layout = QVBoxLayout()
        self.all_h_layout = QHBoxLayout()

        self.layout_init()
        self.textedit_init()

    def layout_init(self):
        self.all_h_layout.addLayout(self.textedit_v_layout)
        self.all_h_layout.addLayout(self.textbrowser_v_layout)
        self.setLayout(self.all_h_layout)

        self.textedit_v_layout.addWidget(self.text_edit_label)
        self.textedit_v_layout.addWidget(self.text_edit)

        self.textbrowser_v_layout.addWidget(self.text_browser_label)
        self.textbrowser_v_layout.addWidget(self.text_browser)

    def textedit_init(self):
        self.text_edit.textChanged.connect(self.show_text_func)

    def show_text_func(self):
        self.text_browser.setText(self.text_edit.toPlainText())

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())