from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QPushButton, QMessageBox
from PySide6.QtCore import Qt, QPropertyAnimation, QTimer,QGraphicsOpacityEffect
from PySide6.QtGui import QIcon
import random

class MemoramaApp(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cartas_volteadas = []
        self.parejas_encontradas = 0
        self.intentos = 0
        self.cartas = []
        self.temporizador = QTimer()
        self.temporizador.setSingleShot(True)
        self.temporizador.timeout.connect(self.ocultar_cartas)
        
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Título
        titulo = QLabel("Memorama Astronómico")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            color: #ffffff;
            font-size: 28px;
            font-weight: bold;
            font-family: 'Segoe UI';
            margin: 20px;
        """)
        
        # Contador de intentos
        self.contador = QLabel("Intentos: 0")
        self.contador.setAlignment(Qt.AlignCenter)
        self.contador.setStyleSheet("""
            color: #cccccc;
            font-size: 18px;
            font-family: 'Segoe UI';
            margin: 10px;
        """)
        
        # Grid para las cartas
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(10)
        self.grid_layout.setContentsMargins(20, 20, 20, 20)
        
        # Botón reiniciar
        btn_reiniciar = QPushButton("Reiniciar Juego")
        btn_reiniciar.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                padding: 10px;
                border: none;
                border-radius: 5px;
                margin: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        btn_reiniciar.clicked.connect(self.reiniciar_juego)
        
        layout.addWidget(titulo)
        layout.addWidget(self.contador)
        layout.addWidget(btn_reiniciar)
        layout.addLayout(self.grid_layout)
        
        self.crear_memorama()
        
    def crear_memorama(self):
        # Limpiar grid
        while self.grid_layout.count():
            child = self.grid_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        # Imágenes
        imagenes = [
            "Museo_Astronomia/museo_astronomía1.jpg",
            "Museo_Astronomia/museo_astronomía2.jpg", 
            "Museo_Astronomia/museo_astronomía3.jpg",
            "Museo_Astronomia/impacto.jpeg",
            "Museo_Astronomia/playera.jpg",
            "Museo_Astronomia/logo.png"
        ]
        
        if len(imagenes) % 2 != 0:
            imagenes = imagenes[:-1]
        
        cartas = imagenes * 2
        random.shuffle(cartas)
        
        self.cartas = []
        self.cartas_volteadas = []
        self.parejas_encontradas = 0
        self.intentos = 0
        self.actualizar_contador()
        
        for i, imagen in enumerate(cartas):
            boton = QPushButton()
            boton.setFixedSize(120, 120)
            boton.setIcon(QIcon("Museo_Astronomia/reverse.jpg"))
            boton.setIconSize(boton.size())
            boton.imagen_frente = imagen
            boton.volteada = False
            boton.emparejada = False
            
            boton.setStyleSheet("""
                QPushButton {
                    border: 2px solid #555;
                    border-radius: 10px;
                    background-color: #2a2a2a;
                }
                QPushButton:hover {
                    border: 2px solid #777;
                }
            """)
            
            self.configurar_animacion(boton)
            
            # 🔥 CORRECCIÓN DEFINITIVA — compatible con cualquier PySide6 🔥
            boton.clicked.connect(lambda *args, b=boton: self.voltear_carta(b))
            
            fila = i // 4
            columna = i % 4
            self.grid_layout.addWidget(boton, fila, columna)
            self.cartas.append(boton)
    
    def configurar_animacion(self, boton):
        efecto = QGraphicsOpacityEffect()
        boton.setGraphicsEffect(efecto)
        
        anim1 = QPropertyAnimation(efecto, b"opacity")
        anim1.setDuration(200)
        anim1.setStartValue(1)
        anim1.setEndValue(0)
        
        anim2 = QPropertyAnimation(efecto, b"opacity")
        anim2.setDuration(200)
        anim2.setStartValue(0)
        anim2.setEndValue(1)
        
        def swap():
            if not boton.volteada and not boton.emparejada:
                boton.setIcon(QIcon(boton.imagen_frente))
            else:
                boton.setIcon(QIcon("Museo_Astronomia/reverse.jpg"))
        
        anim1.finished.connect(swap)
        anim1.finished.connect(anim2.start)
        
        boton.anim1 = anim1
        boton.anim2 = anim2
    
    def voltear_carta(self, carta):
        if (
            carta.volteada or carta.emparejada or 
            len(self.cartas_volteadas) >= 2 or 
            self.temporizador.isActive()
        ):
            return
        
        carta.anim1.start()
        carta.volteada = True
        self.cartas_volteadas.append(carta)
        
        if len(self.cartas_volteadas) == 2:
            self.intentos += 1
            self.actualizar_contador()
            self.verificar_pareja()
    
    def verificar_pareja(self):
        carta1, carta2 = self.cartas_volteadas
        
        if carta1.imagen_frente == carta2.imagen_frente:
            carta1.emparejada = True
            carta2.emparejada = True
            self.cartas_volteadas = []
            self.parejas_encontradas += 1
            
            if self.parejas_encontradas == len(self.cartas) // 2:
                QTimer.singleShot(500, self.mostrar_mensaje_ganador)
        else:
            self.temporizador.start(1000)
    
    def mostrar_mensaje_ganador(self):
        QMessageBox.information(self, "¡Felicidades!", 
            f"¡Completaste el memorama en {self.intentos} intentos!")
    
    def ocultar_cartas(self):
        for carta in self.cartas_volteadas:
            if not carta.emparejada:
                carta.anim1.start()
                carta.volteada = False
        self.cartas_volteadas = []
    
    def actualizar_contador(self):
        self.contador.setText(f"Intentos: {self.intentos} - Parejas: {self.parejas_encontradas}/{len(self.cartas)//2}")
    
    def reiniciar_juego(self):
        self.crear_memorama()

def crear_pagina_explorar(parent=None):
    return MemoramaApp(parent)
