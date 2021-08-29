#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 8.1 QComboBox
#
################################################################################
import sys

from  PyQt5.QtWidgets import (
    QApplication, QComboBox, QFontComboBox, QLineEdit, QMessageBox, QWidget,
    QComboBox,
    QVBoxLayout,
)
from PyQt5.QtGui import QFont


################################################################################
class Demo(QWidget):
    choice = 'a'
    choice_list = ['b', 'c', 'd']

    def __init__(self):
        super().__init__()
        self.combobox_1 = QComboBox()
        self.combobox_2 = QFontComboBox()
        self.lineedit = QLineEdit()

        self.layout = QVBoxLayout()
        self.layout_init()
        self.combobox_init()

    def layout_init(self):
        self.layout.addWidget(self.combobox_1)
        self.layout.addWidget(self.combobox_2)
        self.layout.addWidget(self.lineedit)
        self.setLayout(self.layout)

    def combobox_init(self):
        self.combobox_1.addItem(self.choice)
        self.combobox_1.addItems(self.choice_list)

        self.combobox_1.currentIndexChanged.connect(lambda: self.on_combobox_func(self.combobox_1))
        self.combobox_2.currentFontChanged.connect(lambda: self.on_combobox_func(self.combobox_2))

    def on_combobox_func(self, combobox):
        if self.combobox_1 == combobox:
            QMessageBox.information(self, 'ComboBox 1', '{}: {}'.format(combobox.currentIndex(), combobox.currentText()))
        else:
            font_text = combobox.currentFont()
            self.lineedit.setFont(QFont(font_text))


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
