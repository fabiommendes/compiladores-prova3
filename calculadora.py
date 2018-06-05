import ox
from math import sqrt
from datetime import date
from ox.helpers import identity, cons, singleton, constant, first, second, last

#
# Contexto de avaliação global
# (Atalho para guardar valores temporários das variáveis)
#
variables = {}


#
# Parser
#
def make_parser(lexer):
    parser = ox.make_parser([
        ("module : expr", identity),
        ("expr : atom", identity),
        ("atom : number", identity),
        ("number : NUMBER", float),
        # ...
    ])
    return lambda src: parser(lexer(src))


#
# Lexer
#
def make_lexer():
    return ox.make_lexer([
        ('NUMBER', r'[+-]?\d+(\.\d+)?'),
        ('SYMBOL', r'[a-zA-Z][_a-zA-Z0-9]*'),
        ('OP_SUM', r'[+-]'),
        ('OP_MUL', r'[*/]'),
        ('CONTROL', r'[(),=;%]'),
    ])


#
# Funções úteis
#
def compute_operation(x, op, y):
    # Números são guardados como tuplas de (valor, erro)
    xm, ex = x
    ym, ey = y
    
    if op == '+':
        return (xm + ym, ex + ey)
    elif op == '-':
        return (xm - ym, ex + ey)
    elif op == '*':
        return (xm * ym, abs(ym) * ex + abs(xm) * ey)
    elif op == '/':
        return (xm / ym, (abs(ym) * ex + abs(xm) * ey) / ym**2)
    else:
        raise ValueError('Invalid operator')
    

#
# Cria o parser
#
evaluate = make_parser(make_lexer())

def main():
    while True:
        src = input('$ ')
        if not src:  
            if input('Sair (s/n)?') == 's':
                raise SystemExit(0)
        else:
            x, err = evaluate(src)
            print('out: %f(%f)' % (x, err))


# Le e processa um arquivo JSON+
if __name__ == '__main__':
    main()