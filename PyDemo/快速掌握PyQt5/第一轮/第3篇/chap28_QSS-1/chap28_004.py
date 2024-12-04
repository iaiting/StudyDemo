#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 28.3 子控件 之 QComboBox
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QComboBox
)

################################################################################
class Demo(QComboBox):
    def __init__(self) -> None:
        super().__init__()
        my_list = ['A', 'B', 'C', 'D']
        self.addItems(my_list)

################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()

    qss ='''
    QComboBox::drop-dwon
    '''
    demo.setStyleSheet(qss)
    demo.show()
    sys.exit(app.exec_())
