#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 拖曳无边框窗口
#
################################################################################
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget
)


################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)

    def mousePressEvent(self, QMouseEvent) -> None:
        self.start_x = QMouseEvent.x()
        self.start_y = QMouseEvent.y()
        print(self.start_x)
        print(self.start_y)

    def mouseMoveEvent(self, QMouseEvent) -> None:
        print(QMouseEvent.x())
        print(QMouseEvent.y())

        dis_x = QMouseEvent.x() - self.start_x
        dis_y = QMouseEvent.y() - self.start_y
        self.move(self.x()+ dis_x, self.y()+ dis_y)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
