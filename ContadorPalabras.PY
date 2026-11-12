import sys
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):

    def __init__ (self):
        super().__init__()
        uic.loadUi("ContadorPalabras.ui",self)
        self.btnContar.Clicked.connect(self.ContarPalabras)

    def ContarPalabras(self):
        texto=self.edtCaracteres.text()
        textoSeparado = texto.split()
        print(textoSeparado)
        print("se ha presionado el boton")

    


app=QtWidgets.QApplication(sys.argv)
ventana= ContadorPalabras()
ventana.show()
sys.exit(app.exec())