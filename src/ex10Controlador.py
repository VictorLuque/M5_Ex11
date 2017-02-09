# -*- coding: utf-8 -*-
import sys
#import QColorDialog
from PyQt4 import QtCore
from PyQt4.QtGui import *

from exercici10 import Ui_MainWindow

class Ventana (QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Ventana,self).__init__(parent)
        self.setupUi(self)
        self.horizontalSlider.setValue(10)
        self.horizontalSlider_2.setValue(10)
        self.horizontalSlider_3.setValue(10)
        self.textEdit.setText("AAA")
        self.frame.setStyleSheet("background-color: rgb("+str(self.horizontalSlider.value())+", "+str(self.horizontalSlider_2.value())+", "+str(self.horizontalSlider_3.value())+")")
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"),self.paleta)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"),self.sortir)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL("valueChanged(int)"), self.actualiza)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL("valueChanged(int)"), self.actualiza)
        QtCore.QObject.connect(self.horizontalSlider_3, QtCore.SIGNAL("valueChanged(int)"), self.actualiza)
        
        
    def paleta(self):
        color = QColor(self.horizontalSlider.value(),self.horizontalSlider_2.value(),self.horizontalSlider_3.value(), 255)
        newcolor = QColorDialog.getColor(color)
        self.horizontalSlider.setValue(newcolor.red())
        self.horizontalSlider_2.setValue(newcolor.green())
        self.horizontalSlider_3.setValue(newcolor.blue())
        self.frame.setStyleSheet("background-color: rgb("+str(self.horizontalSlider.value())+", "+str(self.horizontalSlider_2.value())+", "+str(self.horizontalSlider_3.value())+")")
    def actualiza(self):
        self.frame.setStyleSheet("background-color: rgb("+str(self.horizontalSlider.value())+", "+str(self.horizontalSlider_2.value())+", "+str(self.horizontalSlider_3.value())+")")
        self.textEdit.setText(str(self.hex(self.horizontalSlider.value())) + str(self.hex(self.horizontalSlider_2.value())) + str(self.hex(self.horizontalSlider_3.value())))
    def hex(self,dec):
        cont=[]
        strg=""
        hex=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        x=dec
        if (x==0):
            return "00"
        else:
            while (x> 0):
                res = x % 16
                x = x/16
                cont.append(hex[res])
            cont.reverse()
            for i in cont:
                strg = strg + str(i)
            return strg  
        
    def sortir(self):
        app.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    finestra = Ventana()
    finestra.show()
    sys.exit(app.exec_())