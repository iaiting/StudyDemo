#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 28.3 子控件 之 QSpinBox
#
################################################################################
import sys
from PyQt5.QtWidgets import QApplication, QSpinBox

class Demo(QSpinBox):
    def __init__(self) -> None:
        super().__init__()
        self.setMinimum(0)
        self.setMaximum(100)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    qss ='''
    QSpinBox::up-button
    QSpinBox:down-button
    '''
    demo.setStyleSheet(qss)
    demo.show()
    sys.exit(app.exec_())
