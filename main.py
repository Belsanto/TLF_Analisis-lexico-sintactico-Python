# Archivo principal para ejecutar el programa.
from tokens import lexer
from my_parser import parser
from tree import build_tree, draw_tree
import tkinter as tk
from PIL import Image, ImageTk

def main():
    # Código de entrada
    code = "NEWVAL := 3 + 4 | NEWVAL := NEWVAL * 2"

    # Analizar el código
    result = parser.parse(code, lexer=lexer)

    # Construir el árbol de derivación
    tree = build_tree(result)

    # Dibujar el árbol de derivación
    graph = draw_tree(tree)
    graph.write_png('arbol_derivacion.png')

    # Mostrar el árbol en una ventana
    root = tk.Tk()
    root.title("Árbol de Derivación")

    # Cargar la imagen del árbol
    image = Image.open("arbol_derivacion.png")
    photo = ImageTk.PhotoImage(image)

    # Crear y colocar una etiqueta para mostrar la imagen
    label = tk.Label(root, image=photo)
    label.pack()

    # Ejecutar el bucle principal de la aplicación
    root.mainloop()

if __name__ == '__main__':
    main()
