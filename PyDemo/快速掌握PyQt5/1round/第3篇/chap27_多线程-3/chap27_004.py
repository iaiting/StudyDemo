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
        self.label.setAlignment(Qt.AlignCenter)

        self.button = QPushButton('Start')
        self.button.clicked.connect(self.start_func)

        self.crawl_thread = CrawThread()
        self.crawl_thread.status_signal.connect(self.status_func)

        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)

        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.button)


    def start_func(self):
        print('start_func')
        self.crawl_thread.start()

    def status_func(self,status):
        self.label.setText(status)
################################################################################
class CrawThread(QThread):
    status_signal = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()


    def run(self):
        self.status_signal.emit('Crawling')
        response = urllib.request.urlopen('https://www.python.org')
        
        self.status_signal.emit('Saving')
        # print(response.read().decode('utf-8'))
        with open('./python.txt', 'wb') as f:
            f.write(response.read())

        self.status_signal.emit('Done')


################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
