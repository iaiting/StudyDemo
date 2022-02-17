#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 7.4 QCheckBox
#
################################################################################
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QVBoxLayout,
    QWidget
)

################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()

        self.checkbox1 = QCheckBox('checkbox 1', self)
        self.checkbox2 = QCheckBox('checkbox 2', self)
        self.checkbox3 = QCheckBox('checkbox 3', self)

        self.all_v_layout = QVBoxLayout()
        self.layout_init()
        self.checkbox_init()

    def layout_init(self):
        self.setLayout(self.all_v_layout)

        self.all_v_layout.addWidget(self.checkbox1)
        self.all_v_layout.addWidget(self.checkbox2)
        self.all_v_layout.addWidget(self.checkbox3)

    def checkbox_init(self):
        self.checkbox1.setChecked(True)
        self.checkbox1.stateChanged.connect(lambda:self.on_state_change_func(self.checkbox1))

        self.checkbox2.setChecked(False)
        self.checkbox2.stateChanged.connect(lambda:self.on_state_change_func(self.checkbox2))

        self.checkbox3.setTristate(True)
        self.checkbox3.setCheckState(Qt.PartiallyChecked)
        self.checkbox3.stateChanged.connect(lambda:self.on_state_change_func(self.checkbox3))

    def on_state_change_func(self, checkbox):
        print('{} as clicked, and its current state is {}'.format(checkbox.text(), checkbox.checkState()))

################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
