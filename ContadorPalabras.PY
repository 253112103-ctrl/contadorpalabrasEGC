import sys
from PyQt5 import QtWidgets, uic
class ContadorPalabras(QtWidgets.QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("ContadorPalabras.ui",self)
        self.btnContar.clicked.connect(self.ContarPalabras)
    def ContarPalabras(self):
        texto=self.edtCarateres.text()
        textoSeparado = texto.split()
        print(textoSeparado)
        catidadpalabras= len(textoSeparado)
        self.tvpalabras.setText(f"palabras:{catidadpalabras}")
        totalcaracteres = 0
        for palabra in textoSeparado:
            totalcaracteres += len(palabra)
        totalcaracteres
        self.tvcaracteres.setTect(f"caracteres: {totalcaracteres}")
app=QtWidgets.QApplication(sys.argv)
ventana= ContadorPalabras()
ventana.show()
sys.exit(app.exec())