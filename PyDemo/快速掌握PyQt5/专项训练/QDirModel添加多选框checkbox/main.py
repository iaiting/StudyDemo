#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
#
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QDirModel, QWidget
)
class Demo(QWidget):
    pass
    def __init__(self):
        super().__init__()
        self.model = QDirModel

def main():
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

################################################################################
if __name__ == '__main__':
    main()
