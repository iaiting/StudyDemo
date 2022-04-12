#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
#
# 27.2 简单爬虫实战
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, 
)
from PyQt5.QtCore import (
    Qt, QThread, pyqtSignal
)

import urllib.request

################################################################################
class Demo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.label = QLabel('Read to do')
        self.button = QPushButton('Start')

        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)

        self.v_layout.addWidget(self.label)


################################################################################
class CrawThread(QThread):
    status_signal = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()


    def run(self):
        self.status_signal.emit('Crawling')
        response = urllib.request.urlopen('https://www.python.org')
        
        self.status_signal.emit('Saving')
        with open('python.txt', 'w') as f:
            f.write(response.read().decode('utf-8'))

        self.status_signal.emit('Done')


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
