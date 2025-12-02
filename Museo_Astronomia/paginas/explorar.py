from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QPushButton, QMessageBox
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QIcon, QPalette, QBrush
import os
import random
from functools import partial


# ----------------------------------------------------------
# RUTA ABSOLUTA DEL ARCHIVO (SOLUCIÓN DEFINITIVA)
# ----------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def ruta(nombre_archivo):
    """Devuelve la ruta absoluta del archivo, sin importar desde dónde se ejecute."""
    return os.path.join(BASE_DIR, nombre_archivo)


# ----------------------------------------------------------
# PRUEBAS PARA VER SI LAS IMÁGENES EXISTEN
# ----------------------------------------------------------
print("---- PRUEBA DE ARCHIVOS ----")
imagenes_prueba = [
    "ACO_S.png",
    "Messier_94.jpeg",
    "Monkey.jpeg",
    "NGC_1850.png",
    "NGC_3603.png",
    "NGC_4689.png",
    "reverso.png",
    "fondo.png"
]

for archivo in imagenes_prueba:
    print(archivo, "->", os.path.exists(ruta(archivo)))
print("----------------------------")


# ----------------------------------------------------------
# CLASE DE CADA CARTA
# ----------------------------------------------------------
class CartaMemorama(QPushButton):
    def __init__(self, imagen_frente, imagen_reverso):
        super().__init__()

        self.imagen_frente = imagen_frente
        self.imagen_reverso = imagen_reverso

        self.volteada = False
        self.emparejada = False

        self.setFixedSize(130, 130)

        self.setStyleSheet("""
            QPushButton {
                background-color: #0b0f26;
                border-radius: 18px;
                border: 3px solid #4a68ff;
                padding: 0px;
                margin: 0px;
            }
            QPushButton:hover {
                border: 3px solid #7ea0ff;
            }
        """)

        self.setIcon(QIcon(self.imagen_reverso))
        self.setIconSize(self.size())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.setIconSize(self.size())

    def mostrar_frente(self):
        self.setIcon(QIcon(self.imagen_frente))
        self.setIconSize(self.size())
        self.volteada = True

    def mostrar_reverso(self):
        self.setIcon(QIcon(self.imagen_reverso))
        self.setIconSize(self.size())
        self.volteada = False


# ----------------------------------------------------------
# CLASE PRINCIPAL DEL MEMORAMA
# ----------------------------------------------------------
class MemoramaApp(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.cartas_volteadas = []
        self.parejas_encontradas = 0
        self.intentos = 0
        self.bloqueado = False

        self.temporizador = QTimer()
        self.temporizador.setSingleShot(True)
        self.temporizador.timeout.connect(self.ocultar_cartas)

        self.init_ui()

    def init_ui(self):

        # ----------------------------------------------------------
        # FONDO ESPACIAL (FUNCIONAL)
        # ----------------------------------------------------------
        fondo = QPixmap(ruta("fondo.png"))

        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(fondo))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # ----------------------------------------------------------

        layout = QVBoxLayout(self)

        titulo = QLabel("Memorama Astronómico")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            color: #a5baff;
            font-size: 30px;
            font-weight: bold;
        """)

        self.contador = QLabel("Intentos: 0")
        self.contador.setAlignment(Qt.AlignCenter)
        self.contador.setStyleSheet("""
            color: #e0e4ff;
            font-size: 18px;
        """)

        layout.addWidget(titulo)
        layout.addWidget(self.contador)

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(15)
        layout.addLayout(self.grid_layout)

        btn_reiniciar = QPushButton("Reiniciar Juego")
        btn_reiniciar.clicked.connect(self.reiniciar_juego)
        btn_reiniciar.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(btn_reiniciar, alignment=Qt.AlignCenter)

        self.crear_memorama()

    # ----------------------------------------------------------
    def crear_memorama(self):

        while self.grid_layout.count():
            w = self.grid_layout.takeAt(0).widget()
            if w:
                w.deleteLater()

        # Usar imágenes directamente SIN carpeta
        imagenes = [
            ruta("ACO_S.png"),
            ruta("Messier_94.jpeg"),
            ruta("Monkey.jpeg"),
            ruta("NGC_1850.png"),
            ruta("NGC_3603.png"),
            ruta("NGC_4689.png")
        ]

        reverso = ruta("reverso.png")

        cartas = imagenes * 2
        random.shuffle(cartas)

        self.cartas = []
        self.cartas_volteadas = []
        self.parejas_encontradas = 0
        self.intentos = 0
        self.bloqueado = False
        self.actualizar_contador()

        for i, img in enumerate(cartas):
            carta = CartaMemorama(img, reverso)
            carta.clicked.connect(partial(self.voltear_carta, carta))

            self.grid_layout.addWidget(carta, i // 4, i % 4)
            self.cartas.append(carta)

    # ----------------------------------------------------------
    def voltear_carta(self, carta):
        if self.bloqueado or carta.volteada or carta.emparejada:
            return

        carta.mostrar_frente()
        self.cartas_volteadas.append(carta)

        if len(self.cartas_volteadas) == 2:
            self.intentos += 1
            self.actualizar_contador()
            self.bloqueado = True
            QTimer.singleShot(300, self.verificar_pareja)

    # ----------------------------------------------------------
    def verificar_pareja(self):
        c1, c2 = self.cartas_volteadas

        if c1.imagen_frente == c2.imagen_frente:
            c1.emparejada = True
            c2.emparejada = True
            self.parejas_encontradas += 1
            self.cartas_volteadas.clear()
            self.bloqueado = False

            if self.parejas_encontradas == len(self.cartas) // 2:
                QMessageBox.information(
                    self, "¡Felicidades!",
                    f"¡Completaste el memorama en {self.intentos} intentos!"
                )
        else:
            self.temporizador.start(600)

    # ----------------------------------------------------------
    def ocultar_cartas(self):
        for c in self.cartas_volteadas:
            if not c.emparejada:
                c.mostrar_reverso()

        self.cartas_volteadas.clear()
        self.bloqueado = False

    # ----------------------------------------------------------
    def actualizar_contador(self):
        self.contador.setText(
            f"Intentos: {self.intentos} | Parejas: {self.parejas_encontradas}/{len(self.cartas)//2}"
        )

    # ----------------------------------------------------------
    def reiniciar_juego(self):
        self.crear_memorama()


# ----------------------------------------------------------
def crear_pagina_explorar(parent=None):
    return MemoramaApp(parent)
