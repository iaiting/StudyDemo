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
    QApplication, QWidget, QDateTimeEdit, QDateEdit, QTimeEdit,
    QVBoxLayout,
)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.datetime_1 = QDateTimeEdit(self)
        self.datetime_1.dateChanged.connect(lambda : print('Date Changed!'))

        self.datetime_2 = QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.datetime_2.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        self.datetime_2.dateChanged.connect(lambda: print('Time Changed!'))

        self.datetime_3 = QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.datetime_3.dateChanged.connect(lambda: print('DateTime Changed!'))
        self.datetime_3.setCalendarPopup(True)

        self.datetime_4 = QDateTimeEdit(QDate.currentDate(), self)

        self.datetime_5 = QDateTimeEdit(QTime.currentTime(), self)

        self.date = QDateEdit(QDate.currentDate(), self)
        self.date.setDisplayFormat('yyyy/MM/dd')

        self.time = QTimeEdit(QTime.currentTime(), self)
        self.time.setDisplayFormat('HH:mm:ss')

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.datetime_1)
        self.v_layout.addWidget(self.datetime_2)
        self.v_layout.addWidget(self.datetime_3)
        self.v_layout.addWidget(self.datetime_4)
        self.v_layout.addWidget(self.datetime_5)

        self.v_layout.addWidget(self.date)
        self.v_layout.addWidget(self.time)

        self.setLayout(self.v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())