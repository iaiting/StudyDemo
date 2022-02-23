#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 28.2 选择器类型
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QLineEdit, QComboBox, QStackedWidget, QGroupBox,
    QVBoxLayout
)


################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.button1 = QPushButton('button1')
        self.button2 = QPushButton('button2')
        

        self.lineedit1 = QLineEdit()
        self.lineedit2 = SubLineEdit()

        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)

        self.v_layout.addWidget(self.button1)
        self.v_layout.addWidget(self.button2)
        self.v_layout.addWidget(self.lineedit1)
        self.v_layout.addWidget(self.lineedit2)


class SubLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText('indirect')

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
