#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 动态增加和删除控件
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QHBoxLayout, QVBoxLayout,
    QLayout,
)
from PyQt5.QtCore import Qt



################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.label_list = []
        for i in range(5):
            label = QLabel(str(i+1))
            label.setAlignment(Qt.AlignCenter)
            self.label_list.append(label)

        self.add_btn = QPushButton('增加文本')
        self.minus_btn = QPushButton('删除文本')
        self.add_btn.clicked.connect(self.add_slot)
        self.minus_btn.clicked.connect(self.minus_slot)

        all_v_layout = QVBoxLayout()
        self.v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        for l in self.label_list:
            self.v_layout.addWidget(l)

        h_layout.addWidget(self.add_btn)
        h_layout.addWidget(self.minus_btn)

        all_v_layout.addLayout(self.v_layout)
        all_v_layout.addLayout(h_layout)
        self.setLayout(all_v_layout)

        all_v_layout.setSizeConstraint(QLayout.SetFixedSize)
    
    def add_slot(self):
        label = QLabel(str(len(self.label_list) + 1))
        label.setAlignment(Qt.AlignCenter)
        self.label_list.append(label)
        self.v_layout.addWidget(label)

    def minus_slot(self):
        if len(self.label_list)  == 1:
            return 
        label = self.label_list.pop()
        label.deleteLater()


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
