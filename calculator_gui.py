# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 634)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_number('7'))
        self.Button_7.setGeometry(QtCore.QRect(20, 260, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Button_7.setFont(font)
        self.Button_7.setObjectName("Button_7")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_number('8'))
        self.Button_8.setGeometry(QtCore.QRect(110, 260, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Button_8.setFont(font)
        self.Button_8.setObjectName("Button_8")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_number('9'))
        self.Button_9.setGeometry(QtCore.QRect(200, 260, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Button_9.setFont(font)
        self.Button_9.setObjectName("Button_9")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_operator('-'))
        self.minusButton.setGeometry(QtCore.QRect(290, 260, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.addMemoryButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.modifyMemory('+'))
        self.addMemoryButton.setGeometry(QtCore.QRect(20, 130, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addMemoryButton.setFont(font)
        self.addMemoryButton.setObjectName("addMemoryButton")
        self.minusMemoryButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.modifyMemory('-'))
        self.minusMemoryButton.setGeometry(QtCore.QRect(90, 130, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.minusMemoryButton.setFont(font)
        self.minusMemoryButton.setObjectName("minusMemoryButton")
        self.saveMemoryButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.saveToMemory())
        self.saveMemoryButton.setGeometry(QtCore.QRect(160, 130, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveMemoryButton.setFont(font)
        self.saveMemoryButton.setObjectName("saveMemoryButton")
        self.recallMemoryButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.recallMemory())
        self.recallMemoryButton.setGeometry(QtCore.QRect(230, 130, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.recallMemoryButton.setFont(font)
        self.recallMemoryButton.setObjectName("recallMemoryButton")
        self.clearMemoryButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.clearMemory())
        self.clearMemoryButton.setGeometry(QtCore.QRect(300, 130, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clearMemoryButton.setFont(font)
        self.clearMemoryButton.setObjectName("clearMemoryButton")
        self.plusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_operator('+'))
        self.plusButton.setGeometry(QtCore.QRect(290, 180, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.backspace())
        self.arrowButton.setGeometry(QtCore.QRect(200, 180, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_it('%'))
        self.percentButton.setGeometry(QtCore.QRect(110, 180, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.clear_output())
        self.clearButton.setGeometry(QtCore.QRect(20, 180, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_operator('*'))
        self.multiplyButton.setGeometry(QtCore.QRect(290, 340, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_number('6'))
        self.Button_6.setGeometry(QtCore.QRect(200, 340, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Button_6.setFont(font)
        self.Button_6.setObjectName("Button_6")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_number('5'))
        self.Button_5.setGeometry(QtCore.QRect(110, 340, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Button_5.setFont(font)
        self.Button_5.setObjectName("Button_5")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_number('4'))
        self.Button_4.setGeometry(QtCore.QRect(20, 340, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Button_4.setFont(font)
        self.Button_4.setObjectName("Button_4")
        self.dvideButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_operator('/'))
        self.dvideButton.setGeometry(QtCore.QRect(290, 420, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.dvideButton.setFont(font)
        self.dvideButton.setObjectName("dvideButton")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_number('3'))
        self.Button_3.setGeometry(QtCore.QRect(200, 420, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Button_3.setFont(font)
        self.Button_3.setObjectName("Button_3")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_number('2'))
        self.Button_2.setGeometry(QtCore.QRect(110, 420, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Button_2.setFont(font)
        self.Button_2.setObjectName("Button_2")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_number('1'))
        self.Button_1.setGeometry(QtCore.QRect(20, 420, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Button_1.setFont(font)
        self.Button_1.setObjectName("Button_1")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.solve())
        self.equalButton.setGeometry(QtCore.QRect(290, 500, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(200, 500, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_number('0'))
        self.Button_0.setGeometry(QtCore.QRect(110, 500, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Button_0.setFont(font)
        self.Button_0.setObjectName("Button_0")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.negative_positive())
        self.plusminusButton.setGeometry(QtCore.QRect(20, 500, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(20, 10, 351, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #solve equation
    def solve(self):
        try:
            #store whats on screen
            screen = self.outputLabel.text()
            #evaluate what is on the screen
            answer = eval(screen)
            print(answer)
            #output the answer
            self.outputLabel.setText(str(answer))
        except:
            self.outputLabel.setText('ERROR')

    #change between negative and positive
    def negative_positive(self):
        eq = self.outputLabel.text()
        operatorFound = False

        if eq[0] == '-':
            x = eq[1:]
        else:
            x = eq

        for op in ('+', '*', '/', '-'): #the '-' sign must be the last operator in the tuple
            index = x.find(op)
            if index != -1 and x[len(x)-1].isdigit():
                operatorFound = True
                if eq[0] == '-':
                    index += 1
                break

        if operatorFound:
            operand = eq[index+1:]
            eq_temp = eq[:index+1]
            if '-' in operand:
                operand = operand[1:]
                eq = eq_temp + operand
                self.outputLabel.setText(eq)
            else:
                operand = '-' + operand
                eq = eq_temp + operand
                self.outputLabel.setText(eq)
        else:
            if '-' in eq[0]:
                self.outputLabel.setText(eq[1:])
            else:
                if eq != '0':
                    eq = '-' + eq
                    self.outputLabel.setText(eq)

    #replace any value in output label with 0
    def clear_output(self):
        self.outputLabel.setText('0')

    #remove a character
    def backspace(self):
        #store whats already on the screen
        screen = self.outputLabel.text()
        if screen != '0':
            self.outputLabel.setText(screen[:-1])
            if screen[:-1] == '':
                self.outputLabel.setText('0')

    def dot_it(self):
        eq = self.outputLabel.text()
        operatorFound = False

        if eq[0] == '-':
            x = eq[1:]
        else:
            x = eq

        for op in ('+', '-', '*', '/'):
            index = x.find(op)
            if index != -1:
                operatorFound = True
                if eq[0] == '-':
                    index += 1
                break

        if operatorFound:
            secondOperand = eq[index + 1:]

            if '.' not in secondOperand:
                self.outputLabel.setText(eq + '.')
        else:
            if '.' not in eq:
                self.outputLabel.setText(eq + '.')

    def pressed_number(self, pressed):
        if self.outputLabel.text() == '0':
            self.outputLabel.setText(f'{pressed}')
        else:
            #Concatenate the pressed button with what was already in label
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')

    def press_operator(self, pressed):
        eq = self.outputLabel.text()

        if eq[0] == '-':
            x = eq[1:]
        else:
            x = eq

        canInsertOperator = True
        for op in ('+', '-', '*', '/'):
            if op in x:
                canInsertOperator = False

        if canInsertOperator:
            #checks in starts with 0 and if true replaces 0 with 'nothing'
            if self.outputLabel.text() == '0':
                self.outputLabel.setText('')
            #concatenate the pressed button with what was already in label
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')

    def saveToMemory(self):
        writeFile = open('memory_gui.txt', 'w')
        screen = self.outputLabel.text()

        if screen[0] == '-':
            x = screen[1:]
        else:
            x = screen

        operatorFound = False
        for op in ('+', '*', '/', '-'):
            if op in x:
                operatorFound = True
                break

        if not operatorFound and screen[len(screen)-1].isdigit():
            writeFile.write(screen)
        else:
            self.outputLabel.setText('ERROR')

        writeFile.close()

    def recallMemory(self):
        readFile = open('memory_gui.txt', 'r')
        screen = self.outputLabel.text()
        file_content = readFile.read()
        readFile.close()
        if file_content == 'none':
            self.outputLabel.setText('ERROR')
        else:
            if screen[0] == '-':
                temp_screen = screen[1:]
            else:
                temp_screen = screen

            for op in ('+', '/', '*', '-'):
                index = temp_screen.find(op)
                if index != -1:
                    if screen[0] == '-':
                        index += 2 #use to include the operator when splicing label text
                    else:
                        index += 1 #adjust index by accounting for '-' at front of string that was left out
                    break

            if index == -1:
                self.outputLabel.setText(file_content)
            else:
                screen = screen[:index]
                self.outputLabel.setText(f'{screen}{file_content}')

    def clearMemory(self):
        file = open('memory_gui.txt','w')
        file.write('none')
        file.close()

    def modifyMemory(self, symbol):
        file = open('memory_gui.txt', 'r')
        file_content = file.read()
        file.close()

        if file_content == 'none':
            self.outputLabel.setText('ERROR')
        else:
            screen = self.outputLabel.text()

            if screen[0] == '-':
                temp_screen = screen[1:]
            else:
                temp_screen = screen

            operatorFound = False
            for op in ('+', '*', '/', '-'):
                if op in temp_screen:
                    operatorFound = True
                    break

            if operatorFound:
                self.outputLabel.setText('ERROR')

            else:
                answer = eval(f'{file_content}{symbol}{screen}')
                print(answer)
                file = open('memory_gui.txt', 'w')
                file.write(str(answer))
                file.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.addMemoryButton.setText(_translate("MainWindow", "M+"))
        self.minusMemoryButton.setText(_translate("MainWindow", "M-"))
        self.saveMemoryButton.setText(_translate("MainWindow", "MS"))
        self.recallMemoryButton.setText(_translate("MainWindow", "MR"))
        self.clearMemoryButton.setText(_translate("MainWindow", "MC"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.clearButton.setText(_translate("MainWindow", "C"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.dvideButton.setText(_translate("MainWindow", "/"))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.Button_0.setText(_translate("MainWindow", "0"))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))
        self.outputLabel.setText(_translate("MainWindow", "0"))

#a comment
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


