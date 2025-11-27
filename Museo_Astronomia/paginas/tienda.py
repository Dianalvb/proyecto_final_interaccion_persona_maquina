from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGridLayout, QScrollArea,
    QFrame, QPushButton, QSizePolicy, QFormLayout, QLineEdit,
    QComboBox, QCheckBox, QRadioButton, QButtonGroup
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsDropShadowEffect
import os


def crear_pagina_tienda(parent=None):
    pagina = QWidget()
    layout_principal = QVBoxLayout(pagina)
    layout_principal.setContentsMargins(0, 0, 0, 0)

    # ============================================================
    #   SCROLL
    # ============================================================
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    contenedor = QWidget()
    contenido = QVBoxLayout(contenedor)
    contenido.setContentsMargins(0, 0, 0, 0)

    # ============================================================
    #   PORTADA
    # ============================================================
    portada = QLabel()
    ruta_portada = os.path.join(os.path.dirname(__file__), "tienda_portada.jpg")
    px = QPixmap(ruta_portada)

    if not px.isNull():
        portada.setPixmap(px.scaledToWidth(1400, Qt.SmoothTransformation))
    else:
        portada.setText("Falta tienda_portada.jpg")
        portada.setStyleSheet("font-size: 26px; color: #333; padding: 40px;")

    contenido.addWidget(portada)

    # ============================================================
    #   TÍTULO + DESCRIPCIÓN
    # ============================================================
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

    # ============================================================
    #   GRID DE PRODUCTOS (ACTUALIZADO)
    # ============================================================
    grid = QGridLayout()
    grid.setContentsMargins(40, 30, 40, 10)
    grid.setHorizontalSpacing(35)
    grid.setVerticalSpacing(35)

    productos = [
        ("telescopio.jpg", "Telescopio Galileo – Réplica Decorativa"),
        ("meteorito.jpg", "Meteorito Real (Fragmento pequeño)"),
        ("lampara_nebulosa.jpg", "Lámpara Nebulosa RGB"),
        ("atlas.jpg", "Libro: Atlas de las Constelaciones"),
        ("puzzle.jpg", "Puzzle Vía Láctea – 1000 Piezas"),
        ("esfera_led.jpg", "Esfera del Sistema Solar – LED"),
        ("poster.jpg", "Póster Vintage – Eclipse Solar 1900"),
        ("marte_cubo.jpg", "Cubo de Marte – Fotos NASA"),
        ("astronauta.jpg", "Figura Astronauta – Edición Museo"),
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

    # ============================================================
    #   TARJETA DE COMPRA (FORMULARIO)
    # ============================================================
    card = QFrame()
    card.setStyleSheet("background-color: white; border-radius: 14px;")
    card_layout = QFormLayout(card)
    card_layout.setContentsMargins(40, 40, 40, 40)
    card_layout.setSpacing(18)

    sombra = QGraphicsDropShadowEffect()
    sombra.setBlurRadius(40)
    sombra.setXOffset(0)
    sombra.setYOffset(8)
    sombra.setColor(Qt.black)
    card.setGraphicsEffect(sombra)

    nombre = QLineEdit()
    nombre.setPlaceholderText("Tu nombre completo")

    boletos = QComboBox()
    boletos.addItems([
        "Entrada general – $120",
        "Entrada nocturna – $150",
        "Pase anual – $700",
        "Entrada infantil – $80"
    ])

    extra1 = QCheckBox("Visita guiada por astrónomo (+$50)")
    extra2 = QCheckBox("Acceso al telescopio solar (+$30)")
    extra3 = QCheckBox("Audioguía digital (+$25)")

    pago_label = QLabel("Método de pago")
    rb1 = QRadioButton("Tarjeta")
    rb2 = QRadioButton("Efectivo")
    rb3 = QRadioButton("Pago digital")

    grupo = QButtonGroup(card)
    grupo.addButton(rb1)
    grupo.addButton(rb2)
    grupo.addButton(rb3)

    btn_comprar = QPushButton("Comprar Entradas")
    btn_comprar.setStyleSheet("""
        QPushButton {
            background-color: #006241;
            color: white;
            padding: 10px 20px;
            border-radius: 10px;
            font-size: 15px;
        }
        QPushButton:hover {
            background-color: #00845c;
        }
    """)

    btn_cancelar = QPushButton("Cancelar")
    btn_cancelar.setStyleSheet("""
        QPushButton {
            background-color: #b00020;
            color: white;
            padding: 10px 20px;
            border-radius: 10px;
            font-size: 15px;
        }
        QPushButton:hover {
            background-color: #c62828;
        }
    """)

    card_layout.addRow("Nombre:", nombre)
    card_layout.addRow("Tipo de entrada:", boletos)
    card_layout.addRow(extra1)
    card_layout.addRow(extra2)
    card_layout.addRow(extra3)
    card_layout.addRow(pago_label)
    card_layout.addWidget(rb1)
    card_layout.addWidget(rb2)
    card_layout.addWidget(rb3)
    card_layout.addRow(btn_comprar, btn_cancelar)

    contenido.addWidget(card, alignment=Qt.AlignCenter)

    scroll.setWidget(contenedor)
    layout_principal.addWidget(scroll)

    return pagina
