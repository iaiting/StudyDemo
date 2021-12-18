#!/usr/bin/env python3
# -*- coding: utf- -*-

################################################################################
#
# 7.3 QRadioButton
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QHBoxLayout, QLabel, QRadioButton, QVBoxLayout, QWidget,
)

from PyQt5.QtGui import (
    QPixmap
)

################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()

        self.pic_label = QLabel(self)

        self.off_button = QRadioButton('off', self)
        self.on_button = QRadioButton('on', self)

        self.pic_h_layout = QHBoxLayout()
        self.button_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.layout_init()
        self.radiobutton_init()
        self.label_init()

    def layout_init(self):
        self.all_v_layout.addLayout(self.pic_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)
        self.setLayout(self.all_v_layout)

        self.pic_h_layout.addStretch(1)
        self.pic_h_layout.addWidget(self.pic_label)
        self.pic_h_layout.addStretch(1)

        self.button_h_layout.addWidget(self.off_button)
        self.button_h_layout.addWidget(self.on_button)

    def radiobutton_init(self):
        self.off_button.setChecked(True)
        self.off_button.toggled.connect(self.on_off_bulb_func)

    def label_init(self):
        self.pic_label.setPixmap(QPixmap('./images/close.ico'))

    def on_off_bulb_func(self):
        if self.off_button.isChecked():
            self.pic_label.setPixmap(QPixmap('images/close.ico'))
        else:
            self.pic_label.setPixmap(QPixmap('images/doc.ico'))

################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
