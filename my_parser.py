# Definir las reglas gramaticales y el analizador sintáctico.
import ply.yacc as yacc
from tokens import tokens

# Precedencia y asociatividad de operadores
precedence = (
    ('left', 'PS', 'MS'),
    ('left', 'TS', 'DB', 'MOD'),
    ('right', 'PW', 'SQ'),
)

# Reglas gramaticales
def p_program(p):
    'program : statement_list'
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list SEMICOLON statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_statement(p):
    '''statement : assignment
                 | expression'''
    p[0] = p[1]

def p_assignment(p):
    'assignment : NEWVAL ASSIGN expression'
    p[0] = ('assign', p[1], p[3])

def p_expression(p):
    '''expression : expression PS term
                  | expression MS term
                  | term'''
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
            | factor'''
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
                | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_error(p):
    print("Syntax error")

# Construir el parser
parser = yacc.yacc()
