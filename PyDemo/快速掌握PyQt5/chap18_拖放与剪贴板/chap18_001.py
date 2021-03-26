#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 18.1 拖放
#
################################################################################
import sys
from PyQt5.QtWidgets import QApplication, QTextBrowser


################################################################################
class Demo(QTextBrowser):
    def __init__(self):
        super(Demo, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, QDragEnterEvent):
        print('dragEnterEvent')
        if QDragEnterEvent.mimeData().hasText():
            QDragEnterEvent.acceptProposedAction()
        pass

    def dragMoveEvent(self, QDragMoveEvent):
        print('dragMoveEvent')
        pass

    def dragLeaveEvent(self, QDragLeaveEvent):
        print('dragLeaveEvent')
        pass

    def dropEvent(self, QDropEvent):
        print('dropEvent')
        # Windows
        txt_path = QDropEvent.mimeData().text().replace('file:///', '')
        print('***********t101', txt_path)
        with open(txt_path, 'r') as f:
            self.setText(f.read())


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
