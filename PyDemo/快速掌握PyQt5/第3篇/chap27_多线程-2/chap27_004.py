#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 27.2 简单爬虫实战
#
################################################################################
import sys
from urllib import response
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
)
import urllib.request
from PyQt5.QtCore import QThread, pyqtSignal


################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.button = QPushButton('Start', self)

        self.label = QLabel('Ready to do', self)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.button)
        self.setLayout(self.v_layout)


################################################################################
class CrawlThread(QThread):
    status_signal = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()

    def run(self):
        self.status_signal.emit('Crawling')
        response = urllib.request.urlopen('https://www.python.org')
        

        self.status_signal.emit('Saving')
        print(response.read().decode('utf-8'))

        self.status_signal.emit('Done')


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


