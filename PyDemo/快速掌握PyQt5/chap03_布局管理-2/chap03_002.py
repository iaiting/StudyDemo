#!/usr/bin/env python3
# -*- coding: utf-8 -*

################################################################################
#
# 3.2 水平布局QHBoxLayout
#
################################################################################
import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout,
    QLabel, QLineEdit
)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.h_layout = QHBoxLayout()
        self.setLayout(self.h_layout)

        self.user_label = QLabel("Username:", self)
        self.user_line = QLineEdit(self)

        self.h_layout.addWidget(self.user_label)
        self.h_layout.addWidget(self.user_line)


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
    