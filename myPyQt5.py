#Estructura de la aplicación

#Archivos a importar
import sys
from PyQt5.QtWidgets import *

#Creación de la aplicación
app=QApplication(sys.argv)

#Creación de la ventana
win=QWidget()

#Cambiando las propiedades de la ventana
win.setWindowTitle('PyQt5 GUI')
win.resize(400,300)

#Mostrando la ventana construida
win.show()

#Ejecutando la aplicación
sys.exit(app.exec_())
