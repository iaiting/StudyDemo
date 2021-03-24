#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 12.2 QDateTimeEdit
#
################################################################################
import sys
from PyQt5.QtCore import QDate, QTime, QDateTime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QDateTimeEdit,
    QVBoxLayout,
)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.datetime_1 = QDateTimeEdit(self)

        self.datetime_2 = QDateTimeEdit(QDateTime.currentDateTime(), self)

        self.datetime_3 = QDateTimeEdit(QDateTime.currentDateTime(), self)

        self.datetime_4 = QDateTimeEdit(QDate.currentDate(), self)

        self.datetime_5 = QDateTimeEdit(QTime.currentTime(), self)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.datetime_1)
        self.v_layout.addWidget(self.datetime_2)
        self.v_layout.addWidget(self.datetime_3)
        self.v_layout.addWidget(self.datetime_4)
        self.v_layout.addWidget(self.datetime_5)

        self.setLayout(self.v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())