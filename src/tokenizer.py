import ply.lex as lex
import re
import math
from dateutil.parser import parse as parseDateTime
from datetime import datetime


def find_column(token):
    '''
    Retorna o número da coluna em que o token se encontra na linha.
    '''
    text = token.lexer.lexdata
    line_start = text.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def getline(token, i = None) -> str:
    '''
    Retorna a linha do token dado como argumento, podendo ser especificado um índice, opcionalmente.
    '''
    if not i:
        i = token.lineno - 1
    text = token.lexer.lexdata
    lines = text.split('\n')
    return lines[i]

def rem_quotes(text):
    return re.sub(r'^(\"\"\"|\'\'\'|\"|\')((?:.|\n)*)\1$', r'\2', text)

def treat_basic_string(text):
    text = rem_quotes(text)
    # text = text.replace('\\"', '"').replace('\\\\','\\')
    text = text.encode().decode('unicode_escape')
    return text

def treat_literal_string(text):
    text = rem_quotes(text)
    return text

def treat_single_string(text):
    if text[0]== '"':
        return treat_basic_string(text)
    else:
        return treat_literal_string(text)

def treat_BML_string(text):
    text = rem_quotes(text)
    text = re.sub(r'^\n', '', text) # Faz trim do \n que esteja no inicio da frase
    text = remove_leb(text)
    # text = text.replace('\\"', '"').replace('\\\\','\\')
    text = text.encode().decode('unicode_escape')
    return text

def treat_LML_string(text):
    text = rem_quotes(text)
    text = re.sub(r'^\n', '', text) # Faz trim do \n que esteja no inicio da frase
    return text

def treat_keys(text):
    if text[0] == '"' or text[0] == "'":
        text = treat_single_string(text)
    return text

def remove_leb(text):
    '''
    Leb -> Line Ending Backslash
    '''
    regex = re.compile(r'\\[\s\n]+')
    return re.sub(regex,'', text)

def isValidInt(inteiro):
    if inteiro > pow(2,63)-1 or inteiro < -pow(2,63):
        print(f"Cannot parse BigInt {inteiro}!!")
        exit()
        return False
    return True

def parse_bool(text):
    return True if text == 'true' else False
    

