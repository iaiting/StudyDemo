#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 11.1 简单示例
#
################################################################################
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QVBoxLayout


################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)
        self.lcd_1 = QLCDNumber(self)
        self.lcd_1.setDigitCount(10)
        self.lcd_1.display(1234567890)

        self.lcd_2 = QLCDNumber(self)
        self.lcd_2.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_2.setSmallDecimalPoint(True)

        self.lcd_2.setDigitCount(12)
        self.lcd_2.display(0.123456789)

        self.lcd_3 = QLCDNumber()
        self.lcd_3.setSegmentStyle(QLCDNumber.Filled)
        self.lcd_3.display('HELLO')

        self.lcd_4 = QLCDNumber()
        self.lcd_4.setSegmentStyle(QLCDNumber.Outline)
        self.lcd_4.setMode(QLCDNumber.Hex)
        self.lcd_4.setDigitCount(6)
        self.lcd_4.display(666)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.lcd_1)
        self.v_layout.addWidget(self.lcd_2)
        self.v_layout.addWidget(self.lcd_3)
        self.v_layout.addWidget(self.lcd_4)

        self.setLayout(self.v_layout)


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
