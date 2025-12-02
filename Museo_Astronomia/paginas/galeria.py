from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton,
    QStackedWidget, QScrollArea, QGraphicsOpacityEffect
)
from PySide6.QtCore import Qt, QPropertyAnimation
from PySide6.QtGui import QPixmap
import os


# ------------------------------------------------------
# Función para obtener la ruta de las imágenes
# ------------------------------------------------------
def ruta(nombre):
    return os.path.join(os.path.dirname(__file__), nombre)


# ------------------------------------------------------
# Función principal para crear la página de galería
# ------------------------------------------------------
def crear_pagina_galeria(parent=None):
    pagina = QWidget(parent)
    layout_principal = QVBoxLayout(pagina)
    layout_principal.setContentsMargins(0, 0, 0, 0)

    # --------- SCROLL PRINCIPAL ---------
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setStyleSheet("background: white; border: none;")
    contenedor = QWidget()
    layout_contenedor = QVBoxLayout(contenedor)
    layout_contenedor.setContentsMargins(20, 20, 20, 20)
    layout_contenedor.setSpacing(25)

    # --------- PORTADA ---------
    portada = QLabel()
    px_portada = QPixmap(ruta("reverso.png"))
    if not px_portada.isNull():
        portada.setPixmap(px_portada.scaledToWidth(1400, Qt.SmoothTransformation))
        portada.setAlignment(Qt.AlignCenter)
    else:
        portada.setText("reverso.png no encontrado")
        portada.setStyleSheet("font-size: 26px; color: #333; padding: 40px;")
    layout_contenedor.addWidget(portada)

    # --------- TÍTULO Y SUBTÍTULO ---------
    titulo = QLabel("Conoce el Cosmos")
    titulo.setAlignment(Qt.AlignCenter)
    titulo.setStyleSheet("""
        color: #1a1a1a;
        font-size: 48px;
        font-family: 'Times New Roman';
        font-weight: bold;
    """)
    layout_contenedor.addWidget(titulo)

    subtitulo = QLabel("Explora maravillas capturadas por telescopios espaciales")
    subtitulo.setAlignment(Qt.AlignCenter)
    subtitulo.setStyleSheet("""
        color: #333;
        font-size: 24px;
        font-family: 'Times New Roman';
    """)
    layout_contenedor.addWidget(subtitulo)

    # --------- TEXTO INFORMATIVO ---------
    texto_info = QLabel("")
    texto_info.setWordWrap(True)
    texto_info.setAlignment(Qt.AlignTop)
    texto_info.setStyleSheet("""
        color: #222;
        font-size: 22px;
        line-height: 1.4em;
        font-family: 'Times New Roman';
        padding-left: 20px;
    """)

    # --------- DATOS DEL CARRUSEL ---------
    datos = [
        ("NGC 3603", ruta("NGC_3603.png"),
         "Este cúmulo estelar enorme está rodeado por nubes de gas y polvo interestelar."),
        ("NGC 4689", ruta("NGC_4689.png"),
         "Galaxia espiral situada a 54 millones de años luz."),
        ("ACO S 295", ruta("ACO_S.png"),
         "Cúmulo de galaxias que produce efecto de lente gravitacional."),
        ("Monkey’s Head Nebula", ruta("Monkey.jpeg"),
         "Nebulosa de intensa formación estelar esculpida por radiación UV."),
        ("Messier 94", ruta("Messier_94.jpeg"),
         "Galaxia espiral con un anillo de brote estelar."),
        ("NGC 1850", ruta("NGC_1850.png"),
         "Cúmulo globular joven en la Gran Nube de Magallanes.")
    ]

    # --------- CARRUSEL ---------
    carrusel = QStackedWidget()
    carrusel.setMaximumWidth(800)   # ancho máximo
    carrusel.setMaximumHeight(500)  # altura reducida
    opacity = QGraphicsOpacityEffect()
    carrusel.setGraphicsEffect(opacity)
    anim = QPropertyAnimation(opacity, b"opacity")
    anim.setDuration(350)
    anim.setStartValue(0.0)
    anim.setEndValue(1.0)

    # Agregar imágenes al carrusel
    for nombre, ruta_img, _ in datos:
        lbl = QLabel()
        pix = QPixmap(ruta_img)
        lbl.setPixmap(pix)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setScaledContents(True)  # Imagen se ajusta al tamaño del QLabel
        lbl.setStyleSheet("""
            QLabel {
                border-radius: 12px;
                border: 3px solid #cccccc;
            }
        """)
        carrusel.addWidget(lbl)

    # Función para actualizar texto
    def actualizar_texto():
        nombre, _, descripcion = datos[carrusel.currentIndex()]
        texto_info.setText(f"<b style='font-size:26px'>{nombre}</b><br><br>{descripcion}")
        anim.start()

    actualizar_texto()

    # --------- BOTONES DEL CARRUSEL ---------
    btn_left = QPushButton("⟵")
    btn_right = QPushButton("⟶")
    for b in (btn_left, btn_right):
        b.setFixedSize(65, 55)
        b.setStyleSheet("""
            QPushButton {
                background-color: #ebebeb;
                color: #333;
                font-size: 26px;
                border-radius: 10px;
                font-family: 'Times New Roman';
            }
            QPushButton:hover { background-color: #dcdcdc; }
        """)
    btn_left.clicked.connect(lambda: (carrusel.setCurrentIndex((carrusel.currentIndex() - 1) % carrusel.count()),
                                     actualizar_texto()))
    btn_right.clicked.connect(lambda: (carrusel.setCurrentIndex((carrusel.currentIndex() + 1) % carrusel.count()),
                                      actualizar_texto()))

    layout_botones = QHBoxLayout()
    layout_botones.addWidget(btn_left)
    layout_botones.addWidget(btn_right)

    layout_carrusel = QVBoxLayout()
    layout_carrusel.addWidget(carrusel)
    layout_carrusel.addLayout(layout_botones)

    # --------- Layout horizontal: carrusel a la izquierda, texto a la derecha ---------
    layout_horizontal = QHBoxLayout()
    layout_horizontal.addLayout(layout_carrusel, 50)  # 50% ancho
    layout_horizontal.addWidget(texto_info, 50)       # 50% ancho

    layout_contenedor.addLayout(layout_horizontal)

    # --------- INFORMACIÓN ADICIONAL ---------
    info_extra = QLabel("""
    <h2 style='color:#1a1a1a; font-size:32px; font-family:Times New Roman;'>
        Información adicional
    </h2>
    <p style='color:#333; font-size:20px; font-family:Times New Roman;'>
        La astronomía moderna utiliza telescopios espaciales, espectroscopía y modelado
        computacional para comprender objetos a millones de años luz. Esta galería es una
        invitación a reflexionar sobre la grandeza del universo y nuestro lugar en él.
    </p>
    """)
    info_extra.setWordWrap(True)
    layout_contenedor.addSpacing(40)
    layout_contenedor.addWidget(info_extra)

    scroll.setWidget(contenedor)
    layout_principal.addWidget(scroll)

    return pagina
