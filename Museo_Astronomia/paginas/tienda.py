from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGridLayout, QScrollArea,
    QFrame, QPushButton, QSizePolicy
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
import os


def crear_pagina_tienda(parent=None):
    pagina = QWidget()
    layout_principal = QVBoxLayout(pagina)
    layout_principal.setContentsMargins(0, 0, 0, 0)

    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    contenedor = QWidget()
    contenido = QVBoxLayout(contenedor)
    contenido.setContentsMargins(0, 0, 0, 0)

    # Portada
    portada = QLabel()
    ruta_portada = os.path.join(os.path.dirname(__file__), "logoahorasi.png")
    px = QPixmap(ruta_portada)

    if not px.isNull():
        portada.setPixmap(px.scaledToWidth(1400, Qt.SmoothTransformation))
    else:
        portada.setText("Falta tienda_portada.jpg")
        portada.setStyleSheet("font-size: 26px; color: #333; padding: 40px;")

    contenido.addWidget(portada)

    # Título
    titulo = QLabel("Online Boutique – Museo de Astronomía")
    titulo.setStyleSheet("""
        color: #2e2e2e;
        font-size: 38px;
        font-family: 'Times New Roman';
        font-weight: bold;
        margin-left: 40px;
        margin-top: 25px;
    """)

    descripcion = QLabel(
        "Explora nuestra selección de productos inspirados en el espacio: "
        "instrumentos, arte, iluminación, ciencia y objetos exclusivos del Museo de Astronomía."
    )
    descripcion.setWordWrap(True)
    descripcion.setStyleSheet("""
        color: #444;
        font-size: 17px;
        font-family: 'Georgia';
        margin-left: 40px;
        margin-right: 40px;
        margin-top: 10px;
        line-height: 1.4;
    """)

    contenido.addWidget(titulo)
    contenido.addWidget(descripcion)

    # Productos
    grid = QGridLayout()
    grid.setContentsMargins(40, 30, 40, 10)
    grid.setHorizontalSpacing(35)
    grid.setVerticalSpacing(35)

    productos = [
        ("replicaGalileo.jpg", "Telescopio Galileo – Réplica Decorativa"),
        ("meteoritoReal.webp", "Meteorito Real (Fragmento pequeño)"),
        ("LamparaRGB.jpg", "Lámpara Nebulosa RGB"),
        ("atlas.jpg", "Libro: Atlas de las Constelaciones"),
        ("puzzleVL.jpg", "Puzzle Vía Láctea – 1000 Piezas"),
        ("esferaSSLED.jpg", "Esfera del Sistema Solar – LED"),
        ("poster vintage ES.webp", "Póster Vintage – Eclipse Solar 1900"),
        ("cuboMarte.jpg", "Cubo de Marte – Fotos NASA"),
        ("FigAtronauta.jpg", "Figura Astronauta – Edición Museo"),
    ]

    fila = 0
    col = 0

    for img_file, nombre in productos:
        frame_prod = QFrame()
        frame_prod.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border-radius: 10px;
                border: 1px solid #cccccc;
            }
        """)

        layout_prod = QVBoxLayout(frame_prod)
        layout_prod.setContentsMargins(0, 0, 0, 0)

        img = QLabel()
        ruta_prod = os.path.join(os.path.dirname(__file__), img_file)
        p = QPixmap(ruta_prod)

        if p.isNull():
            img.setText("Imagen no encontrada")
            img.setAlignment(Qt.AlignCenter)
            img.setStyleSheet("color:#777; padding:20px;")
        else:
            img.setPixmap(p.scaled(380, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        texto = QLabel(nombre)
        texto.setAlignment(Qt.AlignCenter)
        texto.setStyleSheet("""
            font-family: 'Times New Roman';
            font-size: 18px;
            padding: 10px;
            color: #2d2d2d;
        """)

        boton = QPushButton("Ver más")
        boton.setFixedHeight(35)
        boton.setStyleSheet("""
            QPushButton {
                background-color: #70155F;
                color: white;
                border-radius: 8px;
                font-size: 15px;
                padding: 6px 15px;
            }
            QPushButton:hover {
                background-color: #5a0f4c;
            }
        """)

        layout_prod.addWidget(img)
        layout_prod.addWidget(texto)
        layout_prod.addWidget(boton, alignment=Qt.AlignCenter)

        grid.addWidget(frame_prod, fila, col)

        col += 1
        if col == 3:
            col = 0
            fila += 1

    contenido.addLayout(grid)

    # (Se eliminó la tarjeta de compra completa)

    scroll.setWidget(contenedor)
    layout_principal.addWidget(scroll)

    return pagina
