#!/usr/bin/env python3
# -*- coding -*-

################################################################################
#
# 6.1 同步显示文本
#
################################################################################
import sys
from PyQt5.QtWidgets import ( 
    QApplication,
    QHBoxLayout,
    QLabel,
    QTextBrowser,
    QTextEdit,
    QVBoxLayout,
    QWidget
)

################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()

        self.edit_label = QLabel('QTextEdit')
        self.text_edit = QTextEdit()

        self.browser_label = QLabel('QTextBrowser')
        self.text_browser = QTextBrowser()

        self.h_layout = QHBoxLayout()
        self.v1_layout = QVBoxLayout()
        self.v2_layout = QVBoxLayout()

        self.layout_init()
        self.text_edit_init()

    def layout_init(self):
        self.setLayout(self.h_layout)
        self.h_layout.addLayout(self.v1_layout)
        self.h_layout.addLayout(self.v2_layout)

        self.v1_layout.addWidget(self.edit_label)
        self.v1_layout.addWidget(self.text_edit)

        self.v2_layout.addWidget(self.browser_label)
        self.v2_layout.addWidget(self.text_browser)

    def text_edit_init(self):
        self.text_edit.textChanged.connect(self.show_text_func)

    def show_text_func(self):
        self.text_browser.setText(self.text_edit.toPlainText())

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

