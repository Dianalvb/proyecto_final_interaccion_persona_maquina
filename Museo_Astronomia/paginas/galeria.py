from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


def crear_pagina_galeria(parent=None):
    """Página de galería de imágenes astronómicas"""
    pagina = QWidget(parent)
    layout = QVBoxLayout(pagina)

    titulo = QLabel("Galería de Imágenes Astronómicas")
    titulo.setAlignment(Qt.AlignCenter)
    titulo.setStyleSheet("""
        color: #ffffff;
        font-size: 28px;
        font-weight: bold;
        font-family: 'Segoe UI';
    """)

    descripcion = QLabel(
        "Explora una colección impresionante de imágenes del universo, desde nebulosas hasta galaxias lejanas."
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
