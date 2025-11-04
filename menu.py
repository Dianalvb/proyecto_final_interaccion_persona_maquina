from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout, QStackedWidget, QFrame, QMenu, 
    QStatusBar, QMenuBar, QMessageBox, QTextEdit, QFileDialog,
    QGroupBox, QLineEdit, QGridLayout
)
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QIcon, QAction, QPixmap, QKeySequence, QDesktopServices
from PySide6.QtCore import QUrl
import sys

# App y ventana principal
app = QApplication()
win = QMainWindow()
win.resize(820, 480)

# STACK PRINCIPAL
stack_main = QStackedWidget()

# PANTALLA 1
p1 = QWidget()
p1.setStyleSheet("background-color: #E6EBED;")
p1_layout = QVBoxLayout(p1)
p1_layout.setAlignment(Qt.AlignCenter)

lbl1 = QLabel("Menus")
lbl1.setStyleSheet("font-family: Arial; font-size: 20px; font-weight: 600; color: #212121;")
btn_to_p2 = QPushButton("Ir a pantalla 2")

p1_layout.addWidget(lbl1)
p1_layout.addWidget(btn_to_p2)

# MENÚ SUPERIOR para pantalla 1
menubar = win.menuBar()
m_archivo = QMenu(win)
m_archivo.setIcon(QIcon("imgTarea.jpg"))
menubar.addMenu(m_archivo)
m_exportar = m_archivo.addMenu("Exportar")
m_pantallas = menubar.addMenu("Pantallas")

def pantalla1():
    stack_main.setCurrentIndex(0)
act_p1 = QAction("pantalla 0", win)
act_p1.triggered.connect(pantalla1)
m_pantallas.addAction(act_p1)

def pantalla2():
    stack_main.setCurrentIndex(1)
act_p2 = QAction("pantalla 1", win)
act_p2.triggered.connect(pantalla2)
m_pantallas.addAction(act_p2)

def nuevo():
    QMessageBox.information(win, "Action", "Creaste un documento nuevo")

def abrir():
    QMessageBox.information(win, "Action", "Abriste un archivo")

def exp_pdf():
    QMessageBox.information(win, "Acción", "Exportaste como PDF")

def exp_word():
    QMessageBox.information(win,"Action", "Exportaste como word")


    # Submenú
act_pdf = QAction("PDF", win)
act_pdf.triggered.connect(exp_pdf)
m_exportar.addAction(act_pdf)

act_word = QAction("Word", win)
act_word.triggered.connect(exp_word)
m_exportar.addAction(act_word)

act_nuevo = QAction(QIcon("imgTarea.jpg"), "", win)
act_nuevo.setToolTip("Nuevo documento")
act_nuevo.triggered.connect(nuevo)

act_abrir = QAction("Abrir...", win)
act_abrir.triggered.connect(abrir)

act_salir = QAction("Salir", win)
act_salir.setToolTip("Salir de la aplicación")
act_salir.triggered.connect(win.close)

m_archivo.addAction(act_nuevo)
m_archivo.addAction(act_abrir)
m_archivo.addSeparator()
m_archivo.addAction(act_salir)

# PANTALLA 2
p2 = QWidget()
p2_layout = QHBoxLayout(p2)
p2_layout.setContentsMargins(0, 0, 0, 0)
p2_layout.setSpacing(0)

# barra lateral
sidebar = QFrame()
sidebar.setFixedWidth(200)
sidebar.setObjectName("sidebar")

vside = QVBoxLayout(sidebar)
vside.setContentsMargins(12, 16, 12, 16)
vside.setSpacing(8)

lbl2 = QLabel("Menu Lateral")
lbl2.setObjectName("tituloMenu")
lbl2.setAlignment(Qt.AlignLeft)

btn_back = QPushButton("Regresar")

btn_menubasico1 = QPushButton("menubasico 1")
btn_menubasico2 = QPushButton("menubasico 2")
btn_menubasico4 = QPushButton("menu basico 4")
btn_menubasico5 = QPushButton("menu basico 5")

botones_menu = [btn_menubasico1, btn_menubasico2, btn_menubasico4, btn_menubasico5]
for b in botones_menu:
    b.setCheckable(True)
    b.setCursor(Qt.PointingHandCursor)
    b.setObjectName("btnMenu")

