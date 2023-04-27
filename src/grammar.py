import ply.yacc as yacc
from tokenizer import tokens
from myExceptions import *

# Evita os warnings de tokens não utilizados
not_used_tokens = ['COMMENT','BMLSTRING','LMLSTRING']
for tok in not_used_tokens:
    tokens.remove(tok)

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
    lastisArrayList = False
    for dictionary in dictionaries_list:
        for key, value in dictionary.items():
            if isinstance(value, dict) and key in result:
                try:
                    if lastisArrayList:
                        result[key][-1] = merge_dictionaries([result[key][-1], value])
                    else:
                        result[key] = merge_dictionaries([result[key], value])
                except AttributeError:
                    raise InvalidAtrib(f"Erro de atribuição de valor na chave \"{key}\".", wrong_key = key)
            elif isinstance(value, list) and key in result:
                result[key] += value
            elif key in result: # verificação de duplicateKeys simples
                raise dupKey(f"Erro: Chave \"{key}\" duplicada!", dup_key = key)
            else:
                if isinstance(value, list):
                    lastisArrayList = True
                else:
                    lastisArrayList = False
                result[key] = value
    return result
    
# Unused
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
                        if not (isFinal(result[key]) and isFinal(value)):
                            result[key] = merge_tables([result[key], value])
                        else:
                            raise InvalidAtrib(f"InvalidAtrib na chave \"{key}\".", wrong_key = key)
                except AttributeError:
                    raise InvalidAtrib(f"InvalidAtrib na chave \"{key}\".", wrong_key = key, expected_type="table", value = value) #! preciso de testar melhor esta condiçao.
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
    


def p_0(p):
    'file : newlines toml'
    p.parser.result = p[2]

def p_1(p):
    'file : toml'
    p.parser.result = p[1]

def p_2(p):
    'toml : kvaluepairs tables'
    p[0] = merge_dictionaries([p[1], p[2]])

def p_233(p):
    '''
    toml : kvaluepairs
         | tables
    '''
    p[0] = p[1]

def p_empty_file(p):
    '''
    toml : 
    '''
    p[0] = {}

def p_3(p):
    '''
    kvaluepairs : kvaluepairs kvaluepair newlines
                | kvaluepairs kvaluepair
    '''
    try:
        p[0] = merge_dictionaries([p[1], p[2]])
    except myException as e:
        e.set_lineno(p.lineno(2))
        e.set_lexpos(p.lexpos(2))
        raise e


def p_45(p): 
    '''kvaluepairs : kvaluepair newlines
                   | kvaluepair
    '''
    p[0] = p[1]

def p_5(p):
    'kvaluepair : key EQUAL value'
    p[0] = calcObject(p[1],p[3])
    p.set_lineno(0, p.lineno(1))
    p.set_lexpos(0, p.lexpos(1))

def p_6(p):
    'key : KEY DOT key'
    p[0] = [p[1]] + p[3]
    p.set_lineno(0, p.lineno(1))
    p.set_lexpos(0, p.lexpos(1))

def p_7(p):
    'key : KEY'
    p[0] = [p[1]]
    p.set_lineno(0, p.lineno(1))
    p.set_lexpos(0, p.lexpos(1))

def p_8(p):
    'tables : tables normaltable'
    # p[0] = merge_dictionaries([p[1],p[2]])
    try:
        p[0] = merge_tables([p[1],p[2]])
    except myException as exc:
        exc.set_linetable(p.lineno(2))
        raise exc

def p_9(p):
    'tables : tables arraytable'
    # p[0] = merge_dictionaries([p[1],p[2]])
    try:
        p[0] = merge_tables([p[1],p[2]])
    except myException as exc:
        exc.set_linetable(p.lineno(2))
        raise exc

def p_10(p):
    '''
    tables : arraytable
           | normaltable
    '''
    p[0] = p[1]


def p_11(p):
    'normaltable : OPENPR tablename CLOSEPR newlines kvaluepairs'
    p[0] = calcObject(p[2],p[5])
    p.set_lineno(0, p.lineno(2))

