from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QGridLayout, QSizePolicy)

class StretchButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(40, 40)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')

        self.to_solve = ''

        self.display = QLineEdit()
        self.display.setReadOnly(True)

        button1 = StretchButton('0')
        button2 = StretchButton('1')
        button3 = StretchButton('2')
        button4 = StretchButton('3')
        button5 = StretchButton('4')
        button6 = StretchButton('5')
        button7 = StretchButton('6')
        button8 = StretchButton('7')
        button9 = StretchButton('8')
        button10 = StretchButton('9')
        button11_b = StretchButton('<-')
        button12_C = StretchButton('C')
        button13_p = StretchButton('+')
        button14_m = StretchButton('-')
        button15_u = StretchButton('*')
        button16_d = StretchButton('/')
        button17_r = StretchButton('=')
        button18_p = StretchButton('.')

        layout = QGridLayout()
        layout.addWidget(self.display, 0, 0, 1, 4)
        layout.addWidget(button1, 5, 0, 1, 2)
        layout.addWidget(button2, 4, 0)
        layout.addWidget(button3, 4, 1)
        layout.addWidget(button4, 4, 2)
        layout.addWidget(button5, 3, 0)
        layout.addWidget(button6, 3, 1)
        layout.addWidget(button7, 3, 2)
        layout.addWidget(button8, 2, 0)
        layout.addWidget(button9, 2, 1)
        layout.addWidget(button10, 2, 2)
        layout.addWidget(button11_b, 1, 0)
        layout.addWidget(button12_C, 1, 1)
        layout.addWidget(button13_p, 1, 2)
        layout.addWidget(button14_m, 1, 3)
        layout.addWidget(button15_u, 2, 3)
        layout.addWidget(button16_d, 3, 3)
        layout.addWidget(button17_r, 4, 3, 2, 1)
        layout.addWidget(button18_p, 5, 2)

        self.setLayout(layout)

        button1.clicked.connect(self.button_handler)
        button2.clicked.connect(self.button_handler)
        button3.clicked.connect(self.button_handler)
        button4.clicked.connect(self.button_handler)
        button5.clicked.connect(self.button_handler)
        button6.clicked.connect(self.button_handler)
        button7.clicked.connect(self.button_handler)
        button8.clicked.connect(self.button_handler)
        button9.clicked.connect(self.button_handler)
        button10.clicked.connect(self.button_handler)
        button11_b.clicked.connect(self.button_handler)
        button12_C.clicked.connect(self.button_handler)
        button13_p.clicked.connect(self.button_handler)
        button14_m.clicked.connect(self.button_handler)
        button15_u.clicked.connect(self.button_handler)
        button16_d.clicked.connect(self.button_handler)
        button17_r.clicked.connect(self.button_handler)
        button18_p.clicked.connect(self.button_handler)
    
    def button_handler(self):
        button = self.sender()
        if button.text() in '0123456789/*-+.':
            self.to_solve += button.text()
        elif button.text() == '<-':
            self.to_solve = self.to_solve[0:-1]
        elif button.text() == 'C':
            self.to_solve = ''
        elif button.text() == '=':
            try:
                self.to_solve = str(eval(self.to_solve))
            except:
                self.to_solve = '0'
        self.display.setText(self.to_solve)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
