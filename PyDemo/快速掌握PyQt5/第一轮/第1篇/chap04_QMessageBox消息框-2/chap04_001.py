#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

################################################################################
#
# 4.1 各种类型的消息框
#
################################################################################
import sys

from PyQt5.QtWidgets import (
    QApplication, QPushButton, QWidget,
    QMessageBox,
)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton('information', self)
        self.button.clicked.connect(self.show_message)

    def show_message(self):
        print('show message')
        QMessageBox.information(self, 'Title', 'Content',
                                QMessageBox.No|QMessageBox.Cancel|QMessageBox.Yes)


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
