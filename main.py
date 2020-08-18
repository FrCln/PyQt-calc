from functools import partial
import operator as op
import sys

from PyQt5 import QtWidgets

from calculatorui import Ui_MainWindow


class CalculatorApp(QtWidgets.QApplication):

    actions = {
        '+': op.add,
        '—': op.sub,
        '×': op.mul,
        '÷': op.truediv,
        '%': op.mod
    }

    def __init__(self, *args):
        super().__init__(*args)
        self.ui = Ui_MainWindow()
        self.digit_buttons = self.ui.findChildren(QtWidgets.QPushButton, 'digit')
        self.action_buttons = [
            self.ui.pushButton_14,
            self.ui.pushButton_15,
            self.ui.pushButton_16,
            self.ui.pushButton_17,
            self.ui.pushButton_35,
        ]
        self.result = None
        self.action = None
        self.new_number = False
        self.error = False
        self.build_handlers()
        self.ui.show()

    def build_handlers(self):
        for btn in self.digit_buttons:
            btn.clicked.connect(partial(self.add_digit, btn.text()))
        for btn in self.action_buttons:
            btn.clicked.connect(partial(self.add_action, btn.text()))
        self.ui.ButtonPoint.clicked.connect(self.add_point)
        self.ui.ButtonCE.clicked.connect(self.reset)
        self.ui.ButtonPM.clicked.connect(self.plus_minus)
        self.ui.ButtonBackspace.clicked.connect(self.backspace)
        self.ui.EqualButton.clicked.connect(self.equals)

    def equals(self):
        if not self.error:
            self.eval()
            self.new_number = True
            self.action = None
            self.ui.actionLabel.setText('')

    def read_num(self):
        num = self.ui.label.text()
        if '.' in num:
            num = float(num)
        else:
            num = int(num)
        return num

    def eval(self):
        if self.result and self.action and not self.new_number:
            num = self.read_num()
            if num == 0 and self.action in '÷%':
                self.ui.label.setText('Idiot!')
                self.action = None
                self.result = None
                self.new_number = True
                self.error = True
                return False
            self.result = self.actions[self.action](self.result, num)
            if abs(round(self.result) - self.result) < 1e-10:
                self.result = int(self.result)
            text = str(self.result)
            if self.result >= 0:
                text = ' ' + text
            self.ui.label.setText(text)
        return True

    def add_action(self, action, event):
        if not self.error:
            if self.eval():
                self.action = action
                self.result = self.read_num()
                self.new_number = True
                self.ui.actionLabel.setText(action)

    def add_digit(self, digit, event):
        if self.error:
            self.reset(False)
        if self.new_number:
            self.new_number = False
            text = ' '
        else:
            text = self.ui.label.text()
            if text == ' 0' or text == '-0':
                text = text[:-1]
        text += digit
        self.ui.label.setText(text)

    def add_point(self, event):
        if not self.error:
            if self.new_number:
                self.new_number = False
                text = ' 0'
            else:
                text = self.ui.label.text()
            if '.' not in text:
                text += '.'
                self.ui.label.setText(text)

    def reset(self, event):
        self.result = None
        self.action = None
        self.new_number = False
        self.error = False
        self.ui.label.setText(' 0')
        self.ui.actionLabel.setText('')

    def plus_minus(self, event):
        if not self.error:
            if self.new_number:
                self.new_number = False
                text = '-0'
            else:
                text = self.ui.label.text()
                if text[0] == '-':
                    text = ' ' + text[1:]
                else:
                    text = '-' + text[1:]
            self.ui.label.setText(text)

    def backspace(self, event):
        if not self.error:
            text = self.ui.label.text()
            text = text[:-1]
            if text == ' ' or text == '-':
                text += '0'
            self.ui.label.setText(text)


def my_exception_hook(exc_type, value, traceback):
    import traceback as tb
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setText(str(value))
    msg.setInformativeText(''.join(tb.format_exception(exc_type, value, traceback)))
    msg.setWindowTitle(exc_type.__name__)
    msg.exec_()


app = CalculatorApp(sys.argv)
sys.excepthook = my_exception_hook
app.exec()
