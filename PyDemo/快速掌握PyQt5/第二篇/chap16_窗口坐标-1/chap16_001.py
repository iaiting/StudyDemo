#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 16.1 理解坐标体系
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget
)

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(200, 200)
        self.move(100, 100)
        self.show()

        print('-----------------x(), y(), pos()-----------------')
        print(self.x())
        print(self.y())
        print(self.pos())

        print('-----------------width(), height()-----------------')
        print(self.width())
        print(self.height())

        print('-----------------geometry().x(), geometry.y(), geometry()-----------------')
        print(self.geometry().x())
        print(self.geometry().y())
        print(self.geometry())

        print('-----------------geometry.width(), geometry().height()-----------------')
        print(self.geometry().width())
        print(self.geometry().height())

        print('-----------------frameGeometry().x(), frameGeometry().y(), frameGeometry(), '
              'frameGeometry().width(), frameGeometry().height()-----------------')
        print(self.frameGeometry().x())
        print(self.frameGeometry().y())
        print(self.frameGeometry())
        print(self.frameGeometry().width())
        print(self.frameGeometry().height())


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    # demo.show()
    sys.exit(app.exec_())

