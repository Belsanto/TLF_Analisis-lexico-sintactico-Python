# Trabajo Final de TLF: Análisis Léxico y Sintáctico en Python

Este repositorio contiene el trabajo final de la asignatura Teoría de Lenguajes Formales de Ingeniería de Sistemas y Computación en la Universidad del Quindío. Este proyecto fue desarrollado por los estudiantes Santiago Velandia Gallo y Frank Soto.

## Descripción del Proyecto

Este proyecto implementa un analizador léxico y sintáctico para un lenguaje ficticio utilizando Python. Se emplean las herramientas PLY (Python Lex-Yacc) para el análisis léxico y sintáctico, junto con Graphviz y Pydot para la visualización del árbol de derivación.

## Tabla de Contenidos

- [Análisis Léxico](#análisis-léxico)
- [Análisis Sintáctico](#análisis-sintáctico)
- [Construcción y Visualización del Árbol de Derivación](#construcción-y-visualización-del-árbol-de-derivación)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Créditos](#créditos)

## Análisis Léxico

### Ply (Python Lex-Yacc)

PLY es una implementación en Python de las herramientas Lex y Yacc. Con PLY, puedes construir el analizador léxico y sintáctico de tu lenguaje.

## Instalación
```bash
pip install ply
```
#### Uso
- Analizador Léxico: Define las expresiones regulares para los tokens del lenguaje. Este módulo reconoce una serie de tokens que representan operadores aritméticos, relacionales, lógicos, símbolos de apertura y cierre, palabras reservadas, identificadores y valores.
- Utiliza PLY para convertir una cadena de entrada en una secuencia de tokens.

## Análisis Léxico
- Analizador Sintáctico: Define las reglas gramaticales para reconocer y procesar asignaciones y expresiones aritméticas, así como sus acciones correspondientes.
- Utiliza estas reglas para generar un árbol de derivación basado en la estructura del código de entrada.

## Construcción y Visualización del Árbol de Derivación
### Graphviz y Pydot
Para visualizar árboles de derivación, se utilizan Graphviz junto con Pydot en Python.
### Tkinter
Para una interfaz gráfica simple donde se pueda visualizar directamente en una ventana de Python:

- TreeNode: Usa una clase TreeNode para construir el árbol de derivación.
- Generación de PNG: Genera un archivo PNG del árbol de derivación utilizando Pydot y Graphviz.
- Visualización: Muestra el árbol de derivación en una ventana gráfica utilizando Tkinter y Pillow.

### Requisitos
Asegúrate de tener Python instalado y luego instala las siguientes bibliotecas:
```bash
pip install ply pydot pillow PyQt5 graphviz
```
También puedes instalar todas las dependencias utilizando:
```bash
pip install -r requirements.txt
```
### Instalación de Graphviz
Para instalar Graphviz, sigue estos pasos:

1. Descarga Graphviz desde Graphviz.org.
2. Después de instalar Graphviz, agrega la ubicación de la herramienta dot a tu variable de entorno PATH. Esto permitirá que Pydot pueda encontrar y utilizar la herramienta dot correctamente.

## Cómo agregar dot al PATH en Windows

1. Encuentra la ubicación de instalación de Graphviz (por lo general en la carpeta `bin`).
2. Copia la ruta completa del directorio donde se encuentra `dot`.
3. Abre el Panel de Control de Windows.
4. Haz clic en "Sistema y seguridad".
5. Haz clic en "Sistema".
6. En el panel izquierdo, haz clic en "Configuración avanzada del sistema".
7. En la ventana de Propiedades del Sistema, haz clic en "Variables de entorno".
8. En la sección "Variables del sistema", busca la variable llamada `PATH` y selecciónala.
9. Haz clic en "Editar...".
10. En la ventana de edición, haz clic en "Nuevo" y pega la ruta copiada.
11. Haz clic en "Aceptar" en todas las ventanas para guardar los cambios.

## Uso

Para ejecutar el proyecto, simplemente ejecuta el script principal. Luego en la vista selecciona el archivo que leerá el código fuente (ejemplo de un archivo: `prueba.txt`),luego usa los botones y realiza el análisis léxico y sintáctico, y genera un reporte en formato HTML con el árbol de derivación visualizado.
```bash
python main.py
```
## Créditos
Este proyecto fue desarrollado por Santiago Velandia Gallo y Frank Soto para la asignatura de Teoría de Lenguajes Formales en la Universidad del Quindío.
