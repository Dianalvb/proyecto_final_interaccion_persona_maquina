from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

def crear_pagina1(win, stack):
    p1 = QWidget()
    p1.setStyleSheet("background-color: #E6EBED;")
    layout = QVBoxLayout(p1)
    layout.setAlignment(Qt.AlignCenter)

    lbl = QLabel("Menús principales")
    lbl.setStyleSheet("font-family: Arial; font-size: 20px; font-weight: 600; color: #212121;")

    btn_to_p2 = QPushButton("Ir a pantalla 2")

    def ir_a_p2():
        stack.setCurrentIndex(1)
        win.menuBar().setVisible(False)
        win.statusBar().showMessage("Navegaste a pantalla 2", 2000)

    btn_to_p2.clicked.connect(ir_a_p2)

    layout.addWidget(lbl)
    layout.addWidget(btn_to_p2)

    return p1
