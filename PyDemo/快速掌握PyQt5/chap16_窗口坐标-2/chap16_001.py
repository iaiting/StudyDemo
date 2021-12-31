#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 16.1 理解坐标体系
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
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(200, 200)
    widget.show()

    print('---------------- pos(), x(), y() ----------------')
    print(widget.pos())
    print(widget.pos().x())
    print(widget.pos().y())

    print('---------------- width(), height() ----------------')
    print(widget.width())
    print(widget.height())


    print('---------------- geometry() geometry().x(), geometry.y() ----------------')
    print(widget.geometry())
    print(widget.geometry().x())
    print(widget.geometry().y())

    print('---------------- geometry.width(), geometry().height() ----------------')
    print(widget.geometry().width())
    print(widget.geometry().height())


    print('---------------- frameGeometrys widget.frameGeometry().x(), widget.frameGeometry().y(),',
    'frameGeometry().width() ----------------')
    print(widget.frameGeometry())
    print(widget.frameGeometry().x())
    print(widget.frameGeometry().y())
    print(widget.frameGeometry().width())
    print(widget.frameGeometry().height())

    sys.exit(app.exec_())

