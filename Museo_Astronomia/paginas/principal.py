from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea, QFrame
from PySide6.QtCore import Qt, QUrl, QTimer
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
import os


def crear_pagina_principal(parent=None, base_path="."):
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
