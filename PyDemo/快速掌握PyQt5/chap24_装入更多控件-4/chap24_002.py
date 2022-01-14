#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 24.2 标签页窗口QTabWidget
#
################################################################################
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QTabWidget,
    QTextEdit,
    QWidget
)

################################################################################
class Demo(QTabWidget):
    def __init__(self) -> None:
        super().__init__()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QTextEdit()

        self.addTab(self.tab1, 'Baseic Info')
        self.addTab(self.tab2, 'Contact Info')
        self.addTab(self.tab3, 'More Info')

        self.tab1_init()
        self.tab2_init()

    def tab1_init(self):
        name_label = QLabel('Name:', self.tab1)

    def tab2_init(self):
        tel_label = QLabel('Tel:', self.tab2)


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
