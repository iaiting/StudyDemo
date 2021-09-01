#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
#
#
################################################################################
import sys

from PyQt5.QtWidgets import (
    QApplication,
)

################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel('aa')
    label.show()
    sys.exit(app.exec_())