tokens = [
    'COMMENT',
    'KEY',
    'STRING',
    'LMLSTRING',
    'BMLSTRING',
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
    r'[\w\-]+|\"(?:(?=(?P<t2>\\?))(?P=t2).)*?\"|\'.*?\''
    # t.lexer.push_state(t.lexer.lexstate)
    # t.lexer.begin('RVALUE')
    t.value = treat_keys(t.value)
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
    # r'[\w\-]+|\"[^\"\n]+\"|\'[^\'\n]+\''
    r'[\w\-]+|\"(?:(?=(?P<t2>\\?))(?P=t2).)*?\"|\'.*?\''
    t.value = treat_keys(t.value)
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
    r'\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}\:\d{2}\:\d+\.\d+[\-\+]\d{2}\:\d{2}|\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}\:\d{2}\:\d{2}[\-\+]\d{2}\:\d{2}|\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}\:\d{2}\:\d{2}(\.\d+)?[Zz]'
    # t.value = t.value.replace(' ','T')
    # t.value = re.sub(r'[Tt]',' ',t.value)
    # t.value = t.value.replace('z','Z')
    t.value = str(parseDateTime(t.value))
    t.lexer.pop_state()
    return t

def t_RVALUE_LOCALDATETIME(t):
    r'\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}\:\d{2}\:\d{2}(\.\d+)?'
    # t.value = re.sub(r'[Tt]',' ',t.value)
    t.value = str(parseDateTime(t.value))
    t.lexer.pop_state()
    return t

def t_RVALUE_LOCALDATE(t):
    r'\d{4}\-\d{2}\-\d{2}'
    t.lexer.pop_state()
    t.value = str(parseDateTime(t.value).date())
    return t

def t_RVALUE_LOCALTIME(t):
    r'\d{2}\:\d{2}\:\d{2}(\.\d+)?'
    t.lexer.pop_state()
    t.value = str(parseDateTime(t.value).time())
    return t

def t_RVALUE_EQUAL(t):
    r'='
    return t

# Basic Multi-line
def t_RVALUE_BMLSTRING(t):
    r'""""""|"""(?:"){0,2}(?:(?=(?P<t0>\\?))(?P=t0)(?:.|\n))*?"""(?:"){0,2}'
    t.value = treat_BML_string(t.value)
    t.lexer.pop_state()
    t.type = 'STRING'
    return t

# Literal Multi-line
def t_RVALUE_LMLSTRING(t):
    r'\'\'\'\'\'\'|\'\'\'(?:\'){0,2}(.|\n)*?\'\'\'(?:\'){0,2}'
    t.value = treat_LML_string(t.value)
    t.lexer.pop_state()
    t.type = 'STRING'
    return t

def t_RVALUE_STRING(t):
    # r'(""")(?:"){0,2}[^\1]*?"""(?:"){0,2}|\'\'\'[^\']*\'\'\'|(?P<quote>[\"\'])(?:(?=(?P<t2>\\?))(?P=t2).)*?(?P=quote)'
    r'\"(?:(?=(?P<t2>\\?))(?P=t2).)*?\"|\'.*?\''
    t.value = treat_single_string(t.value)
    t.lexer.pop_state()
    return t


def t_RVALUE_FLOAT(t):
    # r'(\+|\-)?(\d+e(\+|\-)?\d+|\d+\.\d+)'
    # r'(\+|\-)?(\d+(\.\d+)?[eE](\+|\-)?\d+|\d+\.\d+)'
    r'(\+|\-)?(\d(\_?\d)*(\.\d(\_?\d)*)?[eE](\+|\-)?\d(\_?\d)*|\d(\_?\d)*\.\d(\_?\d)*)'
    t.value = float(t.value)
    t.lexer.pop_state()
    return t

def t_RVALUE_INF(t):
    r'(\+|\-)?inf'
    if t.value[0] == "-":
        t.value = -math.inf
    else:
        t.value = math.inf
    t.type = "FLOAT"
    t.lexer.pop_state()
    return t

def t_RVALUE_NAN(t):
    r'(\+|\-)?nan'
    t.value = math.nan
    t.type = "FLOAT"
    t.lexer.pop_state()
    return t

def t_RVALUE_INTHEX(t):
    r'0x[0-9a-zA-Z](\_?[0-9a-zA-Z])*'
    t.value = int(t.value, 16)
    flag = isValidInt(t.value)
    t.type = "INT"
    t.lexer.pop_state()
    return t

def t_RVALUE_INTOCT(t):
    r'0o[0-7](_?[0-7])*'
    t.value = int(t.value, 8)
    flag = isValidInt(t.value)
    t.type = "INT"
    t.lexer.pop_state()
    return t

def t_RVALUE_INTBIN(t):
    r'0b[01](_?[01])*'
    t.value = int(t.value, 2)
    flag = isValidInt(t.value)
    t.type = "INT"
    t.lexer.pop_state()
    return t

def t_RVALUE_INT(t):
    r'(\+|\-)?(0|[1-9](?:\_?\d)*)' # não pode começar em 0
    t.value = int(t.value)
    flag = isValidInt(t.value)
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
    r'\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}\:\d{2}\:\d+\.\d+[\-\+]\d{2}\:\d{2}|\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}\:\d{2}\:\d{2}[\-\+]\d{2}\:\d{2}|\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}\:\d{2}\:\d{2}(\.\d+)?[Zz]'
    # t.value = re.sub(r'[Tt]',' ',t.value)
    # t.value = t.value.replace('z','Z')
    t.value = str(parseDateTime(t.value))
    return t

def t_RARRAY_LOCALDATETIME(t):
    r'\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}\:\d{2}\:\d{2}(\.\d+)?'
    # t.value = re.sub(r'[Tt]',' ',t.value)
    t.value = str(parseDateTime(t.value))
    return t

def t_RARRAY_LOCALDATE(t):
    r'\d{4}\-\d{2}\-\d{2}'
    t.value = str(parseDateTime(t.value).date())
    return t

def t_RARRAY_LOCALTIME(t):
    r'\d{2}\:\d{2}\:\d{2}(\.\d+)?'
    t.value = str(parseDateTime(t.value).time())
    return t

def t_RARRAY_BMLSTRING(t):
    r'""""""|"""(?:"){0,2}(?:(?=(?P<t0>\\?))(?P=t0)(?:.|\n))*?"""(?:"){0,2}'
    t.value = treat_BML_string(t.value)
    t.type = 'STRING'
    return t

def t_RARRAY_LMLSTRING(t):
    r'\'\'\'\'\'\'|\'\'\'(?:\'){0,2}(.|\n)*?\'\'\'(?:\'){0,2}'
    t.value = treat_LML_string(t.value)
    t.type = 'STRING'
    return t

def t_RARRAY_STRING(t):
    r'\"(?:(?=(?P<t2>\\?))(?P=t2).)*?\"|\'.*?\''
    t.value = treat_single_string(t.value)
    return t

def t_RARRAY_FLOAT(t):
    # r'(\+|\-)?(\d+e(\+|\-)?\d+|\d+\.\d+)'
    r'(\+|\-)?(\d+(\.\d+)?[eE](\+|\-)?\d+|\d+\.\d+)'
    t.value = float(t.value)
    return t

def t_RARRAY_INF(t):
    r'(\+|\-)?inf'
    if t.value[0] == "-":
        t.value = -math.inf
    else:
        t.value = math.inf
    t.type = "FLOAT"
    return t

def t_RARRAY_NAN(t):
    r'(\+|\-)?nan'
    t.value = math.nan
    t.type = "FLOAT"
    return t

def t_RARRAY_INTHEX(t):
    r'0x[0-9a-zA-Z](\_?[0-9a-zA-Z])*'
    t.value = int(t.value, 16)
    flag = isValidInt(t.value)
    t.type = "INT"
    return t

def t_RARRAY_INTOCT(t):
    r'0o[0-7](_?[0-7])*'
    t.value = int(t.value, 8)
    flag = isValidInt(t.value)
    t.type = "INT"
    return t

def t_RARRAY_INTBIN(t):
    r'0b[01](_?[01])*'
    t.value = int(t.value, 2)
    flag = isValidInt(t.value)
    t.type = "INT"
    return t

def t_RARRAY_INT(t):
    r'(\+|\-)?(0|[1-9](?:\_?\d)*)' # não pode começar em 0
    t.value = int(t.value)
    flag = isValidInt(t.value)
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
    # r'[\w\-]+|\"[^\"\n]*\"|\'[^\'\n]*\''
    r'[\w\-]+|\"(?:(?=(?P<t2>\\?))(?P=t2).)*?\"|\'.*?\''
    # t.lexer.push_state(t.lexer.lexstate)
    # t.lexer.begin('RVALUE')
    t.value = treat_keys(t.value)
    # t.value = remove_quotes(t.value)
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
    coluna = find_column(t)
    line = getline(t)
    print(f"Erro de parsing do tokenizer: sintaxe inválida na linha {t.lineno}, coluna {coluna}.")
    print(f"{line.rstrip()}")
    print(" " * (coluna - 1) + "^")
    print("Execução interrompida!")
    exit(1)

def t_ANY_COMMENT(t):
    r'\#.*'

def t_ANY_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


lexer = lex.lex()

# with open('examples/test.toml') as f:
#     lexer.input(f.read())

# for token in lexer:
#     print(f'{token}: {lexer.current_state()}')