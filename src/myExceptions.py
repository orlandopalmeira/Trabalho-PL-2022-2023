import re
from abc import ABC, abstractmethod # apenas para definir uma classe abstrata

def find_column(text, lexpos):
    '''
    Retorna o número da coluna em que o token se encontra na linha.
    '''
    line_start = text.rfind('\n', 0, lexpos) + 1
    return (lexpos - line_start)

# Exceção Pai para definir a nossa hierarquia de exceçoes
class myException(ABC, Exception):

    def __init__(self, message = "Erro de parsing.", lineno = None, lexpos = None):
        self.message = message
        self.lineno = lineno
        self.lexpos = lexpos
        super().__init__(self.message)

    def set_lineno(self, lineno):
        self.lineno = lineno
    
    def set_lexpos(self, lexpos):
        self.lexpos = lexpos

    def input_text(self, text):
        # Chama a respetiva função de criação de mensagem de erro.
        self.create_message(text)

    @abstractmethod
    def create_message(self, file_text):
        pass

    def printMessage(self):
        print(self.message)


class dupKey(myException):

    def __init__(self, message="Erro de parsing.", dup_key = None, lineno = None, lexpos = None):
        self.dup_key = dup_key
        super().__init__(message, lineno=lineno, lexpos=lexpos)

    def create_message(self, file_text):
        lineno = self.lineno
        dup_key = self.dup_key
        if dup_key and lineno and self.lexpos:
            arr_of_lines = file_text.split('\n')
            line = arr_of_lines[lineno - 1]
            coluna = find_column(file_text, self.lexpos)
            self.message = f"""
Erro de parsing: sintaxe inválida na linha {lineno}, coluna {coluna+1}.
Encontrada chave \"{dup_key}\" duplicada.
  {line.rstrip()}
  {" " * (coluna)}^\
"""


class InvalidAtrib(myException):

    def __init__(self, message="Erro de atribuição de valor.", wrong_key = None, lineno = None, lexpos = None):
        self.wrong_key = wrong_key
        super().__init__(message, lineno=lineno, lexpos=lexpos)

    def create_message(self, file_text):
        lineno = self.lineno
        wrong_key = self.wrong_key
        if wrong_key and lineno and self.lexpos:
            arr_of_lines = file_text.split('\n')
            line = arr_of_lines[lineno - 1]
            coluna = find_column(file_text, self.lexpos)
            self.message = f"""
Erro de parsing: sintaxe inválida na linha {lineno}, coluna {coluna+1}.
Encontrada chave \"{wrong_key}\" duplicada.
  {line.rstrip()}
  {" " * (coluna)}^\
"""

class parsingError(myException):

    def __init__(self, message="Erro de parsing.", token = None):
        self.value = None
        self.isEOF = True
        lineno = None
        lexpos = None
        if token:
            self.isEOF = False
            self.value = token.value
            lineno = token.lineno
            lexpos = token.lexpos
        super().__init__(message, lineno=lineno, lexpos=lexpos)

    def create_message(self, file_text):
        arr_of_lines = file_text.split('\n')
        if not self.isEOF:
            value = self.value
            lineno = self.lineno
            line = arr_of_lines[lineno - 1]
            coluna = find_column(file_text, self.lexpos)
            self.message = f"""
Erro de parsing: sintaxe inválida na linha {lineno}, coluna {coluna+1}.
Encontrado token '{value}' inesperado.
  {line.rstrip()}
  {" " * (coluna)}^\
"""
        else: # Caso de EOF
            lineno = len(arr_of_lines)
            line = arr_of_lines[-1]
            coluna = len(line)
            self.message = f"""
Erro de parsing: sintaxe inválida na linha {lineno}, coluna {coluna}.
Fim de ficheiro inesperado.
  {line.rstrip()}
  {" " * (coluna - 1)}^\
"""