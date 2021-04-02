#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 27.2 简单爬虫实战
#
################################################################################
import sys
import urllib.request
from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
)


################################################################################
class CrawlThread(QThread):
    status_signal = pyqtSignal(str)

    def __init__(self):
        super(CrawlThread, self).__init__()

    def run(self):
        self.status_signal.emit('Crawling')
        response = urllib.request.urlopen('https://www.python.org')

        self.status_signal.emit('Saving')
        with open('python.txt', 'w') as f:
            f.write(response.read().decode('utf-8'))

        self.status_signal.emit('Done')
        self.sleep(3)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        self.label = QLabel('Ready to do', self)
        self.label.setAlignment(Qt.AlignCenter)

        self.button = QPushButton('Start', self)
        self.button.clicked.connect(self.start_func)

        self.crawl_thread = CrawlThread()
        self.crawl_thread.status_signal.connect(self.status_func)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.button)
        self.setLayout(self.v_layout)

    def start_func(self):
        self.crawl_thread.start()

    def status_func(self, status):
        self.label.setText(status)
        pass


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

