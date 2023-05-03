import ply.yacc as yacc
# from tokenizer import tokens
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

    def p_final(self, p):
        '''
        toml : toml EOF
        '''
        p[0] = p[1]

    def p_0(self, p):
        'toml : newlines toml'
        p[0] = p[2]


    def p_2(self, p):
        'toml : kvaluepairs tables'
        p[0] = merge_dictionaries([p[1], p[2]])

    def p_233(self, p):
        '''
        toml : kvaluepairs
             | tables
        '''
        p[0] = p[1]

    def p_empty_file(self, p):
        '''
        toml : 
        '''
        p[0] = {}

    def p_3(self, p):
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

    def p_45(self, p): 
        '''kvaluepairs : kvaluepair newlines
                       | kvaluepair EOF
        '''
        p[0] = p[1]

    def p_5(self, p):
        'kvaluepair : key EQUAL value'
        p[0] = calcObject(p[1],p[3])
        p.set_lineno(0, p.lineno(1))
        p.set_lexpos(0, p.lexpos(1))

    def p_6(self, p):
        'key : KEY DOT key'
        p[0] = [p[1]] + p[3]
        p.set_lineno(0, p.lineno(1))
        p.set_lexpos(0, p.lexpos(1))

    def p_7(self, p):
        'key : KEY'
        p[0] = [p[1]]
        p.set_lineno(0, p.lineno(1))
        p.set_lexpos(0, p.lexpos(1))

    def p_8(self, p):
        'tables : tables normaltable'
        # p[0] = merge_dictionaries([p[1],p[2]])
        try:
            p[0] = merge_tables([p[1],p[2]])
        except myException as exc:
            exc.set_linetable(p.lineno(2))
            raise exc

    def p_9(self, p):
        'tables : tables arraytable'
        # p[0] = merge_dictionaries([p[1],p[2]])
        try:
            p[0] = merge_tables([p[1],p[2]])
        except myException as exc:
            exc.set_linetable(p.lineno(2))
            raise exc

    def p_10(self, p):
        '''
        tables : arraytable
               | normaltable
        '''
        p[0] = p[1]


    def p_11(self, p):
        'normaltable : OPENPR tablename CLOSEPR newlines kvaluepairs'
        p[0] = calcObject(p[2],p[5])
        p.set_lineno(0, p.lineno(2))

    ### Acrescentei isto por causa dos casos em que só aparece o tablename sem newline, no fim do ficheiro (old_comment)
    def p_111(self, p):
        '''normaltable : OPENPR tablename CLOSEPR newlines
                       | OPENPR tablename CLOSEPR EOF
        '''
        p[0] = calcObject(p[2],{})
        p.set_lineno(0, p.lineno(2))

    def p_12(self, p):
        'arraytable : OPENPR OPENPR tablename CLOSEPR CLOSEPR newlines kvaluepairs'
        p[0] = calcObjectArrayTable(p[3],p[7])
        p.set_lineno(0, p.lineno(3))

    ### Acrescentei isto por causa dos casos em que só aparece o tablename sem newline, no fim do ficheiro (old_comment)
    def p_122(self, p):
        '''
        arraytable : OPENPR OPENPR tablename CLOSEPR CLOSEPR newlines
                   | OPENPR OPENPR tablename CLOSEPR CLOSEPR EOF
        '''
        p[0] = calcObjectArrayTable(p[3],{})
        p.set_lineno(0, p.lineno(3))

    def p_13(self, p):
        'tablename : TABLE DOT tablename'
        p[0] = [p[1]] + p[3]
        p.set_lineno(0, p.lineno(1))

    def p_14(self, p):
        'tablename : TABLE'
        p[0] = [p[1]]
        p.set_lineno(0, p.lineno(1))

    def p_15(self, p):
        'value : INT'
        p[0] = p[1]

    def p_16(self, p):
        'value : FLOAT'
        p[0] = p[1]

    def p_17(self, p):
        'value : STRING'
        p[0] = p[1]

    def p_18(self, p):
        'value : BOOL'
        p[0] = p[1]

    def p_19(self, p):
        'value : OFFSETDATETIME'
        p[0] = p[1]

    def p_20(self, p):
        'value : LOCALDATETIME'
        p[0] = p[1]

    def p_21(self, p):
        'value : LOCALDATE'
        p[0] = p[1]

    def p_22(self, p):
        'value : LOCALTIME'
        p[0] = p[1]

    def p_23(self, p):
        'value : array'
        p[0] = p[1]

    def p_24(self, p):
        'value : dictionary'
        p[0] = p[1]

    def p_25(self, p):
        'array : OPENPR CLOSEPR'
        p[0] = []

    def p_26(self, p):
        'array : OPENPR arraycontent CLOSEPR'
        p[0] = p[2]

    def p_27(self, p):
        '''
        arraycontent : arraycontent arrelem
        '''
        p[0] = p[1] + [p[2]]

    def p_277(self, p):
        "arraycontent : arrelem"
        p[0] = [p[1]]

    #! Talvez até se possa reutilizar o simbolo "value" (para "arrelem"), mas n quis estar a fazer essa confusao.
    def p_28(self, p):
        '''
        arrelem : value COMMA
                | value
        '''
        p[0] = p[1]

    def p_29(self, p):
        'dictionary : OPENCHV CLOSECHV'
        p[0] = dict()

    def p_30(self, p):
        'dictionary : OPENCHV dictcontent CLOSECHV'
        p[0] = p[2]

    def p_31(self, p):
        'dictcontent : dictcontent COMMA kvaluepair'
        try:
            p[0] = merge_dictionaries([p[1], p[3]])
        except myException as e:
            e.set_lineno(p.lineno(3))
            e.set_lexpos(p.lexpos(3))
            raise e

    def p_32(self, p):
        'dictcontent : kvaluepair'
        p[0] = p[1]
        p.set_lineno(0, p.lineno(1))
        p.set_lexpos(0, p.lexpos(1))

    # Utiliza-se esta regra porque uma vez que no tokenizer os "comments" são ignorados, os NEWLINE nem sempre se encontram agrupados.
    def p_newlines(self, p):
        '''
        newlines : NEWLINE newlines
                 | NEWLINE
        '''

    def p_error(self, p):
        raise parsingError(token = p)


    def build(self, **kwargs):
        self.lexer = Lexer()
        self.lexer.build()
        self.parser = yacc.yacc(module=self, **kwargs)

    def input_data(self, data):
        result = self.parser.parse(data)
        return result

    # parser = yacc.yacc(debug=True)