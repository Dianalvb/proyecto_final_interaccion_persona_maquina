from PySide6.QtWidgets import( QWidget, QLabel, QVBoxLayout, QGroupBox, QPushButton, QGridLayout)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap


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
    
    info_label = QLabel("")
    info_label.setAlignment(Qt.AlignCenter)
    info_label.setStyleSheet("""
    color: #ffffff;
    font-size: 16px;
    font-family: 'Segoe UI';
""")

    #columna 1
    boxA= QGroupBox("coleccion 1")
    vA = QVBoxLayout(boxA)
    vA.setSpacing(8)

    btn_imagen1 = QPushButton()
    btn_imagen1.setIcon(QIcon("Museo_Astronomia/museo_astronomía1.jpg"))
    btn_imagen1.setIconSize(QSize(240, 160))  # ajusta al tamaño que quieras
    btn_imagen1.setFixedSize(260, 180)

    vA.addWidget(btn_imagen1)

    #columna 2
    boxB= QGroupBox("coleccion 2")
    vB = QVBoxLayout(boxB)
    vB.setSpacing(8)
    btn_imagen2 = QPushButton()
    btn_imagen2.setIcon(QIcon("Museo_Astronomia/museo_astronomia2.jpg"))
    btn_imagen2.setIconSize(QSize(240, 160))
    btn_imagen2.setFixedSize(260, 180)
    
    vB.addWidget(btn_imagen2)

    #columna 3
    boxC= QGroupBox("coleccion 3")
    vC = QVBoxLayout(boxC)
    vC.setSpacing(8)
    btn_imagen3 = QPushButton()
    btn_imagen3.setIcon(QIcon("Museo_Astronomia/museo_astronomia3.jpg"))
    btn_imagen3.setIconSize(QSize(240, 160))
    btn_imagen3.setFixedSize(260, 180)
    
    vC.addWidget(btn_imagen3)

    #Columna 4
    boxD = QGroupBox("cOLEccion 4")
    vD = QVBoxLayout(boxD)
    vD.setSpacing(8)
    btn_imagen4 = QPushButton()
    btn_imagen4.setIcon(QIcon("Museo_Astronomia/museo_astronomia3.jpg"))
    btn_imagen4.setIconSize(QSize(240, 160))
    btn_imagen4.setFixedSize(260, 180)
    
    vD.addWidget(btn_imagen4)

    grid = QGridLayout()
    grid.addWidget(boxA, 0, 0)
    grid.addWidget(boxB, 0, 1)
    grid.addWidget(boxC, 1, 0)
    grid.addWidget(boxD, 1, 1)
    
    btn_imagen1.clicked.connect(lambda: info_label.setText("Imagenes del sistema solar"))
    btn_imagen2.clicked.connect(lambda: info_label.setText("Fotografías de la galaxia :p"))
    btn_imagen3.clicked.connect(lambda: info_label.setText("Fotografías:p"))
    btn_imagen4.clicked.connect(lambda: info_label.setText("Fotografías"))

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
    layout.addLayout(grid)
    layout.addWidget(info_label)
    layout.addStretch()

    return pagina
