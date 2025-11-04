from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QStatusBar
from paginas.inicio import crear_pagina1
from paginas.principal import crear_pagina2
import sys

# Crear app y ventana
app = QApplication()
win = QMainWindow()
win.resize(820, 480)
win.setWindowTitle("Navegador entre pantallas y menús")

# Stack principal
stack_main = QStackedWidget()
win.setCentralWidget(stack_main)

# Cargar pantallas externas
p1 = crear_pagina1(win, stack_main)
p2 = crear_pagina2(win, stack_main)

stack_main.addWidget(p1)  # index 0
stack_main.addWidget(p2)  # index 1

# Status bar
statusbar = QStatusBar()
win.setStatusBar(statusbar)
statusbar.showMessage("Listo. Estás en la pantalla principal.")

# Mostrar ventana
win.show()
sys.exit(app.exec())
