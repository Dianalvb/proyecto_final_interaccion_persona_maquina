from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QPushButton, QGraphicsOpacityEffect
from PySide6.QtCore import Qt, QPropertyAnimation
from PySide6.QtGui import QIcon

def crear_pagina_explorar(parent=None):
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

    # ------------------------------
    # FUNCIÓN QUE SÍ FUNCIONA
    # ------------------------------
    def animacion(boton, imagen_frente):

        # Mantener animaciones vivas en el botón
        boton.anim1 = None
        boton.anim2 = None

        efecto = QGraphicsOpacityEffect()
        boton.setGraphicsEffect(efecto)

        boton.flipped = False
        boton.front = imagen_frente
        boton.back = "Museo_Astronomia/reverse.jpg"

        # ---------------------------
        # Animación 1: desaparecer
        # ---------------------------
        anim1 = QPropertyAnimation(efecto, b"opacity")
        anim1.setDuration(200)
        anim1.setStartValue(1)
        anim1.setEndValue(0)

        def swap():
            if not boton.flipped:
                boton.setIcon(QIcon(boton.front))
            else:
                boton.setIcon(QIcon(boton.back))
            boton.flipped = not boton.flipped

        anim1.finished.connect(swap)

        # ---------------------------
        # Animación 2: aparecer
        # ---------------------------
        anim2 = QPropertyAnimation(efecto, b"opacity")
        anim2.setDuration(200)
        anim2.setStartValue(0)
        anim2.setEndValue(1)

        anim1.finished.connect(anim2.start)

        # Guardarlas para que no se eliminen
        boton.anim1 = anim1
        boton.anim2 = anim2

        boton.clicked.connect(anim1.start)

    # --------------------------
    # Crear tarjetas
    # --------------------------

    def crear_boton():
        boton = QPushButton()
        boton.setFixedSize(120, 120)
        boton.setIcon(QIcon("Museo_Astronomia/reverse.jpg"))
        boton.setIconSize(boton.size())  # IMPORTANTE
        return boton

    btn1 = crear_boton()
    animacion(btn1, "Museo_Astronomia/museo_astronomía1.jpg")
    layout.addWidget(btn1, 2, 0)

    btn2 = crear_boton()
    animacion(btn2, "Museo_Astronomia/museo_astronomía1.jpg")
    layout.addWidget(btn2, 2, 1)

    btn3 = crear_boton()
    animacion(btn3, "Museo_Astronomia/museo_astronomía1.jpg")
    layout.addWidget(btn3, 2, 2)

    layout.addWidget(titulo, 0, 0, 1, 3)
    layout.addWidget(descripcion, 1, 0, 1, 3)

    return pagina
