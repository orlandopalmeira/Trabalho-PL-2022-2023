import ply.lex as lex
import re

def remove_quotes(string):
    res = re.sub(r'^(\"\"\"|\'\'\'|\"|\')((?:.|\n)*)\1$', r'\2', string).lstrip("\n")
    return res

def parse_bool(string):
    return True if string == 'true' else False
    
def find_column(token):
    text = token.lexer.lexdata
    line_start = text.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Retorna a linha do token em questão
def getline(token) -> str:
    i:int = token.lineno
    text = token.lexer.lexdata
    lines = text.split('\n')
    return lines[i-1]

tokens = [
    'COMMENT',
    'KEY',
    'STRING',
    'INT',
    'FLOAT',
    'BOOL',
    'OFFSETDATETIME',
    'LOCALDATETIME',
    'LOCALDATE',
    'LOCALTIME',
    'TABLE', # object
    'OPENPR', # parenteses rectos
    'CLOSEPR',
    'OPENCHV', # chavetas
    'CLOSECHV',
    'DOT',
    'EQUAL',
    'COMMA',
    'NEWLINE'
]

states = [('RVALUE','exclusive'),
          ('RTABLE','exclusive'),
          ('RARRAY','exclusive'),
          ('RDICT' ,'exclusive')]

# INITIAL
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_KEY(t):
    r'[\w\-]+|\"[\w\.\-]+\"|\'[\w\.\-]+\''
    # t.lexer.push_state(t.lexer.lexstate)
    # t.lexer.begin('RVALUE')
    t.value = remove_quotes(t.value)
    t.lexer.push_state('RVALUE')
    return t

def t_DOT(t):
    r'\.'
    return t

def t_OPENPR(t):
    r'\['
    # t.lexer.push_state(t.lexer.lexstate)
    # t.lexer.begin('RTABLE')
    t.lexer.push_state('RTABLE')
    return t

def t_CLOSEPR(t):
    r'\]'
    t.lexer.pop_state()
    return t

# RTABLE
def t_RTABLE_OPENPR(t):
    r'\['
    # t.lexer.push_state(t.lexer.lexstate)
    # t.lexer.begin('RTABLE')
    t.lexer.push_state('RTABLE')
    return t

def t_RTABLE_TABLE(t):
    r'[\w\-]+|\"[\w\-\. ]+\"|\'[\w\-\. ]+\''
    t.value = remove_quotes(t.value)
    return t

def t_RTABLE_DOT(t):
    r'\.'
    return t

def t_RTABLE_CLOSEPR(t):
    r'\]'
    t.lexer.pop_state()
    return t


# RVALUE
def t_RVALUE_DOT(t):
    r'\.'
    t.lexer.pop_state()
    return t

def t_RVALUE_OFFSETDATETIME(t):
    r'\d{4}\-\d{2}\-\d{2}[T ]\d{2}\:\d{2}\:\d+\.\d+\-\d{2}\:\d{2}|\d{4}\-\d{2}\-\d{2}[T ]\d{2}\:\d{2}\:\d{2}\-\d{2}\:\d{2}|\d{4}\-\d{2}\-\d{2}[T ]\d{2}\:\d{2}\:\d{2}Z'
    t.lexer.pop_state()
    return t

def t_RVALUE_LOCALDATETIME(t):
    r'\d{4}\-\d{2}\-\d{2}[T ]\d{2}\:\d{2}\:\d{2}(\.\d+)?'
    t.lexer.pop_state()
    return t

def t_RVALUE_LOCALDATE(t):
    r'\d{4}\-\d{2}\-\d{2}'
    t.lexer.pop_state()
    return t

def t_RVALUE_LOCALTIME(t):
    r'\d{2}\:\d{2}\:\d{2}(\.\d+)?'
    t.lexer.pop_state()
    return t

def t_RVALUE_EQUAL(t):
    r'='
    return t

def t_RVALUE_STRING(t):
    r'\"\"\"[^\"]*\"\"\"|\'\'\'[^\']*\'\'\'|\"[^\"\n]*\"|\'[^\'\n]*\''
    t.value = remove_quotes(t.value)
    t.lexer.pop_state()
    return t

def t_RVALUE_FLOAT(t):
    r'(\+|\-)?(\d+e(\+|\-)?\d+|\d+\.\d+)'
    t.value = float(t.value)
    t.lexer.pop_state()
    return t

def t_RVALUE_INT(t):
    r'(\+|\-)?\d+'
    t.value = int(t.value)
    t.lexer.pop_state()
    return t

def t_RVALUE_BOOL(t):
    r'\b(true|false)\b'
    t.value = parse_bool(t.value)
    t.lexer.pop_state()
    return t

