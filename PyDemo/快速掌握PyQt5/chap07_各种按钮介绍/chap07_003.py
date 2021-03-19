#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 7.3 QRadioButton
#
################################################################################
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QRadioButton, QLabel,
    QHBoxLayout, QVBoxLayout
)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.off_button = QRadioButton('off', self)
        self.on_button = QRadioButton('on', self)

        self.pic_label = QLabel(self)

        self.pic_h_layout = QHBoxLayout()
        self.button_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.layout_init()
        self.radiobutton_init()
        self.label_init()

    def layout_init(self):
        self.setLayout(self.all_v_layout)
        self.all_v_layout.addLayout(self.pic_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)

        self.pic_h_layout.addStretch(2)
        self.pic_h_layout.addWidget(self.pic_label)
        self.pic_h_layout.addStretch(2)

        self.button_h_layout.addWidget(self.off_button)
        self.button_h_layout.addWidget(self.on_button)

    def label_init(self):
        self.pic_label.setPixmap(QPixmap('images/close.ico'))

    def radiobutton_init(self):
        self.off_button.setChecked(True)
        self.off_button.toggled.connect(self.on_off_bulb_func)
        pass

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

