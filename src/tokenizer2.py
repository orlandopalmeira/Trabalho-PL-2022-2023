import ply.lex as lex
import re

tokens = [
    'COMMENT'
    'KEY',
    # 'VALUE',
    'STRING',
    'INTEGER',
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
    'COMMA'
]

states = [('RVALUE','exclusive'),
          ('RTABLE','exclusive'),
          ('RARRAY','exclusive'),
          ('RDICT' ,'exclusive')]

# INITIAL
def t_KEY(t):
    r'[\w\-]+|\"[\w\.\-]+\"|\'[\w\.\-]+\''
    # t.lexer.push_state(t.lexer.lexstate)
    # t.lexer.begin('RVALUE')
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
    r'[\w\-]+|\"[\w\-]+\"|\'[\w\-]+\''
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

def t_RVALUE_newline(t):
    r'\n'
    t.lexer.lineno += 1
    t.lexer.pop_state()

def t_RVALUE_OFFSETDATETIME(t):
    r'\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d+\.\d+\-\d{2}\:\d{2}|\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}\-\d{2}\:\d{2}|\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}Z'
    t.lexer.pop_state()
    return t

def t_RVALUE_LOCALDATETIME(t):
    r'\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}(\.\d+)?'
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
    t.value = re.sub(r'^("""|\'\'\'|"|\')(.*)\1$', r'\2', t.value)
    t.lexer.pop_state()
    return t

def t_RVALUE_FLOAT(t):
    r'(\+|\-)?(\d+e(\+|\-)?\d+|\d+\.\d+)'
    t.lexer.pop_state()
    return t

def t_RVALUE_INTEGER(t):
    r'(\+|\-)?\d+'
    t.lexer.pop_state()
    return t

def t_RVALUE_BOOL(t):
    r'\b(true|false)\b'
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
    t.value = re.sub(r'^("""|\'\'\'|"|\')(.*)\1$', r'\2', t.value)
    return t

def t_RARRAY_FLOAT(t):
    r'(\+|\-)?(\d+e(\+|\-)?\d+|\d+\.\d+)'
    return t

def t_RARRAY_INTEGER(t):
    r'(\+|\-)?\d+'
    return t

def t_RARRAY_BOOL(t):
    r'\b(true|false)\b'
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
    t.lexer.push_state('RVALUE')
    return t

def t_RDICT_EQUAL(t):
    r'='
    return t

def t_RDICT_STRING(t):
    r'\"\"\"[^\"]*\"\"\"|\'\'\'[^\']*\'\'\'|\"[^\"\n]*\"|\'[^\'\n]*\''
    t.value = re.sub(r'^("""|\'\'\'|"|\')(.*)\1$', r'\2', t.value)
    return t

def t_RDICT_OFFSETDATETIME(t):
    r'\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d+\.\d+\-\d{2}\:\d{2}|\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}\-\d{2}\:\d{2}|\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}Z'
    return t

def t_RDICT_LOCALDATETIME(t):
    r'\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}(\.\d+)?'
    return t

def t_RDICT_LOCALDATE(t):
    r'\d{4}\-\d{2}\-\d{2}'
    return t

def t_RDICT_LOCALTIME(t):
    r'\d{2}\:\d{2}\:\d{2}(\.\d+)?'
    return t

def t_RDICT_FLOAT(t):
    r'(\+|\-)?(\d+e(\+|\-)?\d+|\d+\.\d+)'
    return t

def t_RDICT_INTEGER(t):
    r'(\+|\-)?\d+'
    return t

def t_RDICT_BOOL(t):
    r'\b(true|false)\b'
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
    print(f'Erro em "{t.value}"')
    exit(1)

def t_ANY_COMMENT(t):
    r'\#.*'
    # return t

def t_ANY_newline(t):
    r'\n'
    t.lexer.lineno += 1


lexer = lex.lex()

with open('examples/data1.toml') as f:
    lexer.input(f.read())

for token in lexer:
    print(f'{token}: {lexer.current_state()}')