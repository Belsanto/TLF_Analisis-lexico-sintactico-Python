# my_parser.py
# Importa la biblioteca yacc de PLY para generar el analizador sintáctico.
import ply.yacc as yacc
from tokens import tokens  # Importa los tokens generados por el analizador léxico.

# Precedencia y asociatividad de los operadores.
precedence = (
    ('left', 'PS', 'MS'),  # Precedencia y asociatividad para suma y resta.
    ('left', 'TS', 'DB', 'MOD'),  # Precedencia y asociatividad para multiplicación, división y módulo.
    ('right', 'PW', 'SQ'),  # Precedencia y asociatividad para potencia y raíz cuadrada.
)

# Reglas gramaticales para el parser.
def p_program(p):
    'program : statement_list'  # Regla para el programa.
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                        | statement_list SEMICOLON statement'''  # Regla para una lista de declaraciones.
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_statement(p):
    '''statement : assignment
                    | expression'''  # Regla para una declaración, que puede ser una asignación o una expresión.
    p[0] = p[1]

def p_assignment(p):
    'assignment : NEWVAL ASSIGN expression'  # Regla para una asignación.
    p[0] = ('assign', p[1], p[3])

def p_expression(p):
    '''expression : expression PS term
                    | expression MS term
                    | term'''  # Regla para una expresión, que puede ser una suma/resta de términos o un solo término.
    if len(p) == 4:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
    else:
        p[0] = p[1]

def p_term(p):
    '''term : term TS factor
            | term DB factor
            | term MOD factor
            | factor'''  # Regla para un término, que puede ser un producto/división/módulo de factores o un solo factor.
    if len(p) == 4:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
        elif p[2] == '%':
            p[0] = p[1] % p[3]
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : NUMBER
                | REAL
                | LPAREN expression RPAREN'''  # Regla para un factor, que puede ser un número, un número real o una expresión entre paréntesis.
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' (line {p.lineno})")  # Maneja errores de sintaxis.
    else:
        print("Syntax error at EOF")

# Construye el parser.
parser = yacc.yacc()
