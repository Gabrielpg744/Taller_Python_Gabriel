import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButiin,
from PyQt5 import uic

class Ventana(QMainWindow):
    def __init__(self, texto):
        super().__init__()
        uic.loadUi("Ventana.ui",self)
        self.BotonVerde.clicked.connect(self.imprimirMnesaje)
        self.texto=texto;

    def imprimirMnesaje(self):
        self.txtValor.setText(self.texto)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    miVentana = Ventana("Hola mundo")
    miVentana.show()
    sys.exit(app.exec)