import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLabel, QStackedWidget, QHBoxLayout, QPushButton, QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

# Importar páginas
from paginas.principal import crear_pagina_principal
from paginas.explorar import crear_pagina_explorar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Museo de Astronomía")
        self.resize(1400, 900)

        # Estilo general
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0b0c10;
                color: #ffffff;
            }

            QWidget#nav_bar {
                background-color: #1a1a2e;
                border-bottom: 2px solid #8a2be2;
            }

            QLabel#logo {
                color: #8a2be2;
                font-family: "Orbitron", "Segoe UI";
                font-size: 22px;
                font-weight: bold;
                padding: 10px 30px;
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
                color: #ffffff;
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

        nav_bar = self.crear_barra_navegacion()
        main_layout.addWidget(nav_bar)

        self.stack = QStackedWidget()
        main_layout.addWidget(self.stack)

        # Páginas registradas
        self.paginas = {
            "INICIO": crear_pagina_principal(self),
            "EXPLORAR": crear_pagina_explorar(self),
        }

        for pagina in self.paginas.values():
            self.stack.addWidget(pagina)

        central_widget.setLayout(main_layout)

        self.mostrar_pagina("INICIO")

    def crear_barra_navegacion(self):
        nav_frame = QFrame()
        nav_frame.setObjectName("nav_bar")
        nav_frame.setFixedHeight(80)

        layout = QHBoxLayout()
        layout.setContentsMargins(20, 0, 20, 0)
        layout.setSpacing(0)

        logo = QLabel("🌌 COSMOS EXPLORER")
        logo.setObjectName("logo")
        layout.addWidget(logo)
        layout.addStretch()

        # Botones de navegación
        self.botones_nav = {}
        secciones = ["INICIO", "EXPLORAR"]

        for seccion in secciones:
            boton = QPushButton(seccion)
            boton.setObjectName("nav_button")
            boton.setFixedHeight(80)
            boton.clicked.connect(lambda checked, s=seccion: self.mostrar_pagina(s))
            layout.addWidget(boton)
            self.botones_nav[seccion] = boton

        layout.addStretch()
        nav_frame.setLayout(layout)
        return nav_frame

    def mostrar_pagina(self, nombre):
        for boton in self.botones_nav.values():
            boton.setObjectName("nav_button")
            boton.style().unpolish(boton)
            boton.style().polish(boton)

        if nombre in self.botones_nav:
            self.botones_nav[nombre].setObjectName("nav_button_active")
            self.botones_nav[nombre].style().unpolish(self.botones_nav[nombre])
            self.botones_nav[nombre].style().polish(self.botones_nav[nombre])

        self.stack.setCurrentWidget(self.paginas[nombre])


def main():
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 11))
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
