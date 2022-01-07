#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 23.2 程序启动画面QSplashScreen
#
################################################################################
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QSplashScreen, QWidget
)
from PyQt5.QtCore import Qt

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

################################################################################
if __name__ == "__main__":
    import time

    app = QApplication(sys.argv)

    splash = QSplashScreen()
    splash.setPixmap(QPixmap('../images/splash.jpg'))
    splash.show()
    splash.showMessage('Welcome to Use This PyQt5-made Notebook~', Qt.AlignBottom | Qt.AlignCenter, Qt.red)
    time.sleep(2)
    demo = Demo()
    demo.show()
    splash.finish(demo)
    sys.exit(app.exec_())
