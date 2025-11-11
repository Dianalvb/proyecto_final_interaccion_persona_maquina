from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea, QStackedLayout, QFrame
from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie
import os


def crear_pagina_principal(parent=None, base_path="."):
    pagina = QWidget(parent)
    layout_principal = QVBoxLayout(pagina)
    layout_principal.setContentsMargins(0, 0, 0, 0)
    layout_principal.setSpacing(0)

    # Scroll principal
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    contenedor_scroll = QWidget()
    layout_scroll = QVBoxLayout(contenedor_scroll)
    layout_scroll.setContentsMargins(0, 0, 0, 0)
    layout_scroll.setSpacing(0)

    # ==============================
    # 🌠 Banner tipo Louvre
    # ==============================
    banner = QFrame()
    banner.setMinimumHeight(800)
    banner.setStyleSheet("background-color: black;")

    # Apilamos GIF + overlay + texto centrado
    layout_banner = QStackedLayout(banner)
    layout_banner.setContentsMargins(0, 0, 0, 0)
    layout_banner.setStackingMode(QStackedLayout.StackAll)

    # 🎞️ GIF de fondo
    gif_label = QLabel()
    gif_label.setAlignment(Qt.AlignCenter)
    gif_label.setScaledContents(True)
    ruta_gif = os.path.join(base_path, "espacio.gif")
    ruta_gif = os.path.abspath(ruta_gif)
    print("Ruta del GIF:", ruta_gif, "Existe:", os.path.exists(ruta_gif))

    movie = QMovie(ruta_gif)
    gif_label.setMovie(movie)
    movie.start()

    # 🕶️ Capa semitransparente
    overlay = QLabel()
    overlay.setStyleSheet("background-color: rgba(0, 0, 0, 100);")

    # ✨ Contenedor del texto (centrado con ancho limitado)
    texto_contenedor = QWidget()
    texto_layout = QVBoxLayout(texto_contenedor)
    texto_layout.setContentsMargins(0, 0, 0, 0)
    texto_layout.setAlignment(Qt.AlignCenter)

    texto = QLabel("Bienvenido al Museo de Astronomía")
    texto.setAlignment(Qt.AlignCenter)
    texto.setWordWrap(True)
    texto.setStyleSheet("""
        color: white;
        font-size: 56px;
        font-weight: bold;
        background: transparent;
        max-width: 900px;
        padding: 30px;
    """)

    texto_layout.addWidget(texto, alignment=Qt.AlignCenter)

    # Apilar todo (de abajo hacia arriba)
    layout_banner.addWidget(gif_label)
    layout_banner.addWidget(overlay)
    layout_banner.addWidget(texto_contenedor)

    layout_scroll.addWidget(banner)

    # ==============================
    # 🌌 Sección inferior
    # ==============================
    bienvenida = QLabel("""
        <h2 style="color:#293170; text-align:center;">Explora el universo</h2>
        <p style="color:#333333; text-align:center; font-size:20px; max-width:900px; margin:auto;">
            Descubre los secretos de las estrellas, planetas y galaxias a través de experiencias interactivas y visuales únicas.
        </p>
    """)
    bienvenida.setAlignment(Qt.AlignCenter)
    bienvenida.setWordWrap(True)
    bienvenida.setStyleSheet("background-color: #f5f5f5; padding: 60px;")
    layout_scroll.addWidget(bienvenida)

    extra = QLabel("""
        <h2 style="color:#1a1a2e; text-align:center;">Más allá del cielo</h2>
        <p style="color:#444; text-align:center; font-size:18px; max-width:800px; margin:auto;">
            Sumérgete en una colección digital inspirada en los museos de ciencia y tecnología más reconocidos del mundo.
        </p>
    """)
    extra.setAlignment(Qt.AlignCenter)
    extra.setWordWrap(True)
    extra.setStyleSheet("background-color: #ffffff; padding: 80px; border-top: 3px solid #ccc;")
    layout_scroll.addWidget(extra)

    layout_scroll.addStretch()
    contenedor_scroll.setLayout(layout_scroll)
    scroll.setWidget(contenedor_scroll)
    layout_principal.addWidget(scroll)

    return pagina
