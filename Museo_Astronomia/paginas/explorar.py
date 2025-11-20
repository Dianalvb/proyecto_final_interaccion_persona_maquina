from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QPushButton, QMessageBox, QGraphicsOpacityEffect
from PySide6.QtCore import Qt, QPropertyAnimation, QTimer
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
        self.bloqueado = False  # Para evitar múltiples clicks durante animaciones
        
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
        self.bloqueado = False
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
            
            # Configurar animación más eficiente
            self.configurar_animacion(boton)
            
            # Conexión corregida
            boton.clicked.connect(lambda checked, b=boton: self.voltear_carta(b))
            
            fila = i // 4
            columna = i % 4
            self.grid_layout.addWidget(boton, fila, columna)
            self.cartas.append(boton)
    
    def configurar_animacion(self, boton):
        # Usar una sola animación en lugar de dos
        efecto = QGraphicsOpacityEffect(boton)
        boton.setGraphicsEffect(efecto)
        
        anim = QPropertyAnimation(efecto, b"opacity", boton)
        anim.setDuration(300)
        
        def iniciar_animacion_volteo():
            if not boton.volteada and not boton.emparejada:
                # Animación para voltear (mostrar frente)
                anim.setStartValue(1.0)
                anim.setEndValue(0.0)
                anim.finished.connect(lambda: self.cambiar_imagen_volteo(boton, True))
            else:
                # Animación para devolver (mostrar reverso)
                anim.setStartValue(1.0)
                anim.setEndValue(0.0)
                anim.finished.connect(lambda: self.cambiar_imagen_volteo(boton, False))
            
            anim.start()
        
        boton.iniciar_animacion_volteo = iniciar_animacion_volteo
        boton.anim = anim
    
    def cambiar_imagen_volteo(self, boton, mostrar_frente):
        # Cambiar la imagen cuando la animación de desvanecimiento termina
        if mostrar_frente:
            boton.setIcon(QIcon(boton.imagen_frente))
        else:
            boton.setIcon(QIcon("Museo_Astronomia/reverse.jpg"))
        
        # Animación para reaparecer
        efecto = boton.graphicsEffect()
        anim_reaparecer = QPropertyAnimation(efecto, b"opacity", boton)
        anim_reaparecer.setDuration(300)
        anim_reaparecer.setStartValue(0.0)
        anim_reaparecer.setEndValue(1.0)
        
        # Si estamos ocultando cartas que no son pareja, actualizar estado después de la animación
        if not mostrar_frente:
            anim_reaparecer.finished.connect(lambda: self.finalizar_ocultacion(boton))
        
        anim_reaparecer.start()
    
    def finalizar_ocultacion(self, boton):
        # Solo se llama cuando terminamos de ocultar una carta
        boton.volteada = False
        # Verificar si todas las animaciones de ocultación han terminado
        if all(not carta.volteada for carta in self.cartas_volteadas):
            self.cartas_volteadas.clear()
            self.bloqueado = False
    
    def voltear_carta(self, carta):
        # Validaciones más estrictas
        if (self.bloqueado or carta.volteada or carta.emparejada or 
            len(self.cartas_volteadas) >= 2):
            return
        
        # Bloquear interacción durante la animación
        if len(self.cartas_volteadas) == 0:
            self.bloqueado = True
        
        # Voltear carta
        carta.iniciar_animacion_volteo()
        carta.volteada = True
        self.cartas_volteadas.append(carta)
        
        # Verificar si hay dos cartas volteadas
        if len(self.cartas_volteadas) == 2:
            self.intentos += 1
            self.actualizar_contador()
            
            # Pequeño delay antes de verificar para que se complete la animación
            QTimer.singleShot(350, self.verificar_pareja)
    
    def verificar_pareja(self):
        if len(self.cartas_volteadas) != 2:
            return
            
        carta1, carta2 = self.cartas_volteadas
        
        if carta1.imagen_frente == carta2.imagen_frente:
            # ¡Es pareja!
            carta1.emparejada = True
            carta2.emparejada = True
            self.cartas_volteadas.clear()
            self.parejas_encontradas += 1
            self.bloqueado = False
            
            # Verificar si ganó
            if self.parejas_encontradas == len(self.cartas) // 2:
                QTimer.singleShot(500, self.mostrar_mensaje_ganador)
        else:
            # No es pareja, ocultar después de un tiempo
            self.temporizador.start(1000)  # 1 segundo para ver las cartas
    
    def ocultar_cartas(self):
        # Ocultar todas las cartas volteadas que no son pareja
        for carta in self.cartas_volteadas:
            if not carta.emparejada:
                carta.iniciar_animacion_volteo()  # Esto mostrará el reverso
    
    def mostrar_mensaje_ganador(self):
        QMessageBox.information(self, "¡Felicidades!", 
            f"¡Completaste el memorama en {self.intentos} intentos!")
    
    def actualizar_contador(self):
        self.contador.setText(f"Intentos: {self.intentos} - Parejas: {self.parejas_encontradas}/{len(self.cartas)//2}")
    
    def reiniciar_juego(self):
        self.crear_memorama()

def crear_pagina_explorar(parent=None):
    return MemoramaApp(parent)