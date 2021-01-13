#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 案例4-3 关闭主窗口
#
################################################################################
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QMainWindow


################################################################################
class WinForm(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('关闭主窗口例子')
        self.button1 = QPushButton('关闭主窗口')
        self.button1.clicked.connect(self.onButtonClick)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self):
        qApp = QApplication.instance()
        qApp.quit()


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())
