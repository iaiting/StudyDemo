#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 12.1 QCalendarWidget
#
################################################################################
import sys
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QCalendarWidget, QLabel, QVBoxLayout
)

EMOTION = {  # 1
    '周一': '(╯°Д°)╯︵ ┻━┻',
    '周二': '(╯￣Д￣)╯╘═╛',
    '周三': '╭(￣▽￣)╯╧═╧',
    '周四': '_(:з」∠)_',
    '周五': '(๑•̀ㅂ•́)و✧',
    '周六': '( ˘ 3˘)♥',
    '周日': '(;′༎ຶД༎ຶ`)'
}


################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.calendar = QCalendarWidget(self)
        self.calendar.setMinimumDate(QDate(1946, 2, 14))
        self.calendar.setMaximumDate(QDate(6666, 6, 6))
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.show_emotino_func)

        print(self.calendar.minimumDate())
        print(self.calendar.maximumDate())
        print(self.calendar.selectedDate())

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        weekday = self.calendar.selectedDate().toString('ddd')
        self.label.setText(EMOTION[weekday])

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.calendar)
        self.v_layout.addWidget(self.label)
        self.setLayout(self.v_layout)

    def show_emotino_func(self):
        print("show_emotino_func")
        weekday = self.calendar.selectedDate().toString('ddd')
        print(weekday)
        self.label.setText(EMOTION[weekday])


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
