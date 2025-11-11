from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie
 
 
def crear_pagina_principal(parent=None):
    pagina = QWidget(parent)
    layout = QVBoxLayout(pagina)
    layout.setContentsMargins(40, 40, 40, 40)
    layout.setSpacing(20)
 
    # 🌠 GIF animado (en lugar de video)
    gif_label = QLabel()
    gif_label.setAlignment(Qt.AlignCenter)
    gif_label.setFixedHeight(400)
 
    movie = QMovie("espacio.gif")  # el archivo debe estar en la misma carpeta que main.py
    movie.setScaledSize(gif_label.size())
    movie.start()
 
    gif_label.setMovie(movie)
    layout.addWidget(gif_label, alignment=Qt.AlignCenter)
 
    # 🌟 Título principal
    titulo = QLabel("Bienvenido al Museo de Astronomía")
    titulo.setAlignment(Qt.AlignCenter)
    titulo.setStyleSheet("""
        color: #ffffff;
        font-size: 32px;
        font-weight: bold;
    """)
 
    # 🪐 Descripción
    descripcion = QLabel(
        "Explora el fascinante universo a través de nuestras secciones de estrellas, planetas, galaxias e historia de la astronomía."
    )
    descripcion.setAlignment(Qt.AlignCenter)
    descripcion.setWordWrap(True)
    descripcion.setStyleSheet("""
        color: #e0e0e0;
        font-size: 18px;
        line-height: 1.4;
    """)
 
    layout.addWidget(titulo)
    layout.addWidget(descripcion)
    layout.addStretch()
 
    return pagina
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie
 
 
def crear_pagina_principal(parent=None):
    pagina = QWidget(parent)
    layout = QVBoxLayout(pagina)
    layout.setContentsMargins(40, 40, 40, 40)
    layout.setSpacing(20)
 
    # 🌠 GIF animado (en lugar de video)
    gif_label = QLabel()
    gif_label.setAlignment(Qt.AlignCenter)
    gif_label.setFixedHeight(400)
 
    movie = QMovie("espacio.gif")  # el archivo debe estar en la misma carpeta que main.py
    movie.setScaledSize(gif_label.size())
    movie.start()
 
    gif_label.setMovie(movie)
    layout.addWidget(gif_label, alignment=Qt.AlignCenter)
 
    # 🌟 Título principal
    titulo = QLabel("Bienvenido al Museo de Astronomía")
    titulo.setAlignment(Qt.AlignCenter)
    titulo.setStyleSheet("""
        color: #ffffff;
        font-size: 32px;
        font-weight: bold;
    """)
 
    # 🪐 Descripción
    descripcion = QLabel(
        "Explora el fascinante universo a través de nuestras secciones de estrellas, planetas, galaxias e historia de la astronomía."
    )
    descripcion.setAlignment(Qt.AlignCenter)
    descripcion.setWordWrap(True)
    descripcion.setStyleSheet("""
        color: #e0e0e0;
        font-size: 18px;
        line-height: 1.4;
    """)
 
    layout.addWidget(titulo)
    layout.addWidget(descripcion)
    layout.addStretch()
 
    return pagina