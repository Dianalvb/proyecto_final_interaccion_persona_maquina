from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

def crear_pagina_principal(parent=None):
    pagina = QWidget(parent)
    layout = QVBoxLayout(pagina)

    titulo = QLabel("Bienvenido al Museo de Astronomía")
    titulo.setAlignment(Qt.AlignCenter)
    titulo.setStyleSheet("""
        color: #ffffff;
        font-size: 28px;
        font-weight: bold;
    """)

    descripcion = QLabel(
        "Explora el fascinante universo a través de nuestras secciones de estrellas, planetas, galaxias e historia de la astronomía."
    )
    descripcion.setAlignment(Qt.AlignCenter)
    descripcion.setWordWrap(True)
    descripcion.setStyleSheet("""
        color: #cccccc;
        font-size: 18px;
    """)

    layout.addStretch()
    layout.addWidget(titulo)
    layout.addWidget(descripcion)
    layout.addStretch()

    return pagina
