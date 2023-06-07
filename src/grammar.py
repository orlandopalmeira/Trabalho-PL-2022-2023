import ply.yacc as yacc
from tokenizer import Lexer
from myExceptions import *


def calcObject(chaves, valor):
    dicionario = {chaves[-1]: valor}
    for chave in reversed(chaves[:-1]):
        dicionario = {chave: dicionario}
    return dicionario

def calcObjectArrayTable(chaves, valor):
    dicionario = {chaves[-1]: [valor]}
    for chave in reversed(chaves[:-1]):
        dicionario = {chave: dicionario}
    return dicionario

def merge_dictionaries(dictionaries_list):
    result = {}
    for dictionary in dictionaries_list:
        for key, value in dictionary.items():
            if isinstance(value, dict) and key in result:
                try:
                    result[key] = merge_dictionaries([result[key], value])
                except AttributeError:
                    raise InvalidAtrib(f"Erro de atribuição de valor na chave \"{key}\".", wrong_key = key)
            elif isinstance(value, list) and key in result:
                result[key] += value
            elif key in result: # verificação de duplicateKeys simples
                raise dupKey(f"Erro: Chave \"{key}\" duplicada!", dup_key = key)
            else:
                result[key] = value
    return result
    
def isFinal(objeto):
    '''
    Verifica se um objeto é {key: value} ou {key: [value]} em que value não é um dicionário.
    '''
    if isinstance(objeto, dict):
        for _,value in objeto.items():
            if isinstance(value, dict) or isinstance(value, list):
                return False
    return True

def merge_tables(dictionaries_list):
    result = {}
    lastisArrayList = False
    for dictionary in dictionaries_list:
        for key, value in dictionary.items():
            if isinstance(value, dict) and key in result:
                try:
                    if lastisArrayList:
                        result[key][-1] = merge_tables([result[key][-1], value])
                    else:
                        if not ((isFinal(result[key]) and isFinal(value))):
                            result[key] = merge_tables([result[key], value])
                        else:
                            raise InvalidAtrib(f"InvalidAtrib na chave \"{key}\".", wrong_key = key)
                except AttributeError:
                    raise InvalidAtrib(f"InvalidAtrib na chave \"{key}\".", wrong_key = key)
            elif isinstance(value, list) and key in result:
                if isinstance(result[key], list):
                    result[key] += value
                else:
                    raise InvalidAtrib(f"InvalidAtrib na chave \"{key}\".", wrong_key = key, expected_type="table", value = value)
            elif key in result: # verificação de duplicateKeys simples
                raise dupKey(f"Erro: Chave \"{key}\" duplicada!", dup_key = key)
            else:
                if isinstance(value, list):
                    lastisArrayList = True
                else:
                    lastisArrayList = False
                result[key] = value
    return result
    
