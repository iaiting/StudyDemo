#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 9.1 QSlider
#
################################################################################
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QSlider,
    QVBoxLayout,
    QWidget
)

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.slider_1 = QSlider(Qt.Horizontal, self)
        self.slider_1.setRange(0, 100)
        self.slider_1.valueChanged.connect(lambda: self.on_change_func(self.slider_1))

        self.slider_2 = QSlider(Qt.Vertical, self)
        self.slider_2.setMinimum(0)
        self.slider_2.setMaximum(100)
        self.slider_2.valueChanged.connect(lambda: self.on_change_func(self.slider_2))

        self.label = QLabel('0', self)
        self.label.setFont(QFont('Arial Black', 20))


        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.setLayout(self.v_layout)

        self.v_layout.addWidget(self.slider_1)
        
        self.v_layout.addLayout(self.h_layout)
        self.h_layout.addWidget(self.slider_2)

        self.h_layout.addStretch(1)
        self.h_layout.addWidget(self.label)
        
        self.h_layout.addStretch(1)

    def on_change_func(self, slier):
        if slier == self.slider_1:
            self.label.setText(str(self.slider_1.value()))
            self.slider_2.setValue(self.slider_1.value())
        elif slier == self.slider_2:
            self.label.setText(str(self.slider_2.value()))
            self.slider_1.setValue(self.slider_2.value())
        else:
            pass


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
