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
        self.button2.setProperty('name', 'btn')

        self.lineedit1 = QLineEdit()
        self.lineedit2 = SubLineEdit()

        self.combox = QComboBox()
        my_list = ['A', 'B', 'C', 'D']
        self.combox.addItems(my_list)
        self.combox.setObjectName('cb')

        self.gb = QGroupBox()
        self.label1 = QLabel('label1')
        self.label2 = QLabel('label2')
        self.stack = QStackedWidget()
        self.stack.addWidget(self.label2)

        self.gb_layout = QVBoxLayout()
        self.gb_layout.addWidget(self.label1)
        self.gb_layout.addWidget(self.stack)
        self.gb.setLayout(self.gb_layout)

        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)

        self.v_layout.addWidget(self.button1)
        self.v_layout.addWidget(self.button2)
        self.v_layout.addWidget(self.lineedit1)
        self.v_layout.addWidget(self.lineedit2)
        self.v_layout.addWidget(self.combox)
        self.v_layout.addWidget(self.gb)


class SubLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText('indirect')

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    qss = '''
        * {color: red}
        QPushButton {background-color: blue}
        QPushButton[name='btn'] {background-color: green}
        .QLineEdit {font: bold 20px}
        QComboBox#cb {color: blue}
        QGroupBox QLabel {color: blue}
        QGroupBox > QLabel {font: 30px}
    '''
    demo.setStyleSheet(qss)
    demo.show()
    sys.exit(app.exec_())
