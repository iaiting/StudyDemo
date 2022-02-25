#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 30.1 制作简单浏览器
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
)


################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.resize(1000, 600)

        self.back_btn = QPushButton()
        self.forward_btn = QPushButton()
        self.refresh_btn = QPushButton()

        self.zoom_in_btn = QPushButton()
        self.zoom_out_btn = QPushButton()


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
