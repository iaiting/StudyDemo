#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 勾选菜单
#
################################################################################
import sys
from PyQt5.QtWidgets import (
    QMainWindow, QAction, QApplication
)


################################################################################
class Example(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')
        
        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction('view statusbar', self, checkable=True)
        viewMenu.addAction(viewStatAct)

        viewStatAct.setChecked(True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.triggered.connect(self.toggleMenu)


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')
        self.show()
        
    def toggleMenu(self, state):
        if state:
            pass
            self.statusbar.show()
        else:
            self.statusbar.hide()

################################################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
