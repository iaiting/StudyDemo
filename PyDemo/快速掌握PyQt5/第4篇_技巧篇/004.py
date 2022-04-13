#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 在线程中获取窗口控件内容
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


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())