class Parser:

    tokens = Lexer.tokens

    def p_toml_eof(self, p):
        'toml : toml EOF'
        p[0] = p[1]

    def p_newlines_toml(self, p):
        'toml : newlines toml'
        p[0] = p[2]

    def p_toml_kvps_tables(self, p):
        'toml : kvaluepairs tables'
        p[0] = merge_dictionaries([p[1], p[2]])

    def p_toml_kvps_or_tables(self, p):
        '''
        toml : kvaluepairs
             | tables
        '''
        p[0] = p[1]

    def p_empty_toml(self, p):
        'toml : '
        p[0] = {}

    # Utiliza-se esta regra porque uma vez que no tokenizer os "comments" são ignorados, os NEWLINE nem sempre se encontram agrupados.
    def p_newlines(self, p):
        '''
        newlines : NEWLINE newlines
                 | NEWLINE
        '''

    def p_kvaluepairs(self, p):
        '''
        kvaluepairs : kvaluepairs kvaluepair newlines
                    | kvaluepairs kvaluepair EOF
        '''
        try:
            p[0] = merge_dictionaries([p[1], p[2]])
        except myException as e:
            e.set_lineno(p.lineno(2))
            e.set_lexpos(p.lexpos(2))
            raise e

    def p_single_kvaluepairs(self, p): 
        '''
        kvaluepairs : kvaluepair newlines
                    | kvaluepair EOF
        '''
        p[0] = p[1]

    # O kvaluepair não é seguido de newline ou EOF uma vez que ele é utilizado nas inline tables(dicionários) e estes não têm essa restrição.
    def p_kvaluepair(self, p):
        'kvaluepair : key "=" value'
        p[0] = calcObject(p[1],p[3])
        p.set_lineno(0, p.lineno(1))
        p.set_lexpos(0, p.lexpos(1))

    def p_key(self, p):
        'key : KEY "." key'
        p[0] = [p[1]] + p[3]
        p.set_lineno(0, p.lineno(1))
        p.set_lexpos(0, p.lexpos(1))

    def p_single_key(self, p):
        'key : KEY'
        p[0] = [p[1]]
        p.set_lineno(0, p.lineno(1))
        p.set_lexpos(0, p.lexpos(1))

    def p_tables_normalt(self, p):
        'tables : tables normaltable'
        # p[0] = merge_dictionaries([p[1],p[2]])
        try:
            p[0] = merge_tables([p[1],p[2]])
        except myException as exc:
            exc.set_linetable(p.lineno(2))
            raise exc

    def p_tables_arrayt(self, p):
        'tables : tables arraytable'
        # p[0] = merge_dictionaries([p[1],p[2]])
        try:
            p[0] = merge_tables([p[1],p[2]])
        except myException as exc:
            exc.set_linetable(p.lineno(2))
            raise exc

    def p_single_tables(self, p):
        '''
        tables : arraytable
               | normaltable
        '''
        p[0] = p[1]

    def p_normaltable(self, p):
        'normaltable : "[" tablename "]" newlines kvaluepairs'
        p[0] = calcObject(p[2],p[5])
        p.set_lineno(0, p.lineno(2))

    def p_empty_normaltable(self, p):
        '''
        normaltable : "[" tablename "]" newlines
                    | "[" tablename "]" EOF
        '''
        p[0] = calcObject(p[2],{})
        p.set_lineno(0, p.lineno(2))

    def p_arraytable(self, p):
        'arraytable : "[" "[" tablename "]" "]" newlines kvaluepairs'
        p[0] = calcObjectArrayTable(p[3],p[7])
        p.set_lineno(0, p.lineno(3))

    def p_empty_arraytable(self, p):
        '''
        arraytable : "[" "[" tablename "]" "]" newlines
                   | "[" "[" tablename "]" "]" EOF
        '''
        p[0] = calcObjectArrayTable(p[3],{})
        p.set_lineno(0, p.lineno(3))

    def p_tablename(self, p):
        'tablename : TABLE "." tablename'
        p[0] = [p[1]] + p[3]
        p.set_lineno(0, p.lineno(1))

    def p_single_tablename(self, p):
        'tablename : TABLE'
        p[0] = [p[1]]
        p.set_lineno(0, p.lineno(1))

    def p_value_array(self, p):
        'value : array'
        p[0] = p[1]

    def p_value_dictionary(self, p):
        'value : dictionary'
        p[0] = p[1]

    def p_empty_array(self, p):
        'array : "[" "]"'
        p[0] = []

    def p_array(self, p):
        'array : "[" arraycontent "]"'
        p[0] = p[2]
    
    def p_arraycnt(self, p):
        'arraycontent : list'
        p[0] = p[1]

    def p_arraycnt_comma(self, p):
        'arraycontent : list ","'
        p[0] = p[1]

    def p_list(self, p):
        'list : list "," value'
        p[0] = p[1] + [p[3]]

    def p_list_single(self, p):
        'list : value'
        p[0] = [p[1]]

    def p_empty_dictionary(self, p):
        'dictionary : "{" "}"'
        p[0] = dict()

    def p_dictionary(self, p):
        'dictionary : "{" dictcontent "}"'
        p[0] = p[2]

    def p_dictcontent(self, p):
        'dictcontent : dictcontent "," kvaluepair'
        try:
            p[0] = merge_dictionaries([p[1], p[3]])
        except myException as e:
            e.set_lineno(p.lineno(3))
            e.set_lexpos(p.lexpos(3))
            raise e

    def p_single_dictcontent(self, p):
        'dictcontent : kvaluepair'
        p[0] = p[1]
        p.set_lineno(0, p.lineno(1))
        p.set_lexpos(0, p.lexpos(1))
    
    def p_value_int(self, p):
        'value : INT'
        p[0] = p[1]

    def p_value_float(self, p):
        'value : FLOAT'
        p[0] = p[1]

    def p_value_string(self, p):
        'value : STRING'
        p[0] = p[1]

    def p_value_bool(self, p):
        'value : BOOL'
        p[0] = p[1]

    def p_value_datetime(self, p):
        'value : DATETIME'
        p[0] = p[1]

    def p_error(self, p):
        raise parsingError(token = p)


    def build(self, **kwargs):
        self.lexer = Lexer()
        self.lexer.build()
        self.parser = yacc.yacc(module=self, **kwargs)

    def input_data(self, data):
        result = self.parser.parse(data)
        return result
    