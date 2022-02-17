#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 4.1 各种类型的消息框
#
################################################################################
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton('information', self)
        self.button.clicked.connect(self.show_messagebox)

    def show_messagebox(self):
        QMessageBox.information(self, 'Title', 'Content', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())