vside.addWidget(lbl2)
vside.addSpacing(6)
for b in botones_menu:
    vside.addWidget(b)
vside.addStretch(1)
vside.addWidget(btn_back)

# stack interno
stack_interno = QStackedWidget()

# Funciones para crear las páginas internas del menú lateral
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


def pagina_menuBasico2():
    w = QWidget()
    layout = QVBoxLayout(w)
    lbl = QLabel("Tono comunicativo: Texto")
    lbl.setAlignment(Qt.AlignCenter)

    #columna 1
    boxA=QGroupBox("tono tecnico/frío")
    vA = QVBoxLayout(boxA)
    vA.setSpacing(8)

    lblA = QLabel("Introduzca credenciales y ejecute la operación.")
    lblA.setStyleSheet("font-size: 13px; color:#334155;")
    userA = QLineEdit(); userA.setPlaceholderText("Usuario")
    passA = QLineEdit(); passA.setPlaceholderText("Contraseña")
    passA.setEchoMode(QLineEdit.Password)

    btnGuardarA = QPushButton("Guardar")
    btnEliminarA = QPushButton("Eliminar")

    estadoA = QLabel("Estado: esperando entrada")
    estadoA.setStyleSheet("font-size: 12px; color:#475569;")

    def guardar_A():
        if not userA.text() or not passA.text():
            QMessageBox.warning(win, "Validación",
                            "Campos incompletos. Complete usuario y contraseña.")
        estadoA.setText("Estado: error de validación")
        return
    QMessageBox.information(win, "Proceso",
                            "Operación completada exitosamente.")
    estadoA.setText("Estado: operación exitosa")

    def eliminar_A():
        r = QMessageBox.question(win, "Confirmación",
                             "¿Desea proceder con la eliminación?",
                             QMessageBox.Yes | QMessageBox.No)
        if r == QMessageBox.Yes:
            estadoA.setText("Estado: elemento eliminado")
        else:
            estadoA.setText("Estado: operación cancelada")

    btnGuardarA.clicked.connect(guardar_A)
    btnEliminarA.clicked.connect(eliminar_A)

    vA.addWidget(lblA)
    vA.addWidget(userA)
    vA.addWidget(passA)
    vA.addWidget(btnGuardarA)
    vA.addWidget(btnEliminarA)
    vA.addWidget(estadoA)

    #columna 2

    boxB = QGroupBox("Tono empático / humano")
    vB = QVBoxLayout(boxB)
    vB.setSpacing(8)

    lblB = QLabel("Inicia sesión para continuar 😊")
    lblB.setStyleSheet("font-size: 13px; color:#334155;")
    userB = QLineEdit(); userB.setPlaceholderText("Usuario")
    passB = QLineEdit(); passB.setPlaceholderText("Contraseña (la cuidaremos)")
    passB.setEchoMode(QLineEdit.Password)

    btnGuardarB = QPushButton("Guardar")
    btnEliminarB = QPushButton("Eliminar")

    estadoB = QLabel("Listo para ayudarte ✨")
    estadoB.setStyleSheet("font-size: 12px; color:#475569;")

    def guardar_B():
        if not userB.text() or not passB.text():
            QMessageBox.warning(win, "Faltan datos",
                            "Por favor completa usuario y contraseña antes de continuar 🙏")
        estadoB.setText("Ups, faltó información. Ya casi.")
        return
    QMessageBox.information(win, "¡Todo listo!",
                            "Tus datos se guardaron correctamente. ¡Gracias! ✅")
    estadoB.setText("Cambios guardados con éxito 🎉")

    def eliminar_B():
        r = QMessageBox.question(win, "¿Eliminar este elemento?",
                             "¿Seguro que deseas eliminar esto? No podrás recuperarlo",
                             QMessageBox.Yes | QMessageBox.No)
        if r == QMessageBox.Yes:
         estadoB.setText("Elemento eliminado. Si fue un error, avísanos.")
        else:
            estadoB.setText("Cancelado. Gracias por revisar antes de continuar.")

    btnGuardarB.clicked.connect(guardar_B)
    btnEliminarB.clicked.connect(eliminar_B)

    vB.addWidget(lblB)
    vB.addWidget(userB)
    vB.addWidget(passB)
    vB.addWidget(btnGuardarB)
    vB.addWidget(btnEliminarB)
    vB.addWidget(estadoB)

    layout.addWidget(boxA, 1)
    layout.addWidget(boxB, 1)

    # Estilos suaves para contraste visual
    win.setStyleSheet("""
    QWidget { background: #f8fafc; font-family: Segoe UI; }
    QGroupBox {
        background: #ffffff; border: 1px solid #e5e7eb; border-radius: 10px;
        padding: 12px; font-weight: 700; color:#0f172a;
    }
    QLineEdit { padding: 8px 10px; border:1px solid #cbd5e1; border-radius:8px; background:#fff; }
    QLineEdit:focus { border:1px solid #60a5fa; }
    QPushButton {
        padding: 8px 14px; border-radius: 8px; border: 1px solid #cbd5e1;
        background: #e2e8f0; color: #0f172a; font-weight: 600;
    }
    QPushButton:hover { background: #cbd5e1; }
    """)

    return w


