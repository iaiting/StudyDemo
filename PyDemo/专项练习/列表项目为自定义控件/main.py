from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class myC(QWidget):
    def __init__(self):
        super().__init__()
        hlay = QHBoxLayout(self)
        hlay.setContentsMargins(0,0,0,0)
        hlay.setSpacing(0)
        self.lable = QLabel("this is lable")
        line = QLineEdit()
        btn = QPushButton("btn")
        hlay.addWidget(self.lable)
        hlay.addWidget(line)
        hlay.addWidget(btn)
        self.setLayout(hlay)
        btn.pressed.connect(self.btnclick)
    def setxy(self,x,y):
        self.x = x
        self.y = y
    def btnclick(self):
        print("xy:",self.x," ",self.y)


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        listwidget_1 = QListWidget(self)
        for rown in range(10):
            item = QListWidgetItem('111')
            wg = myC()
            wg.setxy(rown,0)
            wg.lable.setText(wg.lable.text()+" "+str(rown))
            listwidget_1.addItem(item)
            listwidget_1.setItemWidget(item,wg)

        
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(listwidget_1)
        self.setLayout(self.h_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = Demo()
    demo.show()
    app.exec_()