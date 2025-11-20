from PySide6.QtWidgets import( QWidget, QLabel, QVBoxLayout, QGroupBox, QPushButton, QGridLayout)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap

def crear_pagina_tienda(parent=None):
    pagina = QWidget(parent)
    layout = QGridLayout(pagina)

    titulo = QLabel("Area interactiva")
    titulo.setAlignment(Qt.AlignCenter)
    titulo.setStyleSheet("""
        color: #ffffff;
        font-size: 28px;
        font-weight: bold;
        font-family: 'Segoe UI';
    """)


    return pagina