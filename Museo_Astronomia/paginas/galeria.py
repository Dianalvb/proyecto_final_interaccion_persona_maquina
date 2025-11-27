from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton,
    QStackedWidget, QGraphicsOpacityEffect
)
from PySide6.QtCore import Qt, QSize, QPropertyAnimation
from PySide6.QtGui import QPixmap


def crear_pagina_galeria(parent=None):
    pagina = QWidget(parent)

    # 🌌 Fondo espacial suave (imagen en carpeta assets)
    pagina.setStyleSheet("""
        QWidget {
            background-image: url('Museo_Astronomia/fondo_espacio.jpg');
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: cover;
        }
    """)

    layout_principal = QVBoxLayout(pagina)

    # 🔭 TÍTULO
    titulo = QLabel("Conoce el Cosmos")
    titulo.setAlignment(Qt.AlignCenter)
    titulo.setStyleSheet("""
        color: #ffffff;
        font-size: 40px;
        font-weight: bold;
        text-shadow: 2px 2px 6px black;
    """)

    # 🔹 Información que cambiará según la imagen seleccionada
    texto_info = QLabel("")
    texto_info.setAlignment(Qt.AlignTop | Qt.AlignLeft)
    texto_info.setWordWrap(True)
    texto_info.setStyleSheet("""
        color: #e6e6e6;
        font-size: 18px;
        padding: 15px;
        background-color: rgba(0,0,0,0.45);
        border-radius: 12px;
    """)

    # 🔭 Lista de imágenes + textos largos explicativos
    imagenes = [
        (
            "Museo_Astronomia/museo_astronomía1.jpg",
            """🌌 Nebulosa de Orión
            
            Una de las regiones de formación estelar más brillantes del cielo nocturno.
            Contiene miles de estrellas jóvenes, nubes de gas y polvo que revelan la 
            actividad dinámica del universo. Es visible incluso a simple vista desde 
            cielos oscuros."""
        ),
        (
            "Museo_Astronomia/museo_astronomia2.jpg",
            """🌠 Galaxias Espirales
            
            Estructuras gigantes compuestas por miles de millones de estrellas.
            Sus brazos espirales albergan nubes moleculares y sistemas planetarios en
            constante evolución. Nuestra galaxia, la Vía Láctea, pertenece a esta clase."""
        ),
        (
            "Museo_Astronomia/museo_astronomia3.jpg",
            """✨ Nebulosa del Cangrejo
            
            Resultado de una explosión de supernova observada en el año 1054. 
            En su interior, un púlsar emite radiación intensa, iluminando la nube 
            que aún se expande con gran velocidad."""
        ),
        (
            "Museo_Astronomia/museo_astronomia3.jpg",
            """🌌 Universo Profundo
            
            Imágenes capturadas por telescopios espaciales revelan cúmulos, 
            supercúmulos y galaxias que se encuentran a millones de años luz 
            de distancia, permitiendo estudiar la historia cosmológica."""
        ),
    ]

    # 🌟 Carrusel lateral
    carrusel = QStackedWidget()

    # Efecto de transición (desvanecido)
    opacity = QGraphicsOpacityEffect()
    carrusel.setGraphicsEffect(opacity)

    anim = QPropertyAnimation(opacity, b"opacity")
    anim.setDuration(300)
    anim.setStartValue(0.0)
    anim.setEndValue(1.0)

    # Crear imágenes
    labels = []
    for ruta, texto in imagenes:
        lbl = QLabel()
        lbl.setPixmap(QPixmap(ruta).scaled(450, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        lbl.setAlignment(Qt.AlignCenter)
        lbl.info_text = texto

        # Al hacer clic en la imagen → actualizar texto
        lbl.mousePressEvent = lambda _, l=lbl: texto_info.setText(l.info_text)

        labels.append(lbl)
        carrusel.addWidget(lbl)

    # Botones flecha
    btn_left = QPushButton("⟵")
    btn_left.setFixedSize(50, 50)
    btn_left.setStyleSheet("background-color: rgba(0,0,0,0.5); color: white; font-size: 20px; border-radius: 10px;")

    btn_right = QPushButton("⟶")
    btn_right.setFixedSize(50, 50)
    btn_right.setStyleSheet("background-color: rgba(0,0,0,0.5); color: white; font-size: 20px; border-radius: 10px;")

    # Funciones de navegación
    def ir_izquierda():
        carrusel.setCurrentIndex((carrusel.currentIndex() - 1) % carrusel.count())
        texto_info.setText("")  # Espera clic
        anim.start()

    def ir_derecha():
        carrusel.setCurrentIndex((carrusel.currentIndex() + 1) % carrusel.count())
        texto_info.setText("")
        anim.start()

    btn_left.clicked.connect(ir_izquierda)
    btn_right.clicked.connect(ir_derecha)

    # Layout lateral del carrusel
    layout_carrusel = QVBoxLayout()
    layout_carrusel.addWidget(carrusel)

    botones = QHBoxLayout()
    botones.addWidget(btn_left)
    botones.addWidget(btn_right)
    layout_carrusel.addLayout(botones)

    # Layout horizontal: Carrusel | Texto
    layout_horizontal = QHBoxLayout()
    layout_horizontal.addLayout(layout_carrusel, 40)
    layout_horizontal.addWidget(texto_info, 60)

    # Armado final
    layout_principal.addWidget(titulo)
    layout_principal.addLayout(layout_horizontal)
    layout_principal.addStretch()

    return pagina
