#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 24.3 堆叠窗口QStackedWidget
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QListWidget, 
    QHBoxLayout,
)

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.list_widget = QListWidget()
        self.list_widget.addItem('Basic Info')
        self.list_widget.addItem('Contact Info')
        self.list_widget.addItem('More Info')

        self.h_layout = QHBoxLayout()
        self.setLayout(self.h_layout)
        self.h_layout.addWidget(self.list_widget)



################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
