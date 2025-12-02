from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea, QFrame,
    QFormLayout, QLineEdit, QComboBox, QCheckBox,
    QRadioButton, QButtonGroup, QPushButton, QMessageBox
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsDropShadowEffect
import os


def crear_pagina_tickets(parent=None):

    pagina = QWidget()
    layout_principal = QVBoxLayout(pagina)
    layout_principal.setContentsMargins(0, 0, 0, 0)

    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    contenedor = QWidget()
    contenido = QVBoxLayout(contenedor)
    contenido.setContentsMargins(0, 0, 0, 0)

    # ------------------------------------------------------
    # PORTADA
    # ------------------------------------------------------
    portada = QLabel()
    ruta_portada = os.path.join(os.path.dirname(__file__), "horizontes.png")
    px = QPixmap(ruta_portada)

    if not px.isNull():
        portada.setPixmap(px.scaledToWidth(1400, Qt.SmoothTransformation))
    else:
        portada.setText("ticket.png no encontrado")
        portada.setStyleSheet("font-size: 26px; color: #333; padding: 40px;")

    contenido.addWidget(portada)

    # ------------------------------------------------------
    # TITULO Y DESCRIPCION
    # ------------------------------------------------------
    titulo = QLabel("Compra de Entradas – Museo de Astronomía")
    titulo.setStyleSheet("""
        color: #2e2e2e;
        font-size: 38px;
        font-family: 'Times New Roman';
        font-weight: bold;
        margin-left: 40px;
        margin-top: 25px;
    """)

    descripcion = QLabel(
        "Selecciona tu tipo de entrada, cantidad y servicios adicionales."
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

    # ------------------------------------------------------
    # TARJETA DEL FORMULARIO
    # ------------------------------------------------------
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

    # CAMPOS ----------------------------------------------
    nombre = QLineEdit()
    nombre.setPlaceholderText("Tu nombre completo")

    boletos = QComboBox()
    boletos.addItems([
        "Entrada general – $120",
        "Entrada nocturna – $150",
        "Pase anual – $700",
        "Entrada infantil – $80"
    ])

    # Cantidad de boletos
    cantidad = QComboBox()
    cantidad.addItems(["1", "2", "3", "4", "5"])

    # Extras
    extra1 = QCheckBox("Visita guiada por astrónomo (+$50)")
    extra2 = QCheckBox("Acceso al telescopio solar (+$30)")
    extra3 = QCheckBox("Audioguía digital (+$25)")

    # Método de pago
    pago_label = QLabel("Método de pago")
    rb1 = QRadioButton("Tarjeta")
    rb2 = QRadioButton("Efectivo")
    rb3 = QRadioButton("Pago digital")

    grupo = QButtonGroup(card)
    grupo.addButton(rb1)
    grupo.addButton(rb2)
    grupo.addButton(rb3)

    # Botones
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

    # ------------------------------------------------------
    # AGREGAR ELEMENTOS AL FORM
    # ------------------------------------------------------
    card_layout.addRow("Nombre:", nombre)
    card_layout.addRow("Tipo de entrada:", boletos)
    card_layout.addRow("Cantidad:", cantidad)
    card_layout.addRow(extra1)
    card_layout.addRow(extra2)
    card_layout.addRow(extra3)
    card_layout.addRow(pago_label)
    card_layout.addWidget(rb1)
    card_layout.addWidget(rb2)
    card_layout.addWidget(rb3)
    card_layout.addRow(btn_comprar, btn_cancelar)

    contenido.addWidget(card, alignment=Qt.AlignCenter)

    # ------------------------------------------------------
    # FUNCIÓN DE RESUMEN Y TOTAL
    # ------------------------------------------------------
    def mostrar_resumen():

        # Precios base
        precios = {
            "Entrada general – $120": 120,
            "Entrada nocturna – $150": 150,
            "Pase anual – $700": 700,
            "Entrada infantil – $80": 80
        }

        tipo = boletos.currentText()
        cant = int(cantidad.currentText())
        total = precios[tipo] * cant

        # Extras
        if extra1.isChecked(): total += 50
        if extra2.isChecked(): total += 30
        if extra3.isChecked(): total += 25

        # Crear mensaje
        mensaje = f"""
Nombre: {nombre.text()}
Entrada: {tipo}
Cantidad: {cant}

Extras:
 - Visita guiada: {"Sí" if extra1.isChecked() else "No"}
 - Telescopio solar: {"Sí" if extra2.isChecked() else "No"}
 - Audioguía digital: {"Sí" if extra3.isChecked() else "No"}

TOTAL A PAGAR: ${total}

✨ ¡Muchas gracias por tu compra, te esperamos pronto! ✨
"""

        box = QMessageBox()
        box.setWindowTitle("Resumen de compra")
        box.setText(mensaje)
        box.setStandardButtons(QMessageBox.Ok)
        box.exec()

    # Conectar botón
    btn_comprar.clicked.connect(mostrar_resumen)

    # ------------------------------------------------------
    scroll.setWidget(contenedor)
    layout_principal.addWidget(scroll)

    return pagina
