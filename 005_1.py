from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import *

class myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.s = ''    

        self.one = QPushButton('1')
        self.one.clicked.connect(lambda:self.clickedNum('1')) 
        #lambda(람다)에 : 콜론을 해주면 인풋값이 없다. 입력하는값이 없다. 
        #connect는 연결해주는 것이다.
        
        self.plus = QPushButton('+')
        self.plus.clicked.connect(lambda:self.clickedNum('+'))
        
        self.three = QPushButton('3')
        self.three.clicked.connect(lambda:self.clickedNum('3'))

        self.same =  QPushButton('=')
        self.same.clicked.connect(self.calc)

        hbox = QHBoxLayout()
        hbox.addWidget(self.one)
        hbox.addWidget(self.plus)
        hbox.addWidget(self.three)
        hbox.addWidget(self.same)
        
        self.setLayout(hbox)

        self.setWindowTitle("계산기")
        self.show()

    def clickedNum(self, text): #self는 인스턴스를 사용할때 사용하고 text는 들어오는값을 받을때 사용.
        self.s += text
        print(self.s)

    def calc(self):
        print(eval(self.s))
        self.s = ''
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myapp()
    app.exec_()