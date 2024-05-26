# Trabajo final de TLF: Analisis lexico sintactico en Python
Este repositorio se usará para almacenar el trabajo final de la asignatura Teoría de Lenguajes formales de ingeniería de sistemas y computación en universidad del Quindío por los estudiantes Santiago Velandia Gallo y Frank Soto

# Análisis Léxico:

Define y reconoce una serie de tokens que representan operadores aritméticos, relacionales, lógicos, símbolos de apertura y cierre, palabras reservadas, identificadores y valores.
Usa PLY (Python Lex-Yacc) para convertir una cadena de entrada en una secuencia de tokens.

# Análisis Sintáctico:

Define reglas gramaticales básicas para reconocer y procesar asignaciones y expresiones aritméticas.
Utiliza estas reglas para generar un árbol de derivación basado en la estructura del código de entrada.

# Construcción y Visualización del Árbol de Derivación:

Usa una clase TreeNode para construir el árbol de derivación.
Genera un archivo PNG del árbol de derivación utilizando Pydot y Graphviz.
Muestra el árbol de derivación en una ventana gráfica utilizando Tkinter y Pillow.

## Para usar este proyecto es importate instalar Python y las siguientes librerias de Python
### pip install ply pydot pillow
#### tambien puedes usar: pip install -r requirements.txt

### Tambien es necesario instalar https://graphviz.org/download/
Después de instalar Graphviz, asegúrate de agregar la ubicación de la herramienta "dot" a tu variable de entorno PATH. Esto permitirá que PyDot pueda encontrar y utilizar la herramienta "dot" correctamente.
Para agregar la ubicación de la herramienta "dot" a tu variable de entorno PATH, sigue estos pasos:

Encuentra la ubicación donde se instaló Graphviz en tu sistema. Por lo general, la herramienta "dot" se instala en la carpeta bin dentro del directorio de instalación de Graphviz.

Copia la ruta completa del directorio donde se encuentra la herramienta "dot".

Abre el Panel de control de Windows.

Haz clic en "Sistema y seguridad".

Haz clic en "Sistema".

En el panel izquierdo, haz clic en "Configuración avanzada del sistema".

En la ventana de Propiedades del sistema, haz clic en el botón "Variables de entorno".

En la sección "Variables del sistema", busca la variable llamada "PATH" y selecciónala.

Haz clic en el botón "Editar...".

En la ventana de Edición de variables del sistema, haz clic en el botón "Nuevo" y pega la ruta que copiaste en el paso 2.

Haz clic en "Aceptar" en todas las ventanas para guardar los cambios y cerrarlas.
