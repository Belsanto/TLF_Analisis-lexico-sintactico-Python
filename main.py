import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QWidget, QTextEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt
from tokens import lexer  # Importa el lexer generado por el analizador léxico
from my_parser import parser  # Importa el parser
from tree import build_tree, draw_tree  # Importa funciones para construir y dibujar árboles
import tkinter as tk
from PIL import Image, ImageTk
import os

# Define la clase principal de la aplicación
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configura la ventana principal
        self.setWindowTitle("Compilador")
        self.setGeometry(100, 100, 800, 600)

        # Layout principal
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)

        # Botón para cargar un archivo
        self.uploadButton = QPushButton('Subir Archivo', self)
        self.uploadButton.clicked.connect(self.ev_archivo)
        self.layout.addWidget(self.uploadButton)

        # Área de texto para el código fuente
        self.codigoFuente = QTextEdit(self)
        self.layout.addWidget(QLabel('Codigo Fuente', self))
        self.layout.addWidget(self.codigoFuente)

        # Área de texto para el análisis léxico
        self.analisisLexico = QTextEdit(self)
        self.analisisLexico.setReadOnly(True)
        self.layout.addWidget(QLabel('Analisis Lexico', self))
        self.layout.addWidget(self.analisisLexico)

        # Área de texto para el análisis sintáctico
        self.analisisSintactico = QTextEdit(self)
        self.analisisSintactico.setReadOnly(True)
        self.layout.addWidget(QLabel('Analisis Sintactico', self))
        self.layout.addWidget(self.analisisSintactico)

        # Botón para iniciar el análisis léxico
        self.analizarLexicoButton = QPushButton('Analizar Lexico', self)
        self.analizarLexicoButton.clicked.connect(self.ev_lexico)
        self.layout.addWidget(self.analizarLexicoButton)

        # Botón para iniciar el análisis sintáctico
        self.analizarSintacticoButton = QPushButton('Analisis Sintactico', self)
        self.analizarSintacticoButton.clicked.connect(self.ev_sintactico)
        self.layout.addWidget(self.analizarSintacticoButton)

        # Botón para generar el árbol de derivación
        self.generarArbolButton = QPushButton('Generar Árbol de Derivación', self)
        self.generarArbolButton.clicked.connect(self.mostrar_arbol)
        self.layout.addWidget(self.generarArbolButton)

    # Función para manejar la carga de un archivo
    def ev_archivo(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Subir Archivo", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                data = file.read()
                self.codigoFuente.setText(data)

    # Función para realizar el análisis léxico
    def ev_lexico(self):
        self.analisisLexico.clear()
        data = self.codigoFuente.toPlainText()
        lexer.input(data)

        output = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            output.append(f"Linea {tok.lineno} Tipo {tok.type} Valor {tok.value} Posicion {tok.lexpos}")

        self.analisisLexico.setText("\n".join(output))

    # Función para realizar el análisis sintáctico
    def ev_sintactico(self):
        self.analisisSintactico.clear()
        data = self.codigoFuente.toPlainText()
        lexer.input(data)

        valores = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            if tok.type in ['NUMBER', 'REAL', 'STRING', 'CHAR']:
                valores.append(str(tok.value))

        self.analisisSintactico.setText("\n".join(valores))

    # Función para mostrar el árbol de derivación
    def mostrar_arbol(self):
        data = self.codigoFuente.toPlainText()

        # Obtener solo la primera línea no vacía del código fuente
        first_line = ""
        for line in data.splitlines():
            if line.strip():
                first_line = line.strip()
                break

        if not first_line:
            print("No se encontró una línea válida para analizar.")
            return

        result = parser.parse(first_line, lexer=lexer)

        if result:
            # Construir el árbol de derivación
            tree = build_tree(result)

            # Dibujar el árbol de derivación
            graph = draw_tree(tree)
            graph.write_png('arbol_derivacion.png')

            # Mostrar el árbol en una ventana
            root = tk.Tk()
            root.title("Derivación")

            # Cargar la imagen del árbol
            image = Image.open("arbol_derivacion.png")
            photo = ImageTk.PhotoImage(image)

            # Crear y colocar una etiqueta para mostrar la imagen
            label = tk.Label(root, image=photo)
            label.pack()

            # Ejecutar el bucle principal de la aplicación
            root.mainloop()
        else:
            print("Error al analizar la línea para generar el árbol de derivación.")

# Función para iniciar la aplicación
def iniciar():
    app = QApplication(sys.argv)
    ventana = Main()
    ventana.show()
    sys.exit(app.exec_())

# Entrada principal del programa
if __name__ == '__main__':
    iniciar()