def t_RVALUE_OPENPR(t):
    r'\['
    # t.lexer.push_state(t.lexer.lexstate)
    # t.lexer.begin('RARRAY')
    t.lexer.pop_state() # não vamos ler um valor, mas sim uma estrutura
    t.lexer.push_state('RARRAY')
    return t

def t_RVALUE_CLOSEPR(t):
    r'\]'
    t.lexer.pop_state()
    return t

def t_RVALUE_OPENCHV(t):
    r'\{'
    # t.lexer.push_state(t.lexer.lexstate)
    # t.lexer.begin('RDICT')
    t.lexer.pop_state() # não vamos ler um valor, mas sim uma estrutura
    t.lexer.push_state('RDICT')
    return t

def t_RVALUE_CLOSECHV(t):
    r'\}'
    t.lexer.pop_state()
    return t

# RARRAY
def t_RARRAY_OFFSETDATETIME(t):
    r'\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d+\.\d+\-\d{2}\:\d{2}|\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}\-\d{2}\:\d{2}|\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}Z'
    return t

def t_RARRAY_LOCALDATETIME(t):
    r'\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}(\.\d+)?'
    return t

def t_RARRAY_LOCALDATE(t):
    r'\d{4}\-\d{2}\-\d{2}'
    return t

def t_RARRAY_LOCALTIME(t):
    r'\d{2}\:\d{2}\:\d{2}(\.\d+)?'
    return t

def t_RARRAY_STRING(t):
    r'\"\"\"[^\"]*\"\"\"|\'\'\'[^\']*\'\'\'|\"[^\"\n]*\"|\'[^\'\n]*\''
    t.value = remove_quotes(t.value)
    return t

def t_RARRAY_FLOAT(t):
    r'(\+|\-)?(\d+e(\+|\-)?\d+|\d+\.\d+)'
    t.value = float(t.value)
    return t

def t_RARRAY_INT(t):
    r'(\+|\-)?\d+'
    t.value = int(t.value)
    return t

def t_RARRAY_BOOL(t):
    r'\b(true|false)\b'
    t.value = parse_bool(t.value)
    return t

def t_RARRAY_COMMA(t):
    r'\,'
    return t

def t_RARRAY_OPENPR(t):
    r'\['
    # t.lexer.push_state(t.lexer.lexstate)
    # t.lexer.begin('RARRAY')
    t.lexer.push_state('RARRAY')
    return t

def t_RARRAY_CLOSEPR(t):
    r'\]'
    t.lexer.pop_state()
    return t

def t_RARRAY_OPENCHV(t):
    r'\{'
    # t.lexer.push_state(t.lexer.lexstate)
    # t.lexer.begin('RDICT')
    t.lexer.push_state('RDICT')
    return t

def t_RARRAY_CLOSECHV(t):
    r'\}'
    t.lexer.pop_state()
    return t

# RDICT
def t_RDICT_KEY(t):
    r'[\w\-]+|\"[\w\.\-]+\"|\'[\w\.\-]+\''
    # t.lexer.push_state(t.lexer.lexstate)
    # t.lexer.begin('RVALUE')
    t.value = remove_quotes(t.value)
    t.lexer.push_state('RVALUE')
    return t

def t_RDICT_COMMA(t):
    r'\,'
    return t

def t_RDICT_OPENPR(t):
    r'\['
    # t.lexer.push_state(t.lexer.lexstate)
    # t.lexer.begin('RARRAY')
    t.lexer.push_state('RARRAY')
    return t

def t_RDICT_CLOSEPR(t):
    r'\]'
    t.lexer.pop_state()
    return t

def t_RDICT_OPENCHV(t):
    r'\{'
    # t.lexer.push_state(t.lexer.lexstate)
    # t.lexer.begin('RDICT')
    t.lexer.push_state('RDICT')
    return t

def t_RDICT_CLOSECHV(t):
    r'\}'
    t.lexer.pop_state()
    return t

t_ANY_ignore = '\t '

def t_ANY_error(t):
    # print(f'Erro em "{t.value}"')
    coluna = find_column(t)
    line = getline(t)
    print(f"Erro de parsing: sintaxe inválida na linha {t.lineno}, coluna {coluna}.")
    print(f"{line.rstrip()}")
    print(" " * (coluna - 1) + "^")
    print("Execução interrompida!")
    exit(1)

def t_ANY_COMMENT(t):
    r'\#.*\n'
    t.lexer.lineno += 1

def t_ANY_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


lexer = lex.lex()

with open('/home/orlando/Desktop/Trabalho-PL-2022-2023/tests/valid/array/string-quote-comma-2.toml') as f:
    lexer.input(f.read())

for token in lexer:
    print(f'{token}: {lexer.current_state()}')