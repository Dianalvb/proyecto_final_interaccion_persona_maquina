from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


def crear_pagina_explorar(parent=None):
    """Página para explorar el cosmos"""
    pagina = QWidget(parent)
    layout = QVBoxLayout(pagina)

    titulo = QLabel("Explorar el Cosmos")
    titulo.setAlignment(Qt.AlignCenter)
    titulo.setStyleSheet("""
        color: #ffffff;
        font-size: 28px;
        font-weight: bold;
        font-family: 'Segoe UI';
    """)

    descripcion = QLabel(
        "Sumérgete en los misterios del universo: estrellas, nebulosas, agujeros negros y más."
    )
    descripcion.setAlignment(Qt.AlignCenter)
    descripcion.setWordWrap(True)
    descripcion.setStyleSheet("""
        color: #cccccc;
        font-size: 18px;
        font-family: 'Segoe UI';
    """)

    layout.addStretch()
    layout.addWidget(titulo)
    layout.addWidget(descripcion)
    layout.addStretch()

    return pagina
