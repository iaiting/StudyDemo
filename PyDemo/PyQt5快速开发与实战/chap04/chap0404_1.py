#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText("Button")
btn.move(20, 20)
widget.resize(300, 200)
widget.move(250, 200)

widget.setWindowTitle('PyQt 坐标系统例子')
widget.show()

print("QWidget:")
print("w.x() = %d" % widget.x())
print("w.y() = %d" % widget.y())
print("w.width = %d" % widget.width())
print("w.height = %d" % widget.height())

print("QWidget.geometry:")
print("widget.geometry.x() = %d" % widget.geometry().x())
print("widget.geometry.y() = %d" % widget.geometry().y())
print("widget.geometry.width() = %d" % widget.geometry().width())
print("widget.geometry.height() = %d" % widget.geometry().height())

sys.exit(app.exec_())
