#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 4.2 与消息框交互
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QMessageBox
)

################################################################################
class Demo(QWidget):
    pass
    def __init__(self):
        super().__init__()
        self.button = QPushButton('Click Me!', self)
        self.button.clicked.connect(self.show_messagebox)


    def show_messagebox(self):
        choice = QMessageBox.question(self, 'Change Text?', 'Would you like to change the button text?', QMessageBox.Yes|QMessageBox.No)
        if choice == QMessageBox.Yes:
            self.button.setText('Changed!')
        else:
            pass

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
