# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana2_Automata.1.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets,QtTest
from Valida_Alfabeto import Valida_Alfabeto
from Pila import Pila
import pyttsx3






class Ui_Automata_Impar_Palindrome(object):

    

    def setupUi(self, Automata_Impar_Palindrome):
        Automata_Impar_Palindrome.setObjectName("Automata_Impar_Palindrome")
        #Automata_Impar_Palindrome.resize(700,500)
        Automata_Impar_Palindrome.setFixedSize(700,395)
        Automata_Impar_Palindrome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.Palindrome = QtWidgets.QWidget(Automata_Impar_Palindrome)
        self.Palindrome.setObjectName("Palindrome")
        self.Verifica_Lento = QtWidgets.QPushButton(self.Palindrome)
        self.Verifica_Lento.setGeometry(QtCore.QRect(110, 270, 91, 23))
        self.Verifica_Lento.setStyleSheet("background-color: rgb(106, 250, 154);")
        self.Verifica_Lento.setObjectName("Verifica_Lento")
        self.Verifica_rapido = QtWidgets.QPushButton(self.Palindrome)
        self.Verifica_rapido.setGeometry(QtCore.QRect(240, 270, 101, 23))
        self.Verifica_rapido.setStyleSheet("background-color: rgb(106, 250, 154);")
        self.Verifica_rapido.setObjectName("Verifica_rapido")
        self.Automata = QtWidgets.QLabel(self.Palindrome)
        self.Automata.setGeometry(QtCore.QRect(30, 150, 412, 91))
        self.Automata.setText("")
        self.Automata.setPixmap(QtGui.QPixmap("Imagen1_Automata.jpg"))
        self.Automata.setScaledContents(True)
        self.Automata.setObjectName("Automata")
        self.autor = QtWidgets.QLabel(self.Palindrome)
        self.autor.setGeometry(QtCore.QRect(30, 360, 101, 16))
        self.autor.setStyleSheet("font: 75 11pt \"Bahnschrift Light Condensed\";\n"
"background-color: rgb(175, 255, 207);")
        self.Tr5 = QtWidgets.QLabel(self.Palindrome)
        self.Tr5.setGeometry(QtCore.QRect(10, 140, 47, 13))
        self.Tr5.setObjectName("Tr5")
        self.Tr6 = QtWidgets.QLabel(self.Palindrome)
        self.Tr6.setGeometry(QtCore.QRect(10, 120, 47, 13))
        self.Tr6.setObjectName("Tr6")
        self.Tr7 = QtWidgets.QLabel(self.Palindrome)
        self.Tr7.setGeometry(QtCore.QRect(10, 80, 47, 13))
        self.Tr7.setObjectName("Tr7")
        self.Tr8 = QtWidgets.QLabel(self.Palindrome)
        self.Tr8.setGeometry(QtCore.QRect(10, 100, 47, 13))
        self.Tr8.setObjectName("Tr8")
        self.Tr9 = QtWidgets.QLabel(self.Palindrome)
        self.Tr9.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.Tr9.setObjectName("Tr9")
        self.Tr10 = QtWidgets.QLabel(self.Palindrome)
        self.Tr10.setGeometry(QtCore.QRect(10, 160, 47, 13))
        self.Tr10.setObjectName("Tr10")
        self.Tr11 = QtWidgets.QLabel(self.Palindrome)
        self.Tr11.setGeometry(QtCore.QRect(140, 190, 47, 13))
        self.Tr11.setObjectName("Tr11")
        self.Tr12 = QtWidgets.QLabel(self.Palindrome)
        self.Tr12.setGeometry(QtCore.QRect(140, 170, 47, 13))
        self.Tr12.setObjectName("Tr12")
        self.Tr2 = QtWidgets.QLabel(self.Palindrome)
        self.Tr2.setGeometry(QtCore.QRect(140, 210, 47, 13))
        self.Tr2.setObjectName("Tr2")
        self.Tr1 = QtWidgets.QLabel(self.Palindrome)
        self.Tr1.setGeometry(QtCore.QRect(270, 150, 47, 13))
        self.Tr1.setObjectName("Tr1")
        self.Tr4 = QtWidgets.QLabel(self.Palindrome)
        self.Tr4.setGeometry(QtCore.QRect(270, 170, 47, 13))
        self.Tr4.setObjectName("Tr4")
        self.Tr3 = QtWidgets.QLabel(self.Palindrome)
        self.Tr3.setGeometry(QtCore.QRect(320, 220, 47, 13))
        self.Tr3.setObjectName("Tr3")
        self.Palabra = QtWidgets.QLineEdit(self.Palindrome)
        self.Palabra.setGeometry(QtCore.QRect(60, 90, 391, 20))
        self.Palabra.setObjectName("Palabra")
        #self.Palabra.setDisabled(1)
        self.label_Pila= QtWidgets.QLabel(self.Palindrome)
        self.label_Pila.setGeometry(QtCore.QRect(504, 8, 47, 13))
        self.label_Pila.setObjectName("label")
        self.imagen_robot = QtWidgets.QLabel(self.Palindrome)
        self.imagen_robot.setGeometry(QtCore.QRect(540, 20, 141, 370))
        self.imagen_robot.setText("")
        self.imagen_robot.setPixmap(QtGui.QPixmap("automata_imagen.png"))
        self.imagen_robot.setScaledContents(True)
        self.imagen_robot.setObjectName("imagen_robot")
        self.Titulo_Palabra = QtWidgets.QLabel(self.Palindrome)
        self.Titulo_Palabra.setGeometry(QtCore.QRect(200, 70, 111, 16))
        self.Titulo_Palabra.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.Titulo_Palabra.setObjectName("Titulo_Palabra")
        self.listWidget = QtWidgets.QListWidget(self.Palindrome)
        self.listWidget.setGeometry(QtCore.QRect(500, 20, 31, 411))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.addItem("#")
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label = QtWidgets.QLabel(self.Palindrome)
        self.label.setGeometry(QtCore.QRect(70, 20, 481, 21))
        self.label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        Automata_Impar_Palindrome.setCentralWidget(self.Palindrome)
        self.statusbar = QtWidgets.QStatusBar(Automata_Impar_Palindrome)
        self.statusbar.setObjectName("statusbar")
        Automata_Impar_Palindrome.setStatusBar(self.statusbar)
        self.listWidget.setStyleSheet("background-color: rgb(175, 255, 207);")

        self.retranslateUi(Automata_Impar_Palindrome)
        QtCore.QMetaObject.connectSlotsByName(Automata_Impar_Palindrome)

    def retranslateUi(self, Automata_Impar_Palindrome):
        _translate = QtCore.QCoreApplication.translate
        Automata_Impar_Palindrome.setWindowTitle(_translate("Automata_Impar_Palindrome", "MainWindow"))
        self.Verifica_Lento.setText(_translate("Automata_Impar_Palindrome", "Validar_Lento"))
        self.Verifica_rapido.setText(_translate("Automata_Impar_Palindrome", "Validar_Rapido"))
        self.Tr5.setText(_translate("Automata_Impar_Palindrome", "b/#/#b"))
        self.Tr6.setText(_translate("Automata_Impar_Palindrome", "a/a/aa"))
        self.Tr7.setText(_translate("Automata_Impar_Palindrome", "a/b/ba"))
        self.Tr8.setText(_translate("Automata_Impar_Palindrome", "b/a/ab"))
        self.Tr9.setText(_translate("Automata_Impar_Palindrome", "b/b/bb"))
        self.Tr10.setText(_translate("Automata_Impar_Palindrome", "a/#/#a"))
        self.Tr11.setText(_translate("Automata_Impar_Palindrome", "c/b/b"))
        self.Tr12.setText(_translate("Automata_Impar_Palindrome", "c/#/#"))
        self.Tr2.setText(_translate("Automata_Impar_Palindrome", "c/a/a"))
        self.Tr1.setText(_translate("Automata_Impar_Palindrome", "b/b/ λ"))
        self.Tr4.setText(_translate("Automata_Impar_Palindrome", "a/a/ λ"))
        self.Tr3.setText(_translate("Automata_Impar_Palindrome", " λ/#/#"))
        self.Titulo_Palabra.setText(_translate("Automata_Impar_Palindrome", "PALABRA"))
        self.Verifica_Lento.clicked.connect(self.Simulador_Automata_lento)
        self.Verifica_rapido.clicked.connect(self.Simulador_Automata_rapido)
        self.label_Pila.setText(_translate("Automata_Impar_Palindrome", "PILA"))
        self.autor.setText(_translate("MainWindow", "by JOSE CORREA"))
        self.listWidget.addItem("#")

    def Simulador_Automata_lento(self):
        self.label.clear()
        self.Palabra.setEnabled(False)
        self.Verifica_rapido.setEnabled(False)
        self.Verifica_Lento.setEnabled(False)
        self.imagen_robot.setPixmap(QtGui.QPixmap("automata_imagen.png"))
        palabra=self.Palabra.text()+"#"
        Pila_Valida=Pila()
        Pila_Valida.apilar("#")
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-60)
        estado_actual="q0"
        bandera=1
        self.label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";""color: green")
        self.listWidget.clear()
        
        mostrando_cadena_recorrida=""
        for caracter in palabra:
            #(a/#/#a)
            if Pila_Valida.tope()=="#" and caracter=="a" and estado_actual=="q0":
                mostrando_cadena_recorrida="a"
                self.Tr10.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen2_Automata.jpg"))
                estado_actual="q0"
                Pila_Valida.desapilar()
                Pila_Valida.apilar("#")
                Pila_Valida.apilar("a")
                engine.say("Estado inicial q0. leyendo una a")
                engine.runAndWait()
                QtTest.QTest.qWait(1000) 
                self.Tr10.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
                self.label.setText(mostrando_cadena_recorrida)
                Tamaño_list=Pila_Valida.tamano()
                self.listWidget.clear()
                self.listWidget.addItem(caracter)
                for i in range(1,Tamaño_list+1):
                    self.listWidget.addItem(Pila_Valida.mostrar()[Tamaño_list-i])
                  
                
            #(a/a/aa)   
            elif Pila_Valida.tope()=="a" and caracter=="a" and estado_actual=="q0":
                mostrando_cadena_recorrida=mostrando_cadena_recorrida+"a"
                QtTest.QTest.qWait(1000)
                self.Tr6.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen2_Automata.jpg"))
                estado_actual="q0"
                Pila_Valida.desapilar()
                Pila_Valida.apilar("a")
                Pila_Valida.apilar("a")
                engine.say("continúa en Estado inicial q0. leyendo una a")
                engine.runAndWait()
                QtTest.QTest.qWait(1000)
                self.label.setText(caracter+caracter)
                self.Tr6.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
                self.label.setText(mostrando_cadena_recorrida)
                Tamaño_list=Pila_Valida.tamano()
                self.listWidget.clear()
                self.listWidget.addItem(caracter)
                for i in range(1,Tamaño_list+1):
                    self.listWidget.addItem(Pila_Valida.mostrar()[Tamaño_list-i])
                    
                
            #(b/a/ab)
            elif Pila_Valida.tope()=="a" and caracter=="b" and estado_actual=="q0":
                mostrando_cadena_recorrida=mostrando_cadena_recorrida+"b"
                self.Tr8.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen2_Automata.jpg"))
                estado_actual="q0"
                Pila_Valida.desapilar()
                Pila_Valida.apilar("a")
                Pila_Valida.apilar("b")
                engine.say("continúa en Estado inicial q0. leyendo una b")
                engine.runAndWait()
                QtTest.QTest.qWait(1000)
                self.Tr8.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
                self.label.setText(mostrando_cadena_recorrida)
                Tamaño_list=Pila_Valida.tamano()
                self.listWidget.clear()
                self.listWidget.addItem(caracter)
                for i in range(1,Tamaño_list+1):
                    self.listWidget.addItem(Pila_Valida.mostrar()[Tamaño_list-i])
            #(c/b/b)
            elif Pila_Valida.tope()=="b" and caracter=="c" and estado_actual=="q0":
                mostrando_cadena_recorrida=mostrando_cadena_recorrida+"c"
                self.Tr11.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen3_Automata.jpg"))
                estado_actual="q1"
                Pila_Valida.desapilar()
                Pila_Valida.apilar("b")
                engine.say("pasa al estado q1. leyendo una c")
                engine.runAndWait()
                QtTest.QTest.qWait(1000)
                self.Tr11.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
                self.label.setText(mostrando_cadena_recorrida)
                Tamaño_list=Pila_Valida.tamano()
                self.listWidget.clear()
                self.listWidget.addItem("b")
                for i in range(1,Tamaño_list+1):
                    self.listWidget.addItem(Pila_Valida.mostrar()[Tamaño_list-i])
            #(b/b/λ)
            elif Pila_Valida.tope()=="b" and caracter=="b" and estado_actual=="q1":
                mostrando_cadena_recorrida=mostrando_cadena_recorrida+"b"
                QtTest.QTest.qWait(1000)
                self.Tr1.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen3_Automata.jpg"))
                estado_actual="q1"
                Pila_Valida.desapilar()
                engine.say("continúa en Estado q1. leyendo una b")
                engine.runAndWait()
                QtTest.QTest.qWait(1000)
                self.Tr1.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
                self.label.setText(mostrando_cadena_recorrida)
                Tamaño_list=Pila_Valida.tamano()
                self.listWidget.clear()
                self.listWidget.addItem(caracter)
                for i in range(1,Tamaño_list+1):
                    self.listWidget.addItem(Pila_Valida.mostrar()[Tamaño_list-i])
            #(a/a/λ)
            elif Pila_Valida.tope()=="a" and caracter=="a" and estado_actual=="q1":
                mostrando_cadena_recorrida=mostrando_cadena_recorrida+"a"
                QtTest.QTest.qWait(1000)
                self.Tr4.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen3_Automata.jpg"))
                estado_actual="q1"
                Pila_Valida.desapilar()
                engine.say("continúa en estado q1. leyendo una a")
                engine.runAndWait()
                QtTest.QTest.qWait(1000)
                self.Tr4.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
                self.label.setText(mostrando_cadena_recorrida)
                Tamaño_list=Pila_Valida.tamano()
                self.listWidget.clear()
                self.listWidget.addItem(caracter)
                for i in range(1,Tamaño_list+1):
                    self.listWidget.addItem(Pila_Valida.mostrar()[Tamaño_list-i])
            #(λ/#/#)
            elif Pila_Valida.tope()=="#" and estado_actual=="q1" and bandera==len(palabra):
                #self.label.setText(mostrando_cadena_recorrida)
                self.Tr3.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen3_Aceptacion.jpg"))
                estado_actual="q2"
                QtTest.QTest.qWait(1000)
                self.Tr3.setStyleSheet("color: rgb(0, 0, 0);")
                engine.say("pasa al Estado De aceptacion leyendo vacío. La palabra es palindrome")
                engine.runAndWait()
                self.label.setText("SI ES PALINDROME")
                bandera=bandera+1
                self.imagen_robot.setPixmap(QtGui.QPixmap("automata_imagen_aceptada.png"))
                self.listWidget.addItem("#")
                #self.Palabra.setStyleSheet("background-color: rgb(207,232, 162);")
                self.label.setVisible(True)
                msg=QtWidgets.QMessageBox()
                msg.setText("ES PALINDROME")
                msg.setStyleSheet("color: green")
                msg.show()
                msg.exec()
                self.label.clear()
                self.Verifica_rapido.setEnabled(True)
                self.Verifica_Lento.setEnabled(True)
                Tamaño_list=Pila_Valida.tamano()
                self.listWidget.clear()
                for i in range(1,Tamaño_list+1):
                    self.listWidget.addItem(Pila_Valida.mostrar()[Tamaño_list-i])
                self.Palabra.setEnabled(True)
                
            #(b/#/#b) 
            elif Pila_Valida.tope()=="#" and caracter=="b" and estado_actual=="q0":
                mostrando_cadena_recorrida=mostrando_cadena_recorrida+"b"
                self.Tr5.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen2_Automata.jpg"))
                estado_actual="q0"
                Pila_Valida.desapilar()
                Pila_Valida.apilar("#")
                Pila_Valida.apilar("b")
                engine.say("Estado inicial q0. leyendo una b")
                engine.runAndWait()
                QtTest.QTest.qWait(1000) 
                self.Tr5.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
                self.label.setText(mostrando_cadena_recorrida)
                Tamaño_list=Pila_Valida.tamano()
                self.listWidget.clear()
                self.listWidget.addItem(caracter)
                for i in range(1,Tamaño_list+1):
                    self.listWidget.addItem(Pila_Valida.mostrar()[Tamaño_list-i])
            #(c/#/#)
            elif Pila_Valida.tope()=="#" and caracter=="c" and estado_actual=="q0":
                mostrando_cadena_recorrida=mostrando_cadena_recorrida+"c"
                self.Tr12.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen3_Automata.jpg"))
                estado_actual="q1"
                engine.say("pasa al estado q1. leyendo una c")
                engine.runAndWait()
                QtTest.QTest.qWait(1000)
                self.Tr12.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
                self.label.setText(mostrando_cadena_recorrida)
                Tamaño_list=Pila_Valida.tamano()
                self.listWidget.clear()
                for i in range(1,Tamaño_list+1):
                    self.listWidget.addItem(Pila_Valida.mostrar()[Tamaño_list-i])
            #b/b/bb
            elif Pila_Valida.tope()=="b" and caracter=="b" and estado_actual=="q0":
                mostrando_cadena_recorrida=mostrando_cadena_recorrida+"b"
                QtTest.QTest.qWait(1000)
                self.Tr9.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen2_Automata.jpg"))
                estado_actual="q0"
                Pila_Valida.desapilar()
                Pila_Valida.apilar("b")
                Pila_Valida.apilar("b")
                engine.say("continúa en Estado inicial q0. leyendo una b")
                engine.runAndWait()
                QtTest.QTest.qWait(1000)
                self.Tr9.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
                self.label.setText(mostrando_cadena_recorrida)
                Tamaño_list=Pila_Valida.tamano()
                self.listWidget.clear()
                self.listWidget.addItem(caracter)
                for i in range(1,Tamaño_list+1):
                    self.listWidget.addItem(Pila_Valida.mostrar()[Tamaño_list-i])
            #(c/a/a)
            elif Pila_Valida.tope()=="a" and caracter=="c" and estado_actual=="q0":
                mostrando_cadena_recorrida=mostrando_cadena_recorrida+"c"
                self.Tr2.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen3_Automata.jpg"))
                estado_actual="q1"
                Pila_Valida.desapilar()
                Pila_Valida.apilar("a")
                engine.say("pasa al estado q1. leyendo una c")
                engine.runAndWait()
                QtTest.QTest.qWait(1000)
                self.Tr2.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
                self.label.setText(mostrando_cadena_recorrida)
                Tamaño_list=Pila_Valida.tamano()
                self.listWidget.clear()
                self.listWidget.addItem("a")
                for i in range(1,Tamaño_list+1):
                    self.listWidget.addItem(Pila_Valida.mostrar()[Tamaño_list-i])
            #(a/b/ba)
            elif Pila_Valida.tope()=="b" and caracter=="a" and estado_actual=="q0":
                mostrando_cadena_recorrida=mostrando_cadena_recorrida+"a"
                self.Tr7.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen2_Automata.jpg"))
                estado_actual="q0"
                Pila_Valida.desapilar()
                Pila_Valida.apilar("b")
                Pila_Valida.apilar("a")
                engine.say("continúa en Estado inicial q0. leyendo una a")
                engine.runAndWait()
                QtTest.QTest.qWait(1000)
                self.Tr7.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
                self.label.setText(mostrando_cadena_recorrida)
                Tamaño_list=Pila_Valida.tamano()
                self.listWidget.clear()
                self.listWidget.addItem(caracter)
                for i in range(1,Tamaño_list+1):
                    self.listWidget.addItem(Pila_Valida.mostrar()[Tamaño_list-i])
                
            else:
                mostrando_cadena_recorrida=mostrando_cadena_recorrida+caracter
                engine.say("Se quedó sin camino y no finalizó en un estado de aceptacion")
                engine.runAndWait()
                self.label.setText(mostrando_cadena_recorrida)
                self.label.setStyleSheet("color: red;")
                self.imagen_robot.setPixmap(QtGui.QPixmap("automata_imagen_denegado.jpg"))
                msg=QtWidgets.QMessageBox()
                msg.setText("se quedó sin camino NO ES PALINDROME")
                msg.setStyleSheet("color: red")
                msg.show()
                msg.exec()
                msg=QtWidgets.QMessageBox()
                break

        if estado_actual != "q2":
            engine.say("No es palindrome")
            engine.runAndWait()
            self.label.setText("NO ES PALINDROME")
            self.label.setStyleSheet("color: red")
            msg=QtWidgets.QMessageBox()
            msg.setText("debe ser de la forma: ZcZ^(-1), Z=(a*,b*)")
            msg.setStyleSheet("color: red")
            msg.show()
            msg.exec()
            self.label.clear()
            self.Automata.setPixmap(QtGui.QPixmap("Imagen1_Automata.jpg"))
            Tamaño_list=Pila_Valida.tamano()
            self.listWidget.clear()
            self.listWidget.addItem(caracter)
            for i in range(1,Tamaño_list+1):
                self.listWidget.addItem(Pila_Valida.mostrar()[Tamaño_list-i])
            self.Verifica_rapido.setEnabled(True)
            self.Verifica_Lento.setEnabled(True)
            self.Palabra.setEnabled(True)
            
    def Simulador_Automata_rapido(self):
        self.Palabra.setEnabled(False)
        self.Verifica_rapido.setEnabled(False)
        self.Verifica_Lento.setEnabled(False)
        self.imagen_robot.setPixmap(QtGui.QPixmap("automata_imagen.png"))
        palabra=self.Palabra.text()+"#"
        Pila_Valida=Pila()
        Pila_Valida.apilar("#")
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-60)
        estado_actual="q0"
        bandera=1
        self.listWidget.clear()
        for caracter in palabra:
            #(a/#/#a)
            if Pila_Valida.tope()=="#" and caracter=="a" and estado_actual=="q0":
                self.Tr10.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen2_Automata.jpg"))
                estado_actual="q0"
                Pila_Valida.desapilar()
                Pila_Valida.apilar("#")
                Pila_Valida.apilar(caracter)
                self.Tr10.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
            #(a/a/aa)   
            elif Pila_Valida.tope()=="a" and caracter=="a" and estado_actual=="q0":
                self.Tr6.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen2_Automata.jpg"))
                estado_actual="q0"
                Pila_Valida.desapilar()
                Pila_Valida.apilar("a")
                Pila_Valida.apilar("a")
                self.Tr6.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
            #(b/a/ab)
            elif Pila_Valida.tope()=="a" and caracter=="b" and estado_actual=="q0":
                self.Tr8.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen2_Automata.jpg"))
                estado_actual="q0"
                Pila_Valida.desapilar()
                Pila_Valida.apilar("a")
                Pila_Valida.apilar("b")
                self.Tr8.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
            #(c/b/b)
            elif Pila_Valida.tope()=="b" and caracter=="c" and estado_actual=="q0":
                self.Tr11.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen3_Automata.jpg"))
                estado_actual="q1"
                Pila_Valida.desapilar()
                Pila_Valida.apilar("b")
                self.Tr11.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
            #(b/b/λ)
            elif Pila_Valida.tope()=="b" and caracter=="b" and estado_actual=="q1":
                QtTest.QTest.qWait(1000)
                self.Tr1.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen3_Automata.jpg"))
                estado_actual="q1"
                Pila_Valida.desapilar()
                self.Tr1.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
            #(a/a/λ)
            elif Pila_Valida.tope()=="a" and caracter=="a" and estado_actual=="q1":
                QtTest.QTest.qWait(1000)
                self.Tr4.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen3_Automata.jpg"))
                estado_actual="q1"
                Pila_Valida.desapilar()
                self.Tr4.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
            #(λ/#/#)
            elif Pila_Valida.tope()=="#" and estado_actual=="q1" and bandera==len(palabra):
                self.Tr3.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen3_Aceptacion.jpg"))
                estado_actual="q2"
                self.Tr3.setStyleSheet("color: rgb(0, 0, 0);")
                #self.Palabra.setStyleSheet("background-color: rgb(207,232, 162);")
                self.imagen_robot.setPixmap(QtGui.QPixmap("automata_imagen_aceptada.png"))
                engine.say("palindrome")
                engine.runAndWait()
                self.label.setText("SI ES PALINDROME")
                self.label.setStyleSheet("color: GREEN")
                bandera=bandera+1
                self.label.setVisible(True)
                msg=QtWidgets.QMessageBox()
                msg.setText("ES PALINDROME")
                msg.setStyleSheet("color: green")
                msg.show()
                msg.exec()
                self.label.setVisible(True)
                self.Verifica_rapido.setEnabled(True)
                self.Verifica_Lento.setEnabled(True)
                self.Palabra.setEnabled(True)
                
            #(b/#/#b) 
            elif Pila_Valida.tope()=="#" and caracter=="b" and estado_actual=="q0":
                self.Tr5.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen2_Automata.jpg"))
                estado_actual="q0"
                Pila_Valida.desapilar()
                Pila_Valida.apilar("#")
                Pila_Valida.apilar("b")
                self.Tr5.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
            #(c/#/#)
            elif Pila_Valida.tope()=="#" and caracter=="c" and estado_actual=="q0":
                self.Tr12.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen3_Automata.jpg"))
                estado_actual="q1"
                self.Tr12.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
            #b/b/bb
            elif Pila_Valida.tope()=="b" and caracter=="b" and estado_actual=="q0":
                self.Tr9.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen2_Automata.jpg"))
                estado_actual="q0"
                Pila_Valida.desapilar()
                Pila_Valida.apilar("b")
                Pila_Valida.apilar("b")
                self.Tr9.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
            #(c/a/a)
            elif Pila_Valida.tope()=="a" and caracter=="c" and estado_actual=="q0":
                self.Tr2.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen3_Automata.jpg"))
                estado_actual="q1"
                Pila_Valida.desapilar()
                Pila_Valida.apilar("a")
                self.Tr2.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
            #(a/b/ba)
            elif Pila_Valida.tope()=="b" and caracter=="a" and estado_actual=="q0":
                self.Tr7.setStyleSheet("color: rgb(11, 143, 38);")
                self.Automata.setPixmap(QtGui.QPixmap("Imagen2_Automata.jpg"))
                estado_actual="q0"
                Pila_Valida.desapilar()
                Pila_Valida.apilar("b")
                Pila_Valida.apilar("a")
                self.Tr7.setStyleSheet("color: rgb(0, 0, 0);")
                bandera=bandera+1
            else:
                engine.say("No palindrome")
                engine.runAndWait()
                self.imagen_robot.setPixmap(QtGui.QPixmap("automata_imagen_denegado.jpg"))
                msg=QtWidgets.QMessageBox()
                msg.setText("se quedó sin camino NO ES PALINDROME")
                msg.setStyleSheet("color: red")
                msg.show()
                msg.exec()
                

                break

        if estado_actual != "q2":
            self.label.setText("NO ES PALINDROME")
            self.label.setStyleSheet("color: red")
            msg=QtWidgets.QMessageBox()
            msg.setText("debe ser de la forma: ZcZ^(-1), Z=(a*,b*)")
            msg.show()
            msg.setStyleSheet("color: red")
            msg.exec() 
            self.label.setVisible(False)
            self.Automata.setPixmap(QtGui.QPixmap("Imagen1_Automata.jpg"))  
            Tamaño_list=Pila_Valida.tamano()
            self.listWidget.clear()
            for i in range(1,Tamaño_list+1):
                self.listWidget.addItem(Pila_Valida.mostrar()[Tamaño_list-i])
            self.Verifica_rapido.setEnabled(True)
            self.Verifica_Lento.setEnabled(True)  
            self.Palabra.setEnabled(True)  
    


        
        
                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Automata_Impar_Palindrome = QtWidgets.QMainWindow()
    ui = Ui_Automata_Impar_Palindrome()
    ui.setupUi(Automata_Impar_Palindrome)
    Automata_Impar_Palindrome.show()
    sys.exit(app.exec_())
