#!/usr/bin/env python3
# -*- coding:utf-8 -*-

################################################################################
#
# 案例 4-4 屏幕坐标系统显示
#
################################################################################
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText("Button")
btn.move(0, 0)

widget.resize(300, 200)
widget.move(250, 200)

widget.setWindowTitle("PyQt 坐标系统例子")
widget.show()

print("QWidget")
print("w.x()=%d" % widget.x())
print("w.y()=%d" % widget.y())
print("w.width=%d" % widget.width())
print("w.height=%d" % widget.height())

print("QWidget.geometry()")
print("QWidget.geometry().x()=%d" % widget.geometry().x())
print("QWidget.geometry().y()=%d" % widget.geometry().y())
print("QWidget.geometry().width()=%d" % widget.geometry().width())
print("QWidget.geometry().height()=%d" % widget.geometry().height())

sys.exit(app.exec_())
