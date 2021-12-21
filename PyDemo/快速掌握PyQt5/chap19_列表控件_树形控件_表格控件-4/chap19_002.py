#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 19.2 树形控件QTreeWidget
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget,
)

################################################################################
class Demo(QWidget):
    pass
    def __init__(self):
        super().__init__()

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())