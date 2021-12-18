#!/usr/bin/env python3

################################################################################
#
# 7.2 QToolButton
#
################################################################################
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication, QToolButton, QWidget,
)

################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.tool_button = QToolButton(self)
        self.tool_button.setIcon(QIcon('./image/win.png'))

        self.tool_button.setCheckable(True)
        self.tool_button.toggled.connect(self.button_state_func)

        self.tool_button.isCheckable()

    def button_state_func(self):
        print(self.tool_button.isChecked())

################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
