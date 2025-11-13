from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout,  QPushButton
from PySide6.QtCore import Qt
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QRect
from PySide6.QtGui import QIcon, QPixmap


def crear_pagina_explorar(parent=None):
    """Página para explorar el cosmos"""
    pagina = QWidget(parent)
    layout = QGridLayout(pagina)

    titulo = QLabel("Area interactiva")
    titulo.setAlignment(Qt.AlignCenter)
    titulo.setStyleSheet("""
        color: #ffffff;
        font-size: 28px;
        font-weight: bold;
        font-family: 'Segoe UI';
    """)

    descripcion = QLabel(
        "Sumérgete en los misterios del universo: estrellas, nebulosas, agujeros negros y más."
    )
    descripcion.setAlignment(Qt.AlignCenter)
    descripcion.setWordWrap(True)
    descripcion.setStyleSheet("""
        color: #cccccc;
        font-size: 18px;
        font-family: 'Segoe UI';
    """)

    btn_memorama1= QPushButton(pagina)
    btn_memorama1.setIcon(QIcon("Museo_Astronomia/reverse.jpg"))
    btn_memorama1.move(100, 150)
    btn_memorama1.setFixedSize(100,100)
    btn_memorama1.flipped = False
    layout.addWidget(btn_memorama1, 2,0,1,1, Qt.AlignCenter)

    btn_par1= QPushButton(pagina)
    btn_par1.setIcon(QIcon("Museo_Astronomia/reverse.jpg"))
    btn_par1.move(100, 150)
    btn_par1.setFixedSize(100,100)
    btn_par1.flipped = False
    layout.addWidget(btn_par1, 1,0,1,1, Qt.AlignCenter)


    def al_oprimir():
        inicio_memorama1 = btn_memorama1.geometry()
        mid = QRect(inicio_memorama1.x() + inicio_memorama1.width() //2, inicio_memorama1.y(),0,inicio_memorama1.height())
        
        btn_memorama1.shrik = QPropertyAnimation(btn_memorama1, b"geometry")
        btn_memorama1.shrik.setDuration(150)
        btn_memorama1.shrik.setEasingCurve(QEasingCurve.InOutQuad)
        btn_memorama1.shrik.setStartValue(inicio_memorama1)
        btn_memorama1.shrik.setEndValue(mid)

        btn_memorama1.expand = QPropertyAnimation(btn_memorama1, b"geometry")
        btn_memorama1.expand.setDuration(150)
        btn_memorama1.expand.setEasingCurve(QEasingCurve.InOutQuad)
        btn_memorama1.expand.setStartValue(mid)
        btn_memorama1.expand.setEndValue(inicio_memorama1)
        def swap():
            if not btn_memorama1.flipped:
                btn_memorama1.setIcon(QIcon("Museo_Astronomia/museo_astronomía1.jpg"))
            else:
                btn_memorama1.setIcon(QIcon("Museo_Astronomia/reverse.jpg"))
            btn_memorama1.flipped = not btn_memorama1.flipped

        btn_memorama1.shrik.finished.connect(swap)
        btn_memorama1.shrik.finished.connect(btn_memorama1.expand.start)
        btn_memorama1.shrik.start()
    btn_memorama1.clicked.connect(al_oprimir)

    def al_oprimir_par1():
        inicio_par1 = btn_par1.geometry()
        mid = QRect(inicio_par1.x() + inicio_par1.width() //2, inicio_par1.y(),0,inicio_par1.height())
        
        btn_par1.shrik = QPropertyAnimation(btn_par1, b"geometry")
        btn_par1.shrik.setDuration(150)
        btn_par1.shrik.setEasingCurve(QEasingCurve.InOutQuad)
        btn_par1.shrik.setStartValue(inicio_par1)
        btn_par1.shrik.setEndValue(mid)

        btn_par1.expand = QPropertyAnimation(btn_par1, b"geometry")
        btn_par1.expand.setDuration(150)
        btn_par1.expand.setEasingCurve(QEasingCurve.InOutQuad)
        btn_par1.expand.setStartValue(mid)
        btn_par1.expand.setEndValue(inicio_par1)
        def swap2():
            if not btn_par1.flipped:
                btn_par1.setIcon(QIcon("Museo_Astronomia/museo_astronomía1.jpg"))
            else:
                btn_par1.setIcon(QIcon("Museo_Astronomia/reverse.jpg"))
            btn_par1.flipped = not btn_par1.flipped

        btn_par1.shrik.finished.connect(swap2)
        btn_par1.shrik.finished.connect(btn_par1.expand.start)
        btn_par1.shrik.start()
    btn_par1.clicked.connect(al_oprimir_par1)


    layout.addWidget(titulo,0,0,1,1,Qt.AlignCenter)
    layout.addWidget(descripcion, 0,1,0,1,Qt.AlignCenter)
    
    return pagina
