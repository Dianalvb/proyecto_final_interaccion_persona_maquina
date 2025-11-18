from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea, 
    QFrame, QPushButton, QTextEdit, QLineEdit
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
import os


def crear_pagina_feedback(parent=None):
    pagina = QWidget(parent)
    layout_principal = QVBoxLayout(pagina)
    layout_principal.setContentsMargins(0, 0, 0, 0)
    layout_principal.setSpacing(0)

    # Área de scroll para contenido
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    scroll.setStyleSheet("border: none;")

    contenedor_scroll = QWidget()
    layout_scroll = QVBoxLayout(contenedor_scroll)
    layout_scroll.setContentsMargins(0, 0, 0, 0)
    layout_scroll.setSpacing(0)

    # 🎨 Encabezado
    header = QLabel("💬 Feedback y Opiniones")
    header.setAlignment(Qt.AlignCenter)
    header.setStyleSheet("""
        QLabel {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #1a1a2e, stop:1 #16213e);
            color: white;
            font-size: 32px;
            font-weight: bold;
            padding: 40px 20px;
            margin: 0px;
        }
    """)
    header.setFont(QFont("Arial", 24, QFont.Bold))
    layout_scroll.addWidget(header)

    # 📝 Contenido principal
    contenido_frame = QFrame()
    contenido_frame.setStyleSheet("""
        QFrame {
            background-color: #f8f9fa;
            padding: 0px;
        }
    """)
    contenido_layout = QVBoxLayout(contenido_frame)
    contenido_layout.setSpacing(30)
    contenido_layout.setContentsMargins(40, 40, 40, 40)

    # 📋 Formulario de feedback
    formulario_frame = QFrame()
    formulario_frame.setStyleSheet("""
        QFrame {
            background-color: white;
            border-radius: 15px;
            padding: 30px;
            border: 2px solid #e0e0e0;
        }
    """)
    formulario_layout = QVBoxLayout(formulario_frame)
    formulario_layout.setSpacing(20)

    # Título del formulario
    titulo_form = QLabel("Comparte tu experiencia")
    titulo_form.setStyleSheet("""
        QLabel {
            color: #293170;
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 10px;
        }
    """)
    formulario_layout.addWidget(titulo_form)

    # Subtítulo
    subtitulo = QLabel("Esta sección es solo para feedback - Tu opinión nos ayuda a mejorar")
    subtitulo.setStyleSheet("""
        QLabel {
            color: #666;
            font-size: 16px;
            text-align: center;
            margin-bottom: 20px;
        }
    """)
    subtitulo.setAlignment(Qt.AlignCenter)
    formulario_layout.addWidget(subtitulo)

    # 🔸 Campo de nombre
    nombre_layout = QVBoxLayout()
    nombre_layout.setSpacing(5)
    
    label_nombre = QLabel("Nombre (opcional):")
    label_nombre.setStyleSheet("color: #333; font-size: 14px; font-weight: bold;")
    nombre_layout.addWidget(label_nombre)
    
    input_nombre = QLineEdit()
    input_nombre.setPlaceholderText("Ingresa tu nombre")
    input_nombre.setStyleSheet("""
        QLineEdit {
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 14px;
            background-color: #fafafa;
        }
        QLineEdit:focus {
            border-color: #8a2be2;
            background-color: white;
        }
    """)
    nombre_layout.addWidget(input_nombre)
    formulario_layout.addLayout(nombre_layout)

    # ⭐ Calificación
    calificacion_layout = QVBoxLayout()
    calificacion_layout.setSpacing(10)
    
    label_calificacion = QLabel("Calificación:")
    label_calificacion.setStyleSheet("color: #333; font-size: 14px; font-weight: bold;")
    calificacion_layout.addWidget(label_calificacion)
    
    # Estrellas
    estrellas_frame = QFrame()
    estrellas_layout = QHBoxLayout(estrellas_frame)
    estrellas_layout.setAlignment(Qt.AlignCenter)
    estrellas_layout.setSpacing(5)
    
    # Crear 5 estrellas
    for i in range(5):
        estrella = QLabel("⭐")
        estrella.setStyleSheet("font-size: 24px;")
        estrellas_layout.addWidget(estrella)
    
    calificacion_layout.addWidget(estrellas_frame)
    formulario_layout.addLayout(calificacion_layout)

    # 💬 Comentarios
    comentarios_layout = QVBoxLayout()
    comentarios_layout.setSpacing(5)
    
    label_comentarios = QLabel("Tu comentario:")
    label_comentarios.setStyleSheet("color: #333; font-size: 14px; font-weight: bold;")
    comentarios_layout.addWidget(label_comentarios)
    
    area_comentarios = QTextEdit()
    area_comentarios.setPlaceholderText("Escribe tu feedback, sugerencias o comentarios sobre tu experiencia en el museo...")
    area_comentarios.setMinimumHeight(150)
    area_comentarios.setStyleSheet("""
        QTextEdit {
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 14px;
            background-color: #fafafa;
        }
        QTextEdit:focus {
            border-color: #8a2be2;
            background-color: white;
        }
    """)
    comentarios_layout.addWidget(area_comentarios)
    formulario_layout.addLayout(comentarios_layout)

    # 📤 Botón enviar
    btn_enviar = QPushButton("📤 Enviar Feedback")
    btn_enviar.setStyleSheet("""
        QPushButton {
            background-color: #8a2be2;
            color: white;
            font-size: 16px;
            font-weight: bold;
            padding: 15px 30px;
            border: none;
            border-radius: 25px;
            margin-top: 10px;
        }
        QPushButton:hover {
            background-color: #7a1ad2;
        }
        QPushButton:pressed {
            background-color: #6a0ac2;
        }
    """)
    btn_enviar.setCursor(Qt.PointingHandCursor)
    formulario_layout.addWidget(btn_enviar)

    # Conectar función al botón enviar
    def enviar_feedback():
        nombre = input_nombre.text()
        comentario = area_comentarios.toPlainText()
        
        if comentario.strip():
            print(f"Feedback recibido:")
            print(f"Nombre: {nombre if nombre else 'Anónimo'}")
            print(f"Comentario: {comentario}")
            
            # Limpiar campos después de enviar
            input_nombre.clear()
            area_comentarios.clear()
            
            # Mostrar mensaje de confirmación
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.information(pagina, "Feedback Enviado", 
                                  "¡Gracias por tu feedback! Tu opinión es muy valiosa para nosotros.")
        else:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(pagina, "Campo Vacío", 
                              "Por favor, escribe tu comentario antes de enviar.")

    btn_enviar.clicked.connect(enviar_feedback)

    contenido_layout.addWidget(formulario_frame)

    # 🔙 Botón para volver
    btn_volver_frame = QFrame()
    btn_volver_frame.setStyleSheet("background-color: transparent;")
    btn_volver_layout = QHBoxLayout(btn_volver_frame)
    btn_volver_layout.setAlignment(Qt.AlignCenter)
    
    btn_volver = QPushButton("← Volver al Inicio")
    btn_volver.setStyleSheet("""
        QPushButton {
            background-color: #6c757d;
            color: white;
            font-size: 14px;
            padding: 10px 20px;
            border: none;
            border-radius: 20px;
        }
        QPushButton:hover {
            background-color: #5a6268;
        }
    """)
    btn_volver.setCursor(Qt.PointingHandCursor)
    btn_volver_layout.addWidget(btn_volver)
    contenido_layout.addWidget(btn_volver_frame)

    # Conectar botón volver
    if parent and hasattr(parent, 'mostrar_pagina'):
        btn_volver.clicked.connect(lambda: parent.mostrar_pagina("Inicio"))

    layout_scroll.addWidget(contenido_frame)
    layout_scroll.addStretch()

    contenedor_scroll.setLayout(layout_scroll)
    scroll.setWidget(contenedor_scroll)
    layout_principal.addWidget(scroll)

    return pagina