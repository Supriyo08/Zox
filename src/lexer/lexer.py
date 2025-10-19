# Very small lexer for the prototype
import re

token_spec = [
    ('NUMBER',   r'\d+'),
    ('STRING',   r'".*?"'),
    ('NAME',     r'[A-Za-z_][A-Za-z0-9_]*'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('LBRACE',   r'\{'),
    ('RBRACE',   r'\}'),
    ('COMMA',    r','),
    ('EQ',       r'='),
    ('OP',       r'[+\-*/]'),
    ('NEWLINE',  r'\n'),
    ('SKIP',     r'[ \t]+'),
    ('MISMATCH', r'.'),
]

master_pat = re.compile('|'.join('(?P<%s>%s)' % pair for pair in token_spec))

def tokenize(code):
    for mo in master_pat.finditer(code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            yield ('NUMBER', int(value))
        elif kind == 'STRING':
            yield ('STRING', value[1:-1])
        elif kind == 'NAME':
            yield ('NAME', value)
        elif kind == 'SKIP' or kind == 'NEWLINE':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected: {value}')
        else:
            yield (kind, value)
