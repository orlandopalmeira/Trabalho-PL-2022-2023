import ply.lex as lex
import sys
import re
import math
from dateutil.parser import parse as parseDateTime
from datetime import datetime


def find_column(token):
    '''
    Retorna o número da coluna em que o token se encontra na sua linha.
    '''
    text = token.lexer.lexdata
    line_start = text.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def getline(token) -> str:
    '''
    Retorna a string da linha do token dado como argumento.
    '''
    line = token.lineno - 1
    text = token.lexer.lexdata
    lines = text.split('\n')
    return lines[line]

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

def isValidInt(token):
    num = token.value
    MIN_INT = -2**63
    MAX_INT = 2**63 - 1
    if not MIN_INT <= num <= MAX_INT:
        col = find_column(token)
        line = getline(token).rstrip()

        # Mensagem de erro
        print("O número inteiro fornecido não pode ser representado sem perda de precisão.")
        # print("Por favor, forneça um valor inteiro de 64 bits com sinal válido, entre -9.223.372.036.854.775.808 e 9.223.372.036.854.775.807.")
        print(f"O inteiro inválido foi detetado na linha {token.lineno}, coluna {col}.")
        print(f"""\
  {line}
  {" " * (col-1)}^\
""")
        exit(1)

def parse_bool(text):
    return True if text == 'true' else False
    
