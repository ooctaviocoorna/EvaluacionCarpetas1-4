#Importar
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QGridLayout,QWidget
from PyQt5.Qt import *
from PyQt5.QtGui import QIcon

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()                                          #Inicializando la super clase, la cual crea la ventana 
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 GUI')            #Añadiendo la ventana y cambiando propiedades
        self.resize(400,300)
        self.add_menus_and_status()
        self.layout_using_grid()

    def layout_using_grid(self):
        label_1=QLabel('First label')
        label_2=QLabel('Another label')
        label_span=QLabel('Label spanning columns span span span span')

        button_1=QPushButton('Click 1')
        button_2=QPushButton('Click 2')

        grid_layout=QGridLayout()

        grid_layout.addWidget(label_1,0,0)
        grid_layout.addWidget(button_1,0,1)
        grid_layout.addWidget(label_2,1,0)
        grid_layout.addWidget(button_2,1,1)
        grid_layout.addWidget(label_span,2,0,1,3)

        grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        grid_layout.setAlignment(label_1,Qt.AlignRight)
        grid_layout.setAlignment(label_2,Qt.AlignRight)

        layout_widget=QWidget()
        layout_widget.setLayout(grid_layout)

        self.setCentralWidget(layout_widget)

    def add_menus_and_status(self):
        self.statusBar().showMessage('Text in statusbar')

        menubar=self.menuBar()
        
        file_menu=menubar.addMenu('File')
        
        new_icon=QIcon('icons/new_icon.png')
        new_action=QAction(new_icon,'New',self)
        new_action.setStatusTip('New File')
        file_menu.addAction(new_action)
        
        file_menu.addSeparator()

        exit_icon=QIcon('icons/exit_icon.png')
        exit_action=QAction(exit_icon,'Exit',self)
        exit_action.setStatusTip('Click to exit the application.')
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut('Ctrl+Q')
        file_menu.addAction(exit_action)

        #-----------------------------------------------------------
        edit_menu=menubar.addMenu('Edit')

if __name__=='__main__':
    app=QApplication(sys.argv)                              #Creando la aplicación
    gui=GUI()                                                         #Creando la instancia de la clase
    gui.show()                                                  #Mostrando la ventana construida
    sys.exit(app.exec_())                                           #Ejecutando la aplicación
