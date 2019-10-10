# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Valida_Alfabeto import Valida_Alfabeto
import pyttsx3
from Ui_Automata_Impar_Palindrome import Ui_Automata_Impar_Palindrome

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 285)
        MainWindow.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"border-color: rgb(98, 98, 98);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 211, 20))
        self.label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.Cadena = QtWidgets.QLineEdit(self.centralwidget)
        self.Cadena.setGeometry(QtCore.QRect(120, 90, 151, 21))
        self.Cadena.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.Cadena.setObjectName("Cadena")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 70, 61, 16))
        self.label_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.Validar_alfabeto = QtWidgets.QPushButton(self.centralwidget)
        self.Validar_alfabeto.setGeometry(QtCore.QRect(160, 160, 75, 23))
        self.Validar_alfabeto.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.Validar_alfabeto.setObjectName("Validar_alfabeto")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 231, 16))
        self.label_3.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 210, 141, 16))
        self.label_4.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_4.setVisible(False)
        self.Verifica_Palindrome = QtWidgets.QPushButton(self.centralwidget)
        self.Verifica_Palindrome.setGeometry(QtCore.QRect(160, 230, 75, 23))
        self.Verifica_Palindrome.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.Verifica_Palindrome.setVisible(False)
        self.Verifica_Palindrome.setObjectName("Verifica_Palindrome")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Validar Palindrome ∑={a,b,c}"))
        self.label_2.setText(_translate("MainWindow", "Cadena"))
        self.Validar_alfabeto.setText(_translate("MainWindow", "Validar"))
        self.Validar_alfabeto.clicked.connect(self.Validar_Entrada)
        self.label_3.setText(_translate("MainWindow", "Validar si la cadena pertenece al alfabeto"))
        self.label_4.setText(_translate("MainWindow", "Verificar si es palindrome"))
        self.Verifica_Palindrome.setText(_translate("MainWindow", "Verificar"))
        self.Verifica_Palindrome.clicked.connect(self.Venta_Grafo)

    def Validar_Entrada(self):
        palabra=Valida_Alfabeto(self.Cadena.text())
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-60)
        if palabra.valida_expresion()== True:
            engine.say("La palabra si pertenece al alfabeto, puedes pasar a validar si es palindrome")
            engine.runAndWait()
            self.Verifica_Palindrome.setVisible(True)
            self.label_4.setVisible(True)
            self.Validar_alfabeto.setStyleSheet("background-color: green;")
            
        else:
            engine.say("La palabra No pertenece al alfabeto")
            engine.runAndWait()
            self.label_4.setVisible(False)
            self.Verifica_Palindrome.setVisible(False)
            self.Validar_alfabeto.setStyleSheet("background-color: rgb(147, 147, 147);")

    def Venta_Grafo(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_Automata_Impar_Palindrome()
        self.ui.setupUi(self.ventana)
        self.ui.Palabra.setText(self.Cadena.text())
        self.ui.label.setText(self.Cadena.text())
        self.ventana.show()
        
            
            
            
            




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
