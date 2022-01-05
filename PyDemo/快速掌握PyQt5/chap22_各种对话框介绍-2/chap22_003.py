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
    QHBoxLayout,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget
)


################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.textedit = QTextEdit(self)

        self.save_btn = QPushButton('Save', self)
        self.open_btn = QPushButton('Open', self)

        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        
        self.h_layout.addWidget(self.save_btn)
        self.h_layout.addWidget(self.open_btn)

        self.v_layout.addWidget(self.textedit)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
