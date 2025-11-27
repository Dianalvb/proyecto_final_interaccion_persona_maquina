from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton,
    QStackedWidget, QScrollArea, QGraphicsOpacityEffect
)
from PySide6.QtCore import Qt, QPropertyAnimation
from PySide6.QtGui import QPixmap


def crear_pagina_galeria(parent=None):
    # --------- CONTENEDOR PRINCIPAL ---------
    pagina = QWidget(parent)
    layout_pagina = QVBoxLayout(pagina)

    pagina.setStyleSheet("""
        QWidget {
            background: qlineargradient(
                spread:pad, x1:0, y1:0, x2:0, y2:1,
                stop:0 #f9f9f9,
                stop:1 #ececec
            );
        }
    """)

    # --------- SCROLL GENERAL ---------
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setStyleSheet("background: transparent; border: none;")

    contenedor = QWidget()
    layout_contenedor = QVBoxLayout(contenedor)

    # --------- TÍTULO PRINCIPAL ---------
    titulo = QLabel("Conoce el Cosmos")
    titulo.setAlignment(Qt.AlignCenter)
    titulo.setStyleSheet("""
        color: #2b2b2b;
        font-size: 48px;
        font-family: 'Times New Roman';
        font-weight: bold;
        margin-top: 20px;
    """)
    layout_contenedor.addWidget(titulo)

    # --------- TEXTO PRINCIPAL A LA IZQUIERDA ---------
    texto_info = QLabel("")
    texto_info.setWordWrap(True)
    texto_info.setAlignment(Qt.AlignTop)
    texto_info.setStyleSheet("""
        color: #333333;
        font-size: 22px;
        line-height: 1.4em;
        font-family: 'Times New Roman';
        padding-right: 15px;
    """)

    # --------- TEXTO MUSEOGRÁFICO ÚNICO ---------
    texto_museo = (
        "El universo es un espacio vasto y complejo que alberga fenómenos extraordinarios. "
        "Las nebulosas, galaxias espirales y restos de supernovas son algunos de los elementos "
        "que conforman la estructura cósmica que observamos hoy en día. Cada imagen que verás "
        "en esta galería representa un fragmento de la inmensidad del cosmos.\n\n"

        "Las nebulosas, compuestas por gas y polvo interestelar, son las cunas donde nacen "
        "nuevas estrellas. Por otro lado, las galaxias espirales muestran brazos llenos de vida "
        "y actividad estelar. Los restos de supernovas, como la Nebulosa del Cangrejo, revelan "
        "los procesos explosivos que forjan los elementos del universo. Observar estas imágenes "
        "nos permite comprender mejor nuestro origen y el funcionamiento de la naturaleza cósmica."
    )

    # --------- IMÁGENES ---------
    imagenes = [
        "Museo_Astronomia/museo_astronomía1.jpg",
        "Museo_Astronomia/museo_astronomia2.jpg",
        "Museo_Astronomia/museo_astronomia3.jpg",
        "Museo_Astronomia/museo_astronomia3.jpg"
    ]

    # --------- CARRUSEL ---------
    carrusel = QStackedWidget()

    opacity = QGraphicsOpacityEffect()
    carrusel.setGraphicsEffect(opacity)

    anim = QPropertyAnimation(opacity, b"opacity")
    anim.setDuration(300)
    anim.setStartValue(0.0)
    anim.setEndValue(1.0)

    def estilizar_imagen(ruta):
        pixmap = QPixmap(ruta).scaled(
            560, 360,
            Qt.IgnoreAspectRatio,
            Qt.SmoothTransformation
        )
        return pixmap

    for ruta in imagenes:
        lbl = QLabel()
        lbl.setPixmap(estilizar_imagen(ruta))
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setStyleSheet("""
            QLabel {
                border-radius: 10px;
                border: 3px solid #d0d0d0;
            }
        """)
        carrusel.addWidget(lbl)

    # --------- ACTUALIZAR TEXTO ---------
    def actualizar_texto():
        texto_info.setText(texto_museo)
        anim.start()

    actualizar_texto()

    # --------- BOTONES DE CARRUSEL ---------
    btn_left = QPushButton("⟵")
    btn_right = QPushButton("⟶")

    for b in (btn_left, btn_right):
        b.setFixedSize(60, 52)
        b.setStyleSheet("""
            QPushButton {
                background-color: #e4e4e4;
                color: #333;
                font-size: 22px;
                border-radius: 10px;
                font-family: 'Times New Roman';
            }
            QPushButton:hover {
                background-color: #d2d2d2;
            }
        """)

    btn_left.clicked.connect(lambda: (
        carrusel.setCurrentIndex((carrusel.currentIndex() - 1) % carrusel.count()),
        actualizar_texto()
    ))
    btn_right.clicked.connect(lambda: (
        carrusel.setCurrentIndex((carrusel.currentIndex() + 1) % carrusel.count()),
        actualizar_texto()
    ))

    # --------- LAYOUT CARRUSEL DERECHA ---------
    layout_carrusel = QVBoxLayout()
    layout_botones = QHBoxLayout()
    layout_botones.addWidget(btn_left)
    layout_botones.addWidget(btn_right)

    layout_carrusel.addWidget(carrusel)
    layout_carrusel.addLayout(layout_botones)

    # --------- LAYOUT IZQ (TEXTO) — DER (CARRUSEL) ---------
    layout_horizontal = QHBoxLayout()
    layout_horizontal.addWidget(texto_info, 60)
    layout_horizontal.addLayout(layout_carrusel, 40)

    layout_contenedor.addLayout(layout_horizontal)

    # --------- INFORMACIÓN ADICIONAL ---------
    info_extra = QLabel("""
    <h2 style='color:#2f2f2f; font-size:32px; font-family:Times New Roman;'>
        Información adicional
    </h2>
    <p style='color:#444; font-size:20px; font-family:Times New Roman;'>
        La astronomía moderna utiliza telescopios espaciales, espectroscopía y modelado
        computacional para estudiar objetos situados a millones de años luz. Esta galería
        es una invitación a reflexionar sobre la grandeza del universo y nuestro lugar en él.
    </p>
    """)
    info_extra.setWordWrap(True)
    layout_contenedor.addSpacing(40)
    layout_contenedor.addWidget(info_extra)

    scroll.setWidget(contenedor)
    layout_pagina.addWidget(scroll)

    return pagina
