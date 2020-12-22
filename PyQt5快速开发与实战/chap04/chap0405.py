#!/usr/bin/env python3
# -*- coding:utf-8 -*-

################################################################################
#
# 案例 4-5 建立第一个主窗口
#
################################################################################
import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.resize(300, 200)
window.move(250, 150)
window.setWindowTitle('Hello PyQt5')
window.show()
sys.exit(app.exec_())