def pagina_menuBasico4():
    w = QWidget()
    layout = QVBoxLayout(w)

    grid = QGridLayout()

    # Panel Principal: Un encabezado que abarca 3 columnas (Textos:Jerarquía, Grid, contraste), (colspan=3)
    titulo = QLabel("Textos:Jerarquía, Grid, contraste") #Título
    titulo.setStyleSheet("background:#bfdbfe; font-size: 26px; font-weight:600; padding:4px;")
    grid.addWidget(titulo, 0, 0, 1, 3, Qt.AlignCenter) # (widget, fila, columna, cantidad de filas que usara el widget, cantidad de columnas, alineación)

    # Menú lateral: abarca 2 filas (rowspan=2)
    menu = QLabel("Menú lateral\n(rowspan=2)")
    menu.setStyleSheet("background:#fde68a;font-size: 16px;")
    grid.addWidget(menu, 1, 0, 2, 1)

    # Celdas normales
    grid.addWidget(QLabel("Contenido 1"), 1, 1) # widget, fila, columna
    cont2= QLabel("Contenido 2")
    cont2.setStyleSheet("font-size: 13px; color: #64748b;")
    cont2.setWordWrap(True) #Se ajusta a varias lineas sino cabe en una
    grid.addWidget(cont2, 1, 2)
    grid.addWidget(QLabel("Pie o información extra"), 2, 1, 1, 2)

    layout.addLayout(grid)

    """
    Tamaño y Jerarquía 
    titulo principal : 22-28px
    subtitulo o encabezado secundario: 16-20px
    microcopy o texto auxiliar: 10-12 px 
    
    contraste: que no sea letra gris con fondo claro

    """

    return w


def pagina_menuBasico5():
        w = QWidget()
        layout = QVBoxLayout(w)

    # Editor de texto
        editor = QTextEdit()
        layout.addWidget(editor)

    # Menú bar
        menubar = QMenuBar()
        layout.setMenuBar(menubar)

    # Archivo
        m_archivo = menubar.addMenu("Archivo")

        def nuevo():
            editor.clear()

        def abrir():
            ruta, _ = QFileDialog.getOpenFileName(w, "Abrir...", "", "Texto (*.txt);;Todos (*)")
            if ruta:
                with open(ruta, "r", encoding="utf-8") as f:
                    editor.setPlainText(f.read())

        def guardar():
            ruta, _ = QFileDialog.getSaveFileName(w, "Guardar como...", "", "Texto (*.txt)")
            if ruta:
                with open(ruta, "w", encoding="utf-8") as f:
                    f.write(editor.toPlainText())

        act_nuevo = QAction("Nuevo", w)
        act_nuevo.setShortcut(QKeySequence.New)
        act_nuevo.triggered.connect(nuevo)

        act_abrir = QAction("Abrir...", w)
        act_abrir.setShortcut(QKeySequence.Open)
        act_abrir.triggered.connect(abrir)

        act_guardar = QAction("Guardar", w)
        act_guardar.setShortcut(QKeySequence.Save)
        act_guardar.triggered.connect(guardar)

        act_salir = QAction("Salir", w)
        act_salir.setShortcut("Ctrl+Q")
        act_salir.triggered.connect(lambda: w.close())

        m_archivo.addActions([act_nuevo, act_abrir, act_guardar])
        m_archivo.addSeparator()
        m_archivo.addAction(act_salir)

    # Editar
        m_editar = menubar.addMenu("Editar")

        act_undo = QAction("Deshacer", w); act_undo.setShortcut(QKeySequence.Undo); act_undo.triggered.connect(editor.undo)
        act_redo = QAction("Rehacer", w); act_redo.setShortcut(QKeySequence.Redo); act_redo.triggered.connect(editor.redo)
        act_cut  = QAction("Cortar", w);  act_cut.setShortcut(QKeySequence.Cut);   act_cut.triggered.connect(editor.cut)
        act_copy = QAction("Copiar", w);  act_copy.setShortcut(QKeySequence.Copy); act_copy.triggered.connect(editor.copy)
        act_paste= QAction("Pegar", w);   act_paste.setShortcut(QKeySequence.Paste); act_paste.triggered.connect(editor.paste)
        act_all  = QAction("Seleccionar todo", w); act_all.setShortcut(QKeySequence.SelectAll); act_all.triggered.connect(editor.selectAll)

        m_editar.addActions([act_undo, act_redo])
        m_editar.addSeparator()
        m_editar.addActions([act_cut, act_copy, act_paste, act_all])

    # Ayuda
        m_ayuda = menubar.addMenu("Ayuda")

        def ayuda():
            QMessageBox.information(w, "Acerca de", "Ejemplo de barra de menú dentro de un widget.\nUsando PySide6.")

        act_acerca = QAction("Acerca de...", w)
        act_acerca.triggered.connect(ayuda)
        m_ayuda.addAction(act_acerca)

        return w

