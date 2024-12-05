#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 2.2 多个信号连接同一个槽
#
################################################################################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton('Start', self)
        self.button.pressed.connect(self.change_text)
        self.button.released.connect(self.change_text)

    def change_text(self):
        print("change_text")
        if self.button.text() == 'Start':
            self.button.setText('Stop')
        else:
            self.button.setText('Start')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
