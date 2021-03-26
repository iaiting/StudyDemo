#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 17.2 鼠标事件
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
        self.button_label = QLabel('No Button Pressed', self)
        self.xy_label = QLabel('x:0, y:0', self)
        self.global_xy_label = QLabel('global x:0, global y:0', self)

        self.button_label.setAlignment(Qt.AlignCenter)
        self.xy_label.setAlignment(Qt.AlignCenter)
        self.global_xy_label.setAlignment(Qt.AlignCenter)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.button_label)
        self.v_layout.addWidget(self.xy_label)
        self.v_layout.addWidget(self.global_xy_label)

        self.setLayout(self.v_layout)

        self.resize(300, 300)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, QMouseEvent):
        print('mouseMoveEvent')
        x = QMouseEvent.x()
        y = QMouseEvent.y()
        self.xy_label.setText('x:{}, y:{}'.format(x, y))

        global_x = QMouseEvent.globalX()
        global_y = QMouseEvent.globalY()
        self.global_xy_label.setText('global x:{}, global y:{}'.format(global_x, global_y))

    def mousePressEvent(self, QMouseEvent):
        print("mousePressEvent")
        if QMouseEvent.button() == Qt.LeftButton:
            self.button_label.setText('Left Button Pressed')
        elif QMouseEvent.button() == Qt.MidButton:
            self.button_label.setText('Middle Button Pressed')
        elif QMouseEvent.button() == Qt.RightButton:
            self.button_label.setText('Right Button Pressed')


    def mouseReleaseEvent(self, QMouseEvent):
        print("mouseReleaseEvent")
        if QMouseEvent.button() == Qt.LeftButton:
            self.button_label.setText('Left Button Released')
        elif QMouseEvent.button() == Qt.MidButton:
            self.button_label.setText('Middle Button Released')
        elif QMouseEvent.button() == Qt.RightButton:
            self.button_label.setText('Right Button Released')

    def mouseDoubleClickEvent(self, QMouseEvent):
        print("mouseDoubleClickEvent")
        if QMouseEvent.button() == Qt.LeftButton:
            self.button_label.setText('Left Button Double Clicked')
        elif QMouseEvent.button() == Qt.MidButton:
            self.button_label.setText('Middle Button Double Clicked')
        elif QMouseEvent.button() == Qt.RightButton:
            self.button_label.setText('Right Button Double Clicked')


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