### Acrescentei isto por causa dos casos em que só aparece o tablename sem newline, no fim do ficheiro (old_comment)
def p_111(p):
    '''normaltable : OPENPR tablename CLOSEPR newlines
                   | OPENPR tablename CLOSEPR '''
    p[0] = calcObject(p[2],{})
    p.set_lineno(0, p.lineno(2))

def p_12(p):
    'arraytable : OPENPR OPENPR tablename CLOSEPR CLOSEPR newlines kvaluepairs'
    p[0] = calcObjectArrayTable(p[3],p[7])
    p.set_lineno(0, p.lineno(3))

### Acrescentei isto por causa dos casos em que só aparece o tablename sem newline, no fim do ficheiro (old_comment)
def p_122(p):
    '''
    arraytable : OPENPR OPENPR tablename CLOSEPR CLOSEPR newlines
               | OPENPR OPENPR tablename CLOSEPR CLOSEPR 
    '''
    p[0] = calcObjectArrayTable(p[3],{})
    p.set_lineno(0, p.lineno(3))

def p_13(p):
    'tablename : TABLE DOT tablename'
    p[0] = [p[1]] + p[3]
    p.set_lineno(0, p.lineno(1))

def p_14(p):
    'tablename : TABLE'
    p[0] = [p[1]]
    p.set_lineno(0, p.lineno(1))

def p_15(p):
    'value : INT'
    p[0] = p[1]

def p_16(p):
    'value : FLOAT'
    p[0] = p[1]

def p_17(p):
    'value : STRING'
    p[0] = p[1]

def p_18(p):
    'value : BOOL'
    p[0] = p[1]

def p_19(p):
    'value : OFFSETDATETIME'
    p[0] = p[1]

def p_20(p):
    'value : LOCALDATETIME'
    p[0] = p[1]

def p_21(p):
    'value : LOCALDATE'
    p[0] = p[1]

def p_22(p):
    'value : LOCALTIME'
    p[0] = p[1]

def p_23(p):
    'value : array'
    p[0] = p[1]

def p_24(p):
    'value : dictionary'
    p[0] = p[1]

def p_25(p):
    'array : OPENPR CLOSEPR'
    p[0] = []

def p_26(p):
    'array : OPENPR arraycontent CLOSEPR'
    p[0] = p[2]

def p_27(p):
    'arraycontent : value COMMA arraycontent'
    p[0] = [p[1]] + p[3]

def p_28(p):
    '''
    arraycontent : value
                 | value COMMA
    '''
    p[0] = [p[1]]

def p_29(p):
    'dictionary : OPENCHV CLOSECHV'
    p[0] = dict()

def p_30(p):
    'dictionary : OPENCHV dictcontent CLOSECHV'
    # p[0] = dict(merge_dictionaries(p[2]))
    p[0] = p[2]

def p_31(p):
    'dictcontent : dictcontent COMMA kvaluepair'
    # p[0] = [p[1]] + p[3]
    try:
        p[0] = merge_dictionaries([p[1], p[3]])
    except myException as e:
        e.set_lineno(p.lineno(3))
        e.set_lexpos(p.lexpos(3))
        raise e

def p_32(p):
    'dictcontent : kvaluepair'
    p[0] = p[1]
    p.set_lineno(0, p.lineno(1))
    p.set_lexpos(0, p.lexpos(1))

def p_newlines(t):
    '''
    newlines : NEWLINE newlines
             | NEWLINE
    '''

def p_error(p):
#     if p:
#         coluna = aux.find_column(p)
#         line = aux.getline(p)
#         message = f"""
# Erro de parsing: sintaxe inválida na linha {p.lineno}, coluna {coluna}.
# Encontrado token '{p.value}' inesperado.
# {line.rstrip()}
# {" " * (coluna - 1)}^
# """
#         raise myException(message)
#         # print(f"Erro de parsing: sintaxe inválida na linha {p.lineno}, coluna {coluna}.")
#         # print(f"Encontrado token '{p.value}' inesperado.")
#         # print(f"{line.rstrip()}")
#         # print(" " * (coluna - 1) + "^")
#     else:
#         # print("Erro de sintaxe no EOF.")
#         raise myException(flag="EOF")
    raise parsingError(token = p)

parser = yacc.yacc(debug=True)
