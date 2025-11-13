import sys
import os
from functools import partial
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLabel, QStackedWidget, QHBoxLayout, QPushButton, QFrame
)
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QFont, QPixmap

# Importar páginas
from paginas.principal import crear_pagina_principal
from paginas.explorar import crear_pagina_explorar
from paginas.galeria import crear_pagina_galeria
print("⚙️ Ejecutando versión actualizada de main.py")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Museo de Astronomía")
        self.resize(1400, 900)

        # 🎨 Estilo general
        self.setStyleSheet("""
            QMainWindow {
                background-color: #74AAC1;
                color: #ffffff;
            }

            QWidget#nav_bar {
                background-color: #1a1a2e;
                border-bottom: 2px solid #8a2be2;
            }

            QLabel#logo_texto {
                color: #8a2be2;
                font-family: "Orbitron", "Segoe UI";
                font-size: 22px;
                font-weight: bold;
                padding-left: 10px;
            }

            QPushButton#nav_button {
                background-color: transparent;
                color: #c5c6c7;
                font-size: 14px;
                padding: 18px 25px;
                border: none;
            }

            QPushButton#nav_button:hover {
                background-color: #16213e;
                color: #8a2be2;
            }

            QPushButton#nav_button_active {
                background-color: transparent;
                color: #1e90ff;
                font-size: 14px;
                font-weight: bold;
                padding: 18px 25px;
                border-bottom: 3px solid #1e90ff;
            }

            QLabel#titulo_pagina {
                color: #293170;
                font-size: 36px;
                font-weight: bold;
                margin: 20px;
            }
        """)

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Barra de navegación
        nav_bar = self.crear_barra_navegacion()
        main_layout.addWidget(nav_bar)

        # Contenedor de páginas
        self.stack = QStackedWidget()
        main_layout.addWidget(self.stack)

        # Páginas registradas
        self.paginas = {
            "Inicio": crear_pagina_principal(self),
            "Explorar": crear_pagina_explorar(self),
            "Galeria": crear_pagina_galeria(self)
        }

        for pagina in self.paginas.values():
            self.stack.addWidget(pagina)

        central_widget.setLayout(main_layout)
        self.mostrar_pagina("Inicio")

    def crear_barra_navegacion(self):
        nav_frame = QFrame()
        nav_frame.setObjectName("nav_bar")
        nav_frame.setFixedHeight(80)

        layout = QHBoxLayout()
        layout.setContentsMargins(20, 0, 20, 0)
        layout.setSpacing(0)

        # 🔹 Logo + texto
        logo_container = QWidget()
        logo_layout = QHBoxLayout(logo_container)
        logo_layout.setContentsMargins(0, 0, 0, 0)
        logo_layout.setSpacing(10)

        logo_icono = QLabel()

        ruta_logo = os.path.join(os.path.dirname(__file__), "logo.png")
        print("Ruta logo:", ruta_logo, "Existe:", os.path.exists(ruta_logo))

        pixmap = QPixmap(ruta_logo)
        if not pixmap.isNull():
            logo_icono.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            logo_icono.setText("⚠️?")
            logo_icono.setStyleSheet("font-size: 28px; color: #70155F;")

        logo_texto = QLabel("Horizontes Estelares")
        logo_texto.setObjectName("logo_texto")

        logo_layout.addWidget(logo_icono)
        logo_layout.addWidget(logo_texto)
        layout.addWidget(logo_container)

        layout.addStretch()

        # 🔹 Botones de navegación
        self.botones_nav = {}
        secciones = ["Inicio", "Explorar", "Galeria"]

        for seccion in secciones:
            boton = QPushButton(seccion)
            boton.setObjectName("nav_button")
            boton.setFixedHeight(80)

            # ✅ Conexión segura con partial (evita error del 'checked')
            boton.clicked.connect(partial(self.mostrar_pagina, seccion))

            layout.addWidget(boton)
            self.botones_nav[seccion] = boton

        layout.addStretch()
        nav_frame.setLayout(layout)
        return nav_frame

    def mostrar_pagina(self, nombre):
        """Cambia la página visible y actualiza el estilo activo de los botones"""
        for boton in self.botones_nav.values():
            boton.setObjectName("nav_button")
            boton.style().unpolish(boton)
            boton.style().polish(boton)

        if nombre in self.botones_nav:
            self.botones_nav[nombre].setObjectName("nav_button_active")
            self.botones_nav[nombre].style().unpolish(self.botones_nav[nombre])
            self.botones_nav[nombre].style().polish(self.botones_nav[nombre])
            self.botones_nav[nombre].update()

        self.stack.setCurrentWidget(self.paginas[nombre])


def main():
    app = QApplication(sys.argv)
    app.setFont(QFont("Verdana", 11))
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
