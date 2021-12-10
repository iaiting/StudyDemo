#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 1.2 程序运行起点，先实例化Label再调用setText()方法来设置文本
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QLabel
)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel()
    label.setText('Hello World')
    label.show()
    sys.exit(app.exec_())
