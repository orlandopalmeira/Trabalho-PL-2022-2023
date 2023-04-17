import ply.yacc as yacc
from tokenizer import tokens
import json
import sys

#! Evita o warning "WARNING: Token 'COMMENT' defined, but not used" 
tokens.remove('COMMENT')

'''
GRAMATICA:

file : toml

toml : kvaluepairs tables

# Pares chave-valor
kvaluepairs : kvaluepair kvaluepairs
            |

kvaluepair : key EQUAL value

key : KEY DOT key
    | KEY

# tabelas/objectos
tables : normaltable tables
       | arraytable tables
       | 

normaltable : OPENPR tablename CLOSEPR kvaluepairs

arraytable : OPENPR OPENPR tablename CLOSEPR CLOSEPR kvaluepairs

tablename : TABLE DOT tablename
          | TABLE

# valores concretos
value : INT
      | FLOAT
      | STRING
      | BOOL
      | OFFSETDATETIME
      | LOCALDATETIME
      | LOCALDATE
      | LOCALTIME
      | array
      | dictionary

# arrays e dicionarios
array : OPENPR CLOSEPR
      | OPENPR arraycontent CLOSEPR

arraycontent : value COMMA arraycontent
             | value

dictionary : OPENCHV CLOSECHV
           | OPENCHV dictcontent CLOSECHV

dictcontent : kvaluepair COMMA dictcontent
            | kvaluepair
'''
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
                result[key] = merge_dictionaries([result[key], value])
            elif isinstance(value, list) and key in result:
                result[key] += value
            else:
                result[key] = value
    return result

##! Talvez meter esta função num sitio mais apropriado
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

def p_0(p):
    'file : NEWLINE toml'
    p.parser.result = p[2]

def p_1(p):
    'file : toml'
    # with open(out_file,'w') as wf:
    #     json.dump(p[1], wf, indent=2, ensure_ascii=False)
    # print(f"\nResultado escrito no ficheiro {out_file}.")
    p.parser.result = p[1]

def p_2(p):
    'toml : kvaluepairs tables'
    # p[0] = p[1]
    # p[0].update(p[2])
    p[0] = merge_dictionaries([p[1], p[2]])

def p_3(p):
    'kvaluepairs : kvaluepair NEWLINE kvaluepairs'
    p[0] = merge_dictionaries([p[1], p[3]])

def p_4(p):
    'kvaluepairs : '
    p[0] = dict()

def p_34(p):
    'kvaluepairs : kvaluepair'
    p[0] = dict()

def p_5(p):
    'kvaluepair : key EQUAL value'
    p[0] = calcObject(p[1],p[3])

def p_6(p):
    'key : KEY DOT key'
    p[0] = [p[1]] + p[3]

def p_7(p):
    'key : KEY'
    p[0] = [p[1]]

def p_8(p):
    'tables : normaltable tables'
    # p[0] = p[1]
    # p[0].update(p[2])
    p[0] = merge_dictionaries([p[1],p[2]])

def p_9(p):
    'tables : arraytable tables'
    # (tableName,tableContent) = p[1].popitem()
    # if tableName in p[2]:
    #     p[2][tableName].append(tableContent)
    # else:
    #     p[2][tableName] = [tableContent]
    # p[0] = p[2]
    p[0] = merge_dictionaries([p[1],p[2]])

def p_10(p):
    'tables : '
    p[0] = dict()

def p_11(p):
    'normaltable : OPENPR tablename CLOSEPR NEWLINE kvaluepairs'
    p[0] = calcObject(p[2],p[5])
    pass

def p_12(p):
    'arraytable : OPENPR OPENPR tablename CLOSEPR CLOSEPR NEWLINE kvaluepairs'
    p[0] = calcObjectArrayTable(p[3],p[7])

def p_13(p):
    'tablename : TABLE DOT tablename'
    p[0] = [p[1]] + p[3]

def p_14(p):
    'tablename : TABLE'
    p[0] = [p[1]]

def p_15(p):
    'value : INT'
    p[0] = p[1]

def p_16(p):
    'value : FLOAT'
    p[0] = p[1]

def p_17(p):
    'value : STRING'
    p[0] = p[1]
    # print(p[0])

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
    p[0] = dict(merge_dictionaries(p[2]))

def p_31(p):
    'dictcontent : kvaluepair COMMA dictcontent'
    p[0] = [p[1]] + p[3]

def p_32(p):
    'dictcontent : kvaluepair'
    p[0] = [p[1]]

def p_error(p):
    parser.success = False
    if p:
        coluna = find_column(p)
        line = getline(p)
        print(f"Erro de parsing: sintaxe inválida na linha {p.lineno}, coluna {coluna}.")
        print(f"Encontrado token '{p.value}' inesperado.")
        print(f"{line.rstrip()}")
        print(" " * (coluna - 1) + "^")

    else:
        #! Tenho de ver melhor em que situaçoes ocorre isto.
        print("Erro de sintaxe no EOF.")

    print("Execução interrompida!")
    exit(1)

parser = yacc.yacc(debug=True)
parser.success = True
