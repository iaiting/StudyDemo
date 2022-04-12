#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
#
# 27.2 简单爬虫实战
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget,
)


################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()


################################################################################
if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # demo = Demo()
    # demo.show()
    # sys.exit(app.exec_())
    import urllib.request
    response = urllib.request.urlopen('https://www.python.org')
    print(response.read().decode('utf-8'))
