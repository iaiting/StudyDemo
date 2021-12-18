#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 7.4 QCheckBox
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget
)

################################################################################
class Demo(QWidget):
    pass

################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
