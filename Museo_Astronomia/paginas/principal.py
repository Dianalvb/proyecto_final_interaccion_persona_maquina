from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QScrollArea, QFrame, 
    QPushButton
)
from PySide6.QtCore import Qt, QUrl, QTimer
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtGui import QPixmap
import os


def crear_pagina_principal(parent=None, base_path=".", callback_feedback=None):
    # Forzar el backend correcto en Windows (evita que se pierda el audio)
    os.environ["QT_MEDIA_BACKEND"] = "windows"

    pagina = QWidget(parent)
    layout_principal = QVBoxLayout(pagina)
    layout_principal.setContentsMargins(0, 0, 0, 0)
    layout_principal.setSpacing(0)

    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    contenedor_scroll = QWidget()
    layout_scroll = QVBoxLayout(contenedor_scroll)
    layout_scroll.setContentsMargins(0, 0, 0, 0)
    layout_scroll.setSpacing(0)

    # 🪐 Banner superior con video
    banner = QFrame()
    banner.setMinimumHeight(800)
    banner.setStyleSheet("background-color: black;")

    layout_banner = QVBoxLayout(banner)
    layout_banner.setContentsMargins(0, 0, 0, 0)
    layout_banner.setSpacing(0)

    # 🎞️ Video local
    video_widget = QVideoWidget()
    layout_banner.addWidget(video_widget)

    # 🔊 Player y salida de audio — deben guardarse en 'pagina'
    pagina.player = QMediaPlayer()
    pagina.audio_output = QAudioOutput()
    pagina.audio_output.setVolume(1.0)  # Volumen al 100 %

    # Asignar salida y destino de video
    pagina.player.setAudioOutput(pagina.audio_output)
    pagina.player.setVideoOutput(video_widget)

    # 📂 Ruta del video
    ruta_video = os.path.join(os.path.dirname(__file__), "..", "espacio1.mp4")
    ruta_video = os.path.abspath(ruta_video)
    print("Ruta del video:", ruta_video, "Existe:", os.path.exists(ruta_video))

    pagina.player.setSource(QUrl.fromLocalFile(ruta_video))

    # 🔁 Bucle de 22 segundos
    duracion_ms = 22000
    timer = QTimer(pagina)
    timer.timeout.connect(lambda: pagina.player.setPosition(0))

    def iniciar_video(status):
        if status == QMediaPlayer.MediaStatus.LoadedMedia:
            pagina.player.play()
            timer.start(duracion_ms)

    pagina.player.mediaStatusChanged.connect(iniciar_video)

    # ▶️ Iniciar reproducción
    pagina.player.play()

    # Añadir banner y secciones al scroll
    layout_scroll.addWidget(banner)

    # 🧭 Sección de bienvenida
    bienvenida = QLabel("""
        <h2 style="color:#293170; text-align:center;">Explora el universo</h2>
        <p style="color:#333333; text-align:center; font-size:20px; max-width:900px; margin:auto;">
            Descubre los secretos de las estrellas, planetas y galaxias a través de experiencias interactivas y visuales únicas.
        </p>
    """)
    bienvenida.setAlignment(Qt.AlignCenter)
    bienvenida.setWordWrap(True)
    bienvenida.setStyleSheet("background-color: #f5f5f5; padding: 60px;")
    layout_scroll.addWidget(bienvenida)

    # 🖼️ Imagen e historia del museo (CON SCROLL PROPIO)
    historia_frame = QFrame()
    historia_layout = QVBoxLayout(historia_frame)
    historia_layout.setContentsMargins(0, 0, 0, 0)
    historia_layout.setSpacing(15)
    historia_layout.setAlignment(Qt.AlignCenter)

    # Ruta de la imagen
    ruta_historia = os.path.join(os.path.dirname(__file__), "fuera.png")

    if os.path.exists(ruta_historia):
        imagen_historia = QLabel()
        imagen_pixmap = QPixmap(ruta_historia)
        imagen_pixmap = imagen_pixmap.scaledToWidth(600, Qt.SmoothTransformation)
        imagen_historia.setPixmap(imagen_pixmap)
        imagen_historia.setAlignment(Qt.AlignCenter)
        historia_layout.addWidget(imagen_historia)
    else:
        print("⚠ No se encontró la imagen del museo:", ruta_historia)

    # Texto descriptivo / historia CON SCROLL
    texto_historia_frame = QFrame()
    texto_historia_frame.setStyleSheet("background-color: #fafafa; border-top: 2px solid #ddd;")
    texto_historia_layout = QVBoxLayout(texto_historia_frame)
    
    scroll_historia = QScrollArea()
    scroll_historia.setWidgetResizable(True)
    scroll_historia.setMaximumHeight(300)  # Altura máxima con scroll
    scroll_historia.setStyleSheet("border: none; background-color: transparent;")
    
    texto_historia_contenido = QLabel("""
        <h3 style="color:#293170; text-align:center;">La historia detrás del museo</h3>
        <p style="color:#333333; text-align:justify; font-size:18px; max-width:900px; margin:auto; line-height:1.6;">
            Nuestro museo, recientemente inaugurado, fue creado por la <b>Ingeniera Diana</b>.  
            Gracias a su creatividad y pasión por la astronomía, dio vida a este impresionante espacio 
            dedicado a inspirar a nuevas generaciones de exploradores del universo. 🌌<br><br>
            
            Desde su infancia, la Ingeniera Diana mostró un profundo interés por las estrellas y los misterios 
            del cosmos. Después de años de estudio e investigación, decidió compartir su conocimiento y 
            pasión con el mundo, creando este espacio único donde la ciencia se encuentra con la inspiración.<br><br>
            
            El museo cuenta con exhibiciones interactivas, modelos a escala de planetas y sistemas solares, 
            y una colección única de meteoritos auténticos. Cada sala está diseñada para transportar a los 
            visitantes a través del vasto universo, desde nuestro sistema solar hasta las galaxias más lejanas.<br><br>
            
            Nuestra misión es hacer que la astronomía sea accesible para todos, desde niños curiosos hasta 
            adultos que nunca perdieron su asombro por el cielo nocturno. Creemos que cada persona tiene 
            derecho a maravillarse con el universo y entender nuestro lugar en él.<br><br>
            
            <i>"El universo no está hecho de átomos, está hecho de historias." - Margaret Atwood</i><br><br>
            
            ¡Ven a visitarnos y descubre todo lo que el cosmos tiene para ofrecer! Te garantizamos una 
            experiencia que expandirá tus horizontes y despertará tu curiosidad científica.
        </p>
    """)
    texto_historia_contenido.setWordWrap(True)
    texto_historia_contenido.setAlignment(Qt.AlignCenter)
    texto_historia_contenido.setStyleSheet("padding: 40px;")
    
    scroll_historia.setWidget(texto_historia_contenido)
    texto_historia_layout.addWidget(scroll_historia)
    historia_layout.addWidget(texto_historia_frame)

    layout_scroll.addWidget(historia_frame)

    # 💬 BOTÓN PARA FEEDBACK (que llevará a otra sección)
    btn_feedback_frame = QFrame()
    btn_feedback_frame.setStyleSheet("background-color: #ffffff; padding: 30px;")
    btn_feedback_layout = QVBoxLayout(btn_feedback_frame)
    btn_feedback_layout.setAlignment(Qt.AlignCenter)
    
    boton_feedback = QPushButton("💬 Feedback")
    boton_feedback.setStyleSheet("""
        QPushButton {
            background-color: #8a2be2;
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 15px 30px;
            border: none;
            border-radius: 25px;
            min-width: 300px;
        }
        QPushButton:hover {
            background-color: #7a1ad2;
            transform: scale(1.05);
        }
        QPushButton:pressed {
            background-color: #6a0ac2;
        }
    """)
    boton_feedback.setCursor(Qt.PointingHandCursor)
    btn_feedback_layout.addWidget(boton_feedback)
    layout_scroll.addWidget(btn_feedback_frame)

    # Conectar el botón de feedback al callback
    if callback_feedback is not None:
        boton_feedback.clicked.connect(callback_feedback)

    # 🌠 Sección adicional
    extra = QLabel("""
        <h2 style="color:#1a1a2e; text-align:center;">Más allá del cielo</h2>
        <p style="color:#444; text-align:center; font-size:18px; max-width:800px; margin:auto;">
            Sumérgete en una colección digital inspirada en los museos de ciencia y tecnología más reconocidos del mundo.
        </p>
    """)
    extra.setAlignment(Qt.AlignCenter)
    extra.setWordWrap(True)
    extra.setStyleSheet("background-color: #ffffff; padding: 80px; border-top: 3px solid #ccc;")
    layout_scroll.addWidget(extra)

    layout_scroll.addStretch()
    contenedor_scroll.setLayout(layout_scroll)
    scroll.setWidget(contenedor_scroll)
    layout_principal.addWidget(scroll)

    return pagina