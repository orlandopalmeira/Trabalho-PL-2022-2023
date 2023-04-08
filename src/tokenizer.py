import ply.lex as lex

# tokens
tokens = (
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'EQUALS',
    'STRING',
    'INTEGER',
    'DOT',
    'FLOAT',
    'BOOLEAN',
    'DATE',
    'TIME',
    'DATETIME',
    'FIELD',
    'KEY', 
    'OBJECT',
    'COMMENT'
)

t_ANY_COMMA = r'\,'
t_DOT = r'\.'
t_FIELD = r'[a-zA-Z_][a-zA-Z0-9_]*\s*(?=\=)'
t_READINGVALUE_KEY = r'[a-zA-Z_]\w*\s*(?=\=)'
t_OBJECT = r'[a-zA-Z]\w*'

states = (('READINGVALUE','exclusive'),)
stack = [] # ajuda a validar o fecho de listas e dicionários

# Ignorar espaços em branco e tabulações
t_ANY_ignore = ' \t'

# Lidar com \n
def t_ANY_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Lidar com erros
def t_ANY_error(t):
    raise SyntaxError(f"Caracter ilegal '{t.value[0]}' (line {t.lexer.lineno})")

# Ignorar comentarios
def t_ANY_COMMENT(t):
    r'\#.*(?=\n)'

t_READINGVALUE_EQUALS = r'\='
def t_EQUALS(t):
    r'\='
    t.lexer.begin('READINGVALUE')
    return t

t_LBRACKET = r'\['
def t_READINGVALUE_LBRACKET(t):
    r'\['
    global stack
    stack.append('[')
    return t

t_RBRACKET = r'\]'
def t_READINGVALUE_RBRACKET(t):
    r'\]'
    global stack
    if stack.pop() == '[':
        if not stack:
            t.lexer.begin('INITIAL')
        return t
    else:
        raise SyntaxError(f"Error closing list: the char '{t.value[0]}' (line {t.lexer.lineno}) is not compatible with the current structure.")

def t_READINGVALUE_LBRACE(t):
    r'\{'
    global stack
    stack.append('{')
    return t

def t_READINGVALUE_RBRACE(t):
    r'\}'
    global stack
    if stack.pop() == '{':
        if not stack:
            t.lexer.begin('INITIAL')
        return t
    else:
        raise SyntaxError(f"Error closing dictionary: the char '{t.value[0]}' (line {t.lexer.lineno}) is not compatible with the current structure.")

def t_READINGVALUE_BOOLEAN(t):
    r'\btrue\b|\bfalse\b'
    global stack
    if not stack: # só pode voltar ao estado inicial se estiver garantido que este boolean não está dentro de uma lista/dicionário e, para isso, verificamos se a stack não tem nada
        t.lexer.begin('INITIAL')
    return t

def t_READINGVALUE_DATETIME(t):
    r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}-\d{2}:\d{2}'
    global stack
    if not stack: # só pode voltar ao estado inicial se estiver garantido que este datetime não está dentro de uma lista/dicionário e, para isso, verificamos se a stack não tem nada
        t.lexer.begin('INITIAL')
    return t

def t_READINGVALUE_DATE(t):
    r'\d{4}-\d{2}-\d{2}'
    global stack
    if not stack: # só pode voltar ao estado inicial se estiver garantido que este date não está dentro de uma lista/dicionário e, para isso, verificamos se a stack não tem nada
        t.lexer.begin('INITIAL')
    return t

def t_READINGVALUE_TIME(t):
    r'\d{2}:\d{2}:\d{2}'
    global stack
    if not stack: # só pode voltar ao estado inicial se estiver garantido que este time não está dentro de uma lista/dicionário e, para isso, verificamos se a stack não tem nada
        t.lexer.begin('INITIAL')
    return t

def t_READINGVALUE_STRING(t):
    r'\"[^"]*\"|\'[^\']*\''
    global stack
    if not stack: # só pode voltar ao estado inicial se estiver garantido que esta string não está dentro de uma lista/dicionário e, para isso, verificamos se a stack não tem nada
        t.lexer.begin('INITIAL')
    return t


def t_READINGVALUE_FLOAT(t):
    r'\d+\.\d+'
    global stack
    if not stack: # só pode voltar ao estado inicial se estiver garantido que este float não está dentro de uma lista/dicionário e, para isso, verificamos se a stack não tem nada
        t.lexer.begin('INITIAL')
    return t

def t_READINGVALUE_INTEGER(t):
    r'\d+'
    global stack
    if not stack: # só pode voltar ao estado inicial se estiver garantido que este integer não está dentro de uma lista/dicionário e, para isso, verificamos se a stack não tem nada
        t.lexer.begin('INITIAL')
    return t

lexer = lex.lex()
data = '''
# This is a TOML document

title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00

[database]
enabled = true
ports = [ 8000, 8001, 8002 ]
data = [ ["delta", "phi"], [3.14] ]
temp_targets = { cpu = 79.5, case = 72.0 }

[servers]

    [servers.alpha]
    ip = "10.0.0.1"
    role = "frontend"

[servers.beta]
ip = "10.0.0.2"
role = "backend"
'''
lexer.input(data)

for tok in lexer:
    print(tok)