# Agregar las páginas al stack interno
stack_interno.addWidget(pagina_menuBasico1())  # index 0
stack_interno.addWidget(pagina_menuBasico2())  # index 1
stack_interno.addWidget(pagina_menuBasico4())  # index 2
stack_interno.addWidget(pagina_menuBasico5())  # index 3


# lógica de cambio de página interna
def mostrar_pagina(numero, boton):
    stack_interno.setCurrentIndex(numero)
    for b in botones_menu:
        b.setChecked(b == boton)

btn_menubasico1.clicked.connect(lambda: mostrar_pagina(0, btn_menubasico1))
btn_menubasico2.clicked.connect(lambda: mostrar_pagina(1, btn_menubasico2))
btn_menubasico4.clicked.connect(lambda: mostrar_pagina(2, btn_menubasico4))
btn_menubasico5.clicked.connect(lambda: mostrar_pagina(3, btn_menubasico5))

mostrar_pagina(0, btn_menubasico1)

p2_layout.addWidget(sidebar)
p2_layout.addWidget(stack_interno, 1)

# Añadir pantallas principales al stack
stack_main.addWidget(p1)  # index 0
stack_main.addWidget(p2)  # index 1

# NAVEGACIÓN ENTRE PANTALLAS
statusbar = QStatusBar()
win.setStatusBar(statusbar)

def ir_a_p2():
    stack_main.setCurrentIndex(1)
    win.menuBar().setVisible(False)
    statusbar.showMessage("Navegaste a pantalla 2", 2000)

def regresar_a_p1():
    stack_main.setCurrentIndex(0)
    win.menuBar().setVisible(True)
    statusbar.showMessage("Volviste a la pantalla principal", 2000)

btn_to_p2.clicked.connect(ir_a_p2)
btn_back.clicked.connect(regresar_a_p1)

# Configuración final
win.setWindowTitle("Navegador entre pantallas y menús")
win.setCentralWidget(stack_main)
win.setStyleSheet("""
    QWidget { font-family: Arial, sans-serif; font-size: 14px; }
    #sidebar {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #404040, stop:1 #bfbfbf);
        border-right: 0px solid transparent;
    }
    #tituloMenu { font-size: 16px; font-weight: 700; padding: 4px 6px; color: white; }
    #btnMenu {
        text-align: left;
        padding: 10px 12px;
        border-radius: 10px;
        border: 1px solid transparent;
        background: #ffffff;
    }
    #btnMenu:hover { background: #f3f4f6; }
    #btnMenu:checked {
        background: #e8eefc;
        border: 1px solid #c7d2fe;
        font-weight: 600;
    }
""")

statusbar.showMessage("Listo. Estás en la pantalla principal.")
win.show()
sys.exit(app.exec())