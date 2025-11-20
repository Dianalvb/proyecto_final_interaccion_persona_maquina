from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QPushButton, QMessageBox
from PySide6.QtCore import Qt, QTimer
import random
from functools import partial

class MemoramaApp(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cartas_volteadas = []
        self.parejas_encontradas = 0
        self.intentos = 0
        self.cartas = []
        self.bloqueado = False
        
        self.temporizador = QTimer()
        self.temporizador.setSingleShot(True)
        self.temporizador.timeout.connect(self.ocultar_cartas)
        
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)

        # Título
        titulo = QLabel("Memorama Astronómico ")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            color: #ffffff;
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 10px;
        """)

        # Contador
        self.contador = QLabel("Intentos: 0")
        self.contador.setAlignment(Qt.AlignCenter)
        self.contador.setStyleSheet("""
            color: #cccccc;
            font-size: 18px;
            margin-bottom: 10px;
        """)

        # Grid del memorama
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(10)

        layout.addWidget(titulo)
        layout.addWidget(self.contador)
        layout.addLayout(self.grid_layout)

        # Botón reiniciar
        self.btn_reiniciar = QPushButton("Reiniciar Juego")
        self.btn_reiniciar.setStyleSheet("""
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
        self.btn_reiniciar.clicked.connect(self.reiniciar_juego)
        layout.addWidget(self.btn_reiniciar, alignment=Qt.AlignCenter)

        self.crear_memorama()

    def crear_memorama(self):
        # Limpiar grid
        while self.grid_layout.count():
            item = self.grid_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Memorama con EMOJIS (sin imágenes)
        emojis = ["🌕", "🪐", "☄️", "🌟", "🌌", "🛸"]
        cartas = emojis * 2
        random.shuffle(cartas)

        self.cartas = []
        self.cartas_volteadas = []
        self.parejas_encontradas = 0
        self.intentos = 0
        self.bloqueado = False
        self.actualizar_contador()

        for i, emoji in enumerate(cartas):
            boton = QPushButton("❓")  
            boton.setFixedSize(110, 110)
            boton.setStyleSheet("""
                QPushButton {
                    font-size: 40px;
                    background-color: #222;
                    border: 2px solid #555;
                    border-radius: 15px;
                    color: white;
                }
                QPushButton:hover {
                    border: 2px solid #aaa;
                }
            """)

            boton.texto_frente = emoji
            boton.volteada = False
            boton.emparejada = False

            boton.clicked.connect(partial(self.voltear_carta, boton))

            self.grid_layout.addWidget(boton, i // 4, i % 4)
            self.cartas.append(boton)

    def voltear_carta(self, carta):
        if self.bloqueado or carta.volteada or carta.emparejada:
            return
        
        carta.volteada = True
        carta.setText(carta.texto_frente)
        carta.update()

        self.cartas_volteadas.append(carta)

        if len(self.cartas_volteadas) == 2:
            self.intentos += 1
            self.actualizar_contador()
            self.bloqueado = True
            QTimer.singleShot(300, self.verificar_pareja)

    # SIN efectos / SIN animación
    def animar_volteo(self, carta, mostrar):
        if mostrar:
            carta.setText(carta.texto_frente)
        else:
            carta.setText("❓")
            carta.volteada = False

        carta.update()

    def verificar_pareja(self):
        if len(self.cartas_volteadas) != 2:
            return

        c1, c2 = self.cartas_volteadas

        if c1.texto_frente == c2.texto_frente:
            c1.emparejada = True
            c2.emparejada = True
            self.cartas_volteadas.clear()
            self.bloqueado = False
            self.parejas_encontradas += 1

            if self.parejas_encontradas == len(self.cartas) // 2:
                QTimer.singleShot(200, self.mostrar_mensaje_ganador)

        else:
            self.temporizador.start(400)

    def ocultar_cartas(self):
        for carta in self.cartas_volteadas:
            if not carta.emparejada:
                carta.setText("❓")
                carta.volteada = False
                carta.update()

        self.cartas_volteadas.clear()
        self.bloqueado = False

    def mostrar_mensaje_ganador(self):
        QMessageBox.information(self, "¡Felicidades!",
            f"¡Completaste el memorama en {self.intentos} intentos!")

    def actualizar_contador(self):
        self.contador.setText(
            f"Intentos: {self.intentos}  |  Parejas: {self.parejas_encontradas}/{len(self.cartas)//2}"
        )

    def reiniciar_juego(self):
        self.crear_memorama()


def crear_pagina_explorar(parent=None):
    return MemoramaApp(parent)
