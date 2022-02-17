#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 23.2 程序启动画面QSplashScreen
#
################################################################################

import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QSplashScreen,
)

################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()


################################################################################
if __name__ == '__main__':
    import time
    app = QApplication(sys.argv)

    splash = QSplashScreen()
    # splash.resize(800, 800)
    splash.setPixmap(QPixmap('./python.jpg'))
    splash.show()
    splash.showMessage('welcome to Use This PyQt5-Made Notbook~',
                       Qt.AlignBottom|Qt.AlignCenter, Qt.blue)
    time.sleep(5)
    demo = Demo()
    demo.show()
    splash.finish(demo)
    sys.exit(app.exec_())
