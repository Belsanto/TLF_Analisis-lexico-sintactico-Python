# tokens.py
# Definir los tokens y el analizador léxico.

import ply.lex as lex

# Lista de tokens
tokens = [
    'PS', 'MS', 'TS', 'DB', 'PW', 'SQ', 'MOD',  # Operadores aritméticos
    'EQ', 'GTOE', 'LTOE', 'GT', 'LT', 'EQNOT',  # Operadores relacionales
    'IAI', 'IOI', 'INI',                       # Operadores lógicos
    'ASSIGN',                                   # Operador de asignación
    'LPAREN', 'LBRACE', 'LQUESTION',            # Símbolos de abrir
    'RPAREN', 'RBRACE', 'RQUESTION',            # Símbolos de cerrar
    'BREVE',                                     # Terminal y/o inicial
    'SEMICOLON',                                 # Separador de sentencias
    'LOOPFOR', 'WHILEFOR',                       # Palabras reservadas para bucle
    'IFTHIS', 'OTHERWISE',                       # Palabras para decisión
    'ICLASSI', 'INTI', 'IENUMI',                 # Palabras para la clase
    'NEWVAL', 'NEWFUNC',                         # Identificadores
    'NUMBER', 'REAL', 'STRING', 'CHAR',          # Valores de asignación
    'NEWINT', 'NEWNUM', 'NEWEXT', 'NEWCHAR',     # Tipos de datos
    'COMMENT',                                   # Comentarios
    'HEXADECIMAL'                                # Hexadecimal
]

# Definiciones regulares para tokens simples
t_PS = r'\+'
t_MS = r'-'
t_TS = r'\*'
t_DB = r'/'
t_PW = r'\*\*'
t_SQ = r'sqrt'
t_MOD = r'%'
t_EQ = r'=='
t_GTOE = r'>='
t_LTOE = r'<='
t_GT = r'>'
t_LT = r'<'
t_EQNOT = r'!='
t_IAI = r'&&'
t_IOI = r'\|\|'
t_INI = r'!'
t_ASSIGN = r':='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LQUESTION = r'\¿'
t_RQUESTION = r'\?'
t_BREVE = r'BREVE'
t_SEMICOLON = r'\|'
t_LOOPFOR = r'LOOPFOR'
t_WHILEFOR = r'WHILEFOR'
t_IFTHIS = r'IFTHIS'
t_OTHERWISE = r'OTHERWISE'
t_ICLASSI = r'ICLASSI'
t_INTI = r'INTI'
t_IENUMI = r'IENUMI'
t_NEWVAL = r'NEWVAL'
t_NEWFUNC = r'NEWFUNC'
t_NEWINT = r'NEWINT'
t_NEWNUM = r'NEWNUM'
t_NEWEXT = r'NEWEXT'
t_NEWCHAR = r'NEWCHAR'

# Definiciones regulares para valores
def t_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # Quitar las comillas
    return t

def t_CHAR(t):
    r'\'.\''
    t.value = t.value[1:-1]  # Quitar las comillas
    return t

def t_HEXADECIMAL(t):
    r'H[A-Fa-f0-9]+'
    t.value = int(t.value[1:], 16)
    return t

# Definiciones para comentarios
def t_COMMENT(t):
    r'B \{.*?\} V'
    pass  # Ignorar los comentarios

# Ignorar espacios, tabs y saltos de línea
t_ignore = ' \t\n'

# Manejo de errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
