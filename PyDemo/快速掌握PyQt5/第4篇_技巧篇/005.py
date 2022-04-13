#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 窗口在屏幕居中显示
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget
)


################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # self.resize(100, 100)
        self.center()

    def center(self):
        desktop = QApplication.desktop()
        d_w = desktop.width()
        d_h = desktop.height()

        pos_x = d_w/2 - self.frameGeometry().width() / 2
        pos_y = d_h/2 - self.frameGeometry().height() / 2

        self.move(int(pos_x), int(pos_y))


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