class Lexer:
    
    tokens = [
        'KEY',
        'STRING',
        'INT',
        'FLOAT',
        'BOOL',
        'DATETIME',
        'TABLE', 
        'NEWLINE',
        'EOF',
    ]

    literals = [
        '[',
        ']',
        '{',
        '}',
        '.',
        '=',
        ','
    ]

    states = [('RVALUE','exclusive'),
              ('RTABLE','exclusive'),
              ('RARRAY','exclusive'),
              ('RDICT' ,'exclusive')]

    # INITIAL
    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t

    def t_KEY(self, t):
        r'[\w\-]+|\"(?:(?=(?P<t2>\\?))(?P=t2).)*?\"|\'.*?\''
        t.value = treat_keys(t.value)
        return t

    def t_dot(self, t):
        r'\.'
        t.type = '.'
        return t

    def t_openpr(self, t):
        r'\['
        t.type = '['
        t.lexer.push_state('RTABLE')
        return t

    def t_equal(self, t):
        r'='
        t.type = '='
        t.lexer.push_state('RVALUE')
        return t


    # RTABLE
    def t_RTABLE_openpr(self, t):
        r'\['
        t.type = '['
        t.lexer.push_state('RTABLE')
        return t

    def t_RTABLE_TABLE(self, t):
        r'[\w\-]+|\"(?:(?=(?P<t2>\\?))(?P=t2).)*?\"|\'.*?\''
        t.value = treat_keys(t.value)
        return t

    def t_RTABLE_dot(self, t):
        r'\.'
        t.type = '.'
        return t

    def t_RTABLE_closepr(self, t):
        r'\]'
        t.type = ']'
        t.lexer.pop_state()
        return t

    def t_RTABLE_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t


    # RVALUE
    def t_RVALUE_OFFSETDATETIME(self, t):
        r'\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}\:\d{2}\:\d+\.\d+[\-\+]\d{2}\:\d{2}|\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}\:\d{2}\:\d{2}[\-\+]\d{2}\:\d{2}|\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}\:\d{2}\:\d{2}(\.\d+)?[Zz]'
        t.value = str(parseDateTime(t.value))
        t.lexer.pop_state()
        t.type = 'DATETIME'
        return t

    def t_RVALUE_LOCALDATETIME(self, t):
        r'\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}\:\d{2}\:\d{2}(\.\d+)?'
        t.value = str(parseDateTime(t.value))
        t.lexer.pop_state()
        t.type = 'DATETIME'
        return t

    def t_RVALUE_LOCALDATE(self, t):
        r'\d{4}\-\d{2}\-\d{2}'
        t.lexer.pop_state()
        t.value = str(parseDateTime(t.value).date())
        t.type = 'DATETIME'
        return t

    def t_RVALUE_LOCALTIME(self, t):
        r'\d{2}\:\d{2}\:\d{2}(\.\d+)?'
        t.lexer.pop_state()
        t.value = str(parseDateTime(t.value).time())
        t.type = 'DATETIME'
        return t

    # Basic Multi-line
    def t_RVALUE_BMLSTRING(self, t):
        r'""""""|""""{0,2}(?:(?=(?P<t0>\\?))(?P=t0)(?:.|\n))*?""""{0,2}'
        t.value = treat_BML_string(t.value)
        t.lexer.pop_state()
        t.type = 'STRING'
        return t

    # Literal Multi-line
    def t_RVALUE_LMLSTRING(self, t):
        r'\'\'\'\'\'\'|\'\'\'\'{0,2}(.|\n)*?\'\'\'\'{0,2}'
        t.value = treat_LML_string(t.value)
        t.lexer.pop_state()
        t.type = 'STRING'
        return t

    def t_RVALUE_STRING(self, t):
        r'\"(?:(?=(?P<t2>\\?))(?P=t2).)*?\"|\'.*?\''
        t.value = treat_single_string(t.value)
        t.lexer.pop_state()
        return t

    def t_RVALUE_FLOAT(self, t):
        r'(\+|\-)?(\d(\_?\d)*(\.\d(\_?\d)*)?[eE](\+|\-)?\d(\_?\d)*|\d(\_?\d)*\.\d(\_?\d)*)'
        t.value = float(t.value)
        t.lexer.pop_state()
        return t

    def t_RVALUE_INF(self, t):
        r'(\+|\-)?inf'
        if t.value[0] == "-":
            t.value = -math.inf
        else:
            t.value = math.inf
        t.type = "FLOAT"
        t.lexer.pop_state()
        return t

    def t_RVALUE_NAN(self, t):
        r'(\+|\-)?nan'
        t.value = math.nan
        t.type = "FLOAT"
        t.lexer.pop_state()
        return t

    def t_RVALUE_INTHEX(self, t):
        r'0x[0-9a-fA-F](\_?[0-9a-fA-F])*'
        t.value = int(t.value, 16)
        isValidInt(t)
        t.type = "INT"
        t.lexer.pop_state()
        return t

    def t_RVALUE_INTOCT(self, t):
        r'0o[0-7](_?[0-7])*'
        t.value = int(t.value, 8)
        isValidInt(t)
        t.type = "INT"
        t.lexer.pop_state()
        return t

    def t_RVALUE_INTBIN(self, t):
        r'0b[01](_?[01])*'
        t.value = int(t.value, 2)
        isValidInt(t)
        t.type = "INT"
        t.lexer.pop_state()
        return t

    def t_RVALUE_INT(self, t):
        r'(\+|\-)?(0|[1-9](?:\_?\d)*)' # não pode começar em 0
        t.value = int(t.value)
        isValidInt(t)
        t.lexer.pop_state()
        return t

    def t_RVALUE_BOOL(self, t):
        r'\b(true|false)\b'
        t.value = parse_bool(t.value)
        t.lexer.pop_state()
        return t

    def t_RVALUE_openpr(self, t):
        r'\['
        t.type = '['
        t.lexer.pop_state() # não vamos ler um valor, mas sim uma estrutura
        t.lexer.push_state('RARRAY')
        return t

    def t_RVALUE_closepr(self, t):
        r'\]'
        t.type = ']'
        t.lexer.pop_state()
        return t

    def t_RVALUE_openchv(self, t):
        r'\{'
        t.type = '{'
        t.lexer.pop_state() # não vamos ler um valor, mas sim uma estrutura
        t.lexer.push_state('RDICT')
        return t

    def t_RVALUE_closechv(self, t):
        r'\}'
        t.type = '}'
        t.lexer.pop_state()
        return t

    def t_RVALUE_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t


    # RARRAY
    def t_RARRAY_OFFSETDATETIME(self, t):
        r'\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}\:\d{2}\:\d+\.\d+[\-\+]\d{2}\:\d{2}|\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}\:\d{2}\:\d{2}[\-\+]\d{2}\:\d{2}|\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}\:\d{2}\:\d{2}(\.\d+)?[Zz]'
        t.value = str(parseDateTime(t.value))
        t.type = 'DATETIME'
        return t

    def t_RARRAY_LOCALDATETIME(self, t):
        r'\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}\:\d{2}\:\d{2}(\.\d+)?'
        t.value = str(parseDateTime(t.value))
        t.type = 'DATETIME'
        return t

    def t_RARRAY_LOCALDATE(self, t):
        r'\d{4}\-\d{2}\-\d{2}'
        t.value = str(parseDateTime(t.value).date())
        t.type = 'DATETIME'
        return t

    def t_RARRAY_LOCALTIME(self, t):
        r'\d{2}\:\d{2}\:\d{2}(\.\d+)?'
        t.value = str(parseDateTime(t.value).time())
        t.type = 'DATETIME'
        return t

    def t_RARRAY_BMLSTRING(self, t):
        r'""""""|""""{0,2}(?:(?=(?P<t0>\\?))(?P=t0)(?:.|\n))*?""""{0,2}'
        t.value = treat_BML_string(t.value)
        t.type = 'STRING'
        return t

    def t_RARRAY_LMLSTRING(self, t):
        r'\'\'\'\'\'\'|\'\'\'\'{0,2}(.|\n)*?\'\'\'\'{0,2}'
        t.value = treat_LML_string(t.value)
        t.type = 'STRING'
        return t

    def t_RARRAY_STRING(self, t):
        r'\"(?:(?=(?P<t2>\\?))(?P=t2).)*?\"|\'.*?\''
        t.value = treat_single_string(t.value)
        return t

    def t_RARRAY_FLOAT(self, t):
        r'(\+|\-)?(\d(\_?\d)*(\.\d(\_?\d)*)?[eE](\+|\-)?\d(\_?\d)*|\d(\_?\d)*\.\d(\_?\d)*)'
        t.value = float(t.value)
        return t

    def t_RARRAY_INF(self, t):
        r'(\+|\-)?inf'
        if t.value[0] == "-":
            t.value = -math.inf
        else:
            t.value = math.inf
        t.type = "FLOAT"
        return t

    def t_RARRAY_NAN(self, t):
        r'(\+|\-)?nan'
        t.value = math.nan
        t.type = "FLOAT"
        return t

    def t_RARRAY_INTHEX(self, t):
        r'0x[0-9a-fA-F](\_?[0-9a-fA-F])*'
        t.value = int(t.value, 16)
        isValidInt(t)
        t.type = "INT"
        return t

    def t_RARRAY_INTOCT(self, t):
        r'0o[0-7](_?[0-7])*'
        t.value = int(t.value, 8)
        isValidInt(t)
        t.type = "INT"
        return t

    def t_RARRAY_INTBIN(self, t):
        r'0b[01](_?[01])*'
        t.value = int(t.value, 2)
        isValidInt(t)
        t.type = "INT"
        return t

    def t_RARRAY_INT(self, t):
        r'(\+|\-)?(0|[1-9](?:\_?\d)*)' # não pode começar em 0
        t.value = int(t.value)
        isValidInt(t)
        return t

    def t_RARRAY_BOOL(self, t):
        r'\b(true|false)\b'
        t.value = parse_bool(t.value)
        return t

    def t_RARRAY_comma(self, t):
        r'\,'
        t.type = ','
        return t

    def t_RARRAY_openpr(self, t):
        r'\['
        t.type = '['
        t.lexer.push_state('RARRAY')
        return t

    def t_RARRAY_closepr(self, t):
        r'\]'
        t.type = ']'
        t.lexer.pop_state()
        return t

    def t_RARRAY_openchv(self, t):
        r'\{'
        t.type = '{'
        t.lexer.push_state('RDICT')
        return t

    def t_RARRAY_closechv(self, t):
        r'\}'
        t.type = '}'
        t.lexer.pop_state()
        return t


    # RDICT
    def t_RDICT_KEY(self, t):
        r'[\w\-]+|\"(?:(?=(?P<t2>\\?))(?P=t2).)*?\"|\'.*?\''
        t.value = treat_keys(t.value)
        return t
    
    def t_RDICT_dot(self, t):
        r'\.'
        t.type = '.'
        return t
    
    def t_RDICT_equal(self, t):
        r'='
        t.type = '='
        t.lexer.push_state('RVALUE')
        return t

    def t_RDICT_comma(self, t):
        r'\,'
        t.type = ','
        return t

    def t_RDICT_openpr(self, t):
        r'\['
        t.type = '['
        t.lexer.push_state('RARRAY')
        return t

    def t_RDICT_closepr(self, t):
        r'\]'
        t.type = ']'
        t.lexer.pop_state()
        return t

    def t_RDICT_openchv(self, t):
        r'\{'
        t.type = '{'
        t.lexer.push_state('RDICT')
        return t
    
    def t_RDICT_closechv(self, t):
        r'\}'
        t.type = '}'
        t.lexer.pop_state()
        return t
    
    def t_RDICT_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t


    def t_eof(self, t):
        # Uma vez que o lexer chama t_eof, sempre que é retornado um token na sua própria função, desta maneira assegura que só passa por ela uma vez.
        if not t.lexer.end:
            t.type = 'EOF'
            t.lexer.end = True
            return t

    t_ANY_ignore = '\t '

    def t_ANY_error(self, t):
        coluna = find_column(t)
        line = getline(t)
        print(f"Erro de parsing do tokenizer: sintaxe inválida na linha {t.lineno}, coluna {coluna}.")
        print(f"{line.rstrip()}")
        print(" " * (coluna - 1) + "^")
        print("Execução interrompida!")
        exit(1)

    def t_ANY_COMMENT(self, t):
        r'\#.*'

    def t_ANY_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

# Fim da gramática

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        self.lexer.end = False

    # Para testar o lexer
    def test(self, data):
        self.lexer.end = False
        self.lexer.input(data)

        for tok in self.lexer:
            print(f'{tok}: {self.lexer.current_state()}')
        



# Codigo executado caso o tokenizer seja chamado diretamente (principalmente para DEBUG)
# python3 tokenizer.py [nome do ficheiro de input]
if __name__ == '__main__':
    m = Lexer()
    m.build()
    in_file = "examples/default.toml"
    if len(sys.argv) > 1:
        in_file = sys.argv[1]
    with open(in_file) as f:
        data = f.read()
    m.test(data)