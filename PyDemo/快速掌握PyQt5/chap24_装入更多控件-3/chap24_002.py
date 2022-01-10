#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 24.2 标签页窗口QTabWidget
#
################################################################################

import sys
from PyQt5.QtCore import qWarning
from PyQt5.QtWidgets import (
    QTabWidget, QTableView, QWidget, QApplication
)

################################################################################
class Demo(QTabWidget):
    def __init__(self) -> None:
        super().__init__()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, 'Basice Info')
        self.addTab(self.tab2, 'Contact Info')
        self.addTab(self.tab3, 'More Info')



################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

