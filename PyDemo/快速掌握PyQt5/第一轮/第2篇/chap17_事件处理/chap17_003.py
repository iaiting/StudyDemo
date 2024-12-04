#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 17.3 键盘事件
#
################################################################################
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout
)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.pic_label = QLabel(self)
        self.pic_label.setText('键盘事件')
        self.pic_label.setAlignment(Qt.AlignCenter)

        self.key_label = QLabel('No Key Pressed',self)
        self.key_label.setAlignment(Qt.AlignCenter)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.pic_label)
        self.v_layout.addWidget(self.key_label)
        self.setLayout(self.v_layout)

    def keyPressEvent(self, QKeyEvent):
        print('keyPressEvent')
        if QKeyEvent.key() == Qt.Key_Up:
            self.key_label.setText('Key Up Pressed')
        elif QKeyEvent.key() == Qt.Key_Down:
            self.key_label.setText("Key Down Pressed")
        elif QKeyEvent.key() == Qt.Key_Left:
            self.key_label.setText("Key Left Pressed")
        elif QKeyEvent.key() == Qt.Key_Right:
            self.key_label.setText('Key Right Pressed')

    def keyReleaseEvent(self, QKeyEvent):
        print('keyReleaseEvent')
        self.key_label.setText('Key Released')


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
