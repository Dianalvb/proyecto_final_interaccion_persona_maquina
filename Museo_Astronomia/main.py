import sys
import os
from functools import partial
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLabel, QStackedWidget, QHBoxLayout, QPushButton, QFrame
)
from PySide6.QtCore import Qt, QUrl, QSize
from PySide6.QtGui import QFont, QPixmap, QIcon

# Importar páginas
from paginas.principal import crear_pagina_principal
from paginas.explorar import crear_pagina_explorar
from paginas.galeria import crear_pagina_galeria
from paginas.tienda import crear_pagina_tienda

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
            "Galeria": crear_pagina_galeria(self),
            "Tienda": crear_pagina_tienda(self)
        }

        for pagina in self.paginas.values():
            self.stack.addWidget(pagina)

        central_widget.setLayout(main_layout)
        self.mostrar_pagina("Inicio")

    def crear_barra_navegacion(self):
        nav_frame = QFrame()
        nav_frame.setObjectName("nav_bar")
        nav_frame.setFixedHeight(80)

        # Layout principal dividido en 3 zonas
        layout_general = QHBoxLayout(nav_frame)
        layout_general.setContentsMargins(20, 0, 20, 0)
        layout_general.setSpacing(0)

        # ============================================================
        #   ZONA IZQUIERDA (LOGO)
        # ============================================================
        zona_izquierda = QHBoxLayout()
        zona_izquierda.setAlignment(Qt.AlignLeft)

        logo_icono = QLabel()
        ruta_logo = os.path.join(os.path.dirname(__file__), "logo.png")
        pix_logo = QPixmap(ruta_logo)

        if not pix_logo.isNull():
            logo_icono.setPixmap(pix_logo.scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            logo_icono.setText("⚠️")
            logo_icono.setStyleSheet("font-size: 25px; color:#70155F;")

        logo_texto = QLabel("Horizontes Estelares")
        logo_texto.setObjectName("logo_texto")

        zona_izquierda.addWidget(logo_icono)
        zona_izquierda.addWidget(logo_texto)

        # ============================================================
        #   ZONA CENTRAL (MENÚ)
        # ============================================================
        zona_centro = QHBoxLayout()
        zona_centro.setAlignment(Qt.AlignCenter)

        self.botones_nav = {}
        secciones = ["Inicio", "Explorar", "Galeria", "Tienda"]

        for seccion in secciones:
            boton = QPushButton(seccion)
            boton.setObjectName("nav_button")
            boton.setFixedHeight(80)
            boton.clicked.connect(partial(self.mostrar_pagina, seccion))
            zona_centro.addWidget(boton)
            self.botones_nav[seccion] = boton

        # ============================================================
        #   ZONA DERECHA (TICKETS PEGADO A LA ESQUINA)
        # ============================================================
        zona_derecha = QHBoxLayout()
        zona_derecha.setAlignment(Qt.AlignRight)

        boton_tickets = QPushButton("Tickets")
        boton_tickets.setFixedHeight(40)
        boton_tickets.setCursor(Qt.PointingHandCursor)

        ruta_ticket = os.path.join(os.path.dirname(__file__), "ticket.png")
        pix_ticket = QPixmap(ruta_ticket)

        if not pix_ticket.isNull():
            boton_tickets.setIcon(QIcon(pix_ticket))
            boton_tickets.setIconSize(QSize(22, 22))

        boton_tickets.setStyleSheet("""
            QPushButton {
                background-color: #0db36c;
                color: white;
                font-family: 'Times New Roman';
                font-size: 15px;
                padding: 8px 20px;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #0a9a5d;
            }
        """)

        boton_tickets.clicked.connect(partial(self.mostrar_pagina, "Tienda"))

        zona_derecha.addWidget(boton_tickets)

        # ============================================================
        #   ENSAMBLAR ZONAS
        # ============================================================
        layout_general.addLayout(zona_izquierda, 1)
        layout_general.addLayout(zona_centro, 2)
        layout_general.addLayout(zona_derecha, 1)

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
