#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 窗口居中
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QDesktopWidget,
)


################################################################################
class Example(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())