#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 8.2 QSpinBox
#
################################################################################
import sys

from  PyQt5.QtWidgets import (
    QApplication,
    QDoubleSpinBox,
    QHBoxLayout,
    QSpinBox,
    QWidget,
)

################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.spinbox = QSpinBox(self)
        self.spinbox.setRange(-99, 99)
        self.spinbox.setSingleStep(2)
        self.spinbox.setValue(88)
        self.spinbox.valueChanged.connect(self.value_change_func)

        self.double_spinbox = QDoubleSpinBox(self)
        self.double_spinbox.setRange(-99.99, 99.99)
        self.double_spinbox.setSingleStep(0.01)
        self.double_spinbox.setValue(66.66)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.spinbox)
        self.h_layout.addWidget(self.double_spinbox)
        self.setLayout(self.h_layout)

    def value_change_func(self):
        decimal_part = self.double_spinbox.value() - int(self.double_spinbox.value())
        self.double_spinbox.setValue(self.spinbox.value() + decimal_part)


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
