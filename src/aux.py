
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