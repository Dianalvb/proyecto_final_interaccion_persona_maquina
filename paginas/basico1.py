from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QFrame, QStackedWidget
from PySide6.QtCore import Qt
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
def pagina_menuBasico1():
    w = QWidget()
    layout = QVBoxLayout(w)
    lbl = QLabel("Abrir url")
    lbl.setAlignment(Qt.AlignCenter)
    btn = QPushButton("Botón abrir enlace")
    def abrir_enlace():
        url = QUrl("https://www.costco.es/sobre-nosotros")
        QDesktopServices.openUrl(url)
    btn.clicked.connect(abrir_enlace)
    layout.addWidget(lbl)
    layout.addWidget(btn)
    return w