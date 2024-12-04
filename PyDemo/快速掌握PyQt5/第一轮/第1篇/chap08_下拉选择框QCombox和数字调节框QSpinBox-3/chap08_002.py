#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 8.2 QSpinBox
#
################################################################################

import sys
from PyQt5.QtWidgets import (
    QApplication, QDoubleSpinBox, QHBoxLayout, QWidget, QSpinBox
)

################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.spinbox = QSpinBox(self)
        self.spinbox.setRange(-99, 99)
        self.spinbox.setSingleStep(1)
        self.spinbox.setValue(-10)
        self.spinbox.valueChanged.connect(self.value_change_func)

        self.double_spinbox = QDoubleSpinBox(self)
        self.double_spinbox.setRange(-99.99, 99.99)
        self.double_spinbox.setSingleStep(0.01)
        self.double_spinbox.setValue(66.66)

        self.all_h_layout = QHBoxLayout()
        self.setLayout(self.all_h_layout)

        self.layout_init()

    def layout_init(self):
        self.all_h_layout.addWidget(self.spinbox)
        self.all_h_layout.addWidget(self.double_spinbox)

    def value_change_func(self):
        decimal_part = self.double_spinbox.value() - int(self.double_spinbox.value())
        self.double_spinbox.setValue(self.spinbox.value() + decimal_part)


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())