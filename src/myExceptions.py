from abc import ABC, abstractmethod # apenas para definir uma classe abstrata

def _find_column(text, lexpos):
    '''
    Retorna o número da coluna em que o token se encontra na linha.
    '''
    line_start = text.rfind('\n', 0, lexpos) + 1
    return (lexpos - line_start)

# Exceção Pai para definir a nossa hierarquia de exceçoes
class myException(ABC, Exception):

    def __init__(self, message = "Erro de parsing.", lineno = None, lexpos = None, linetable = None):
        self.message = message
        self.lineno = lineno
        self.lexpos = lexpos
        self.linetable = linetable
        super().__init__(self.message)

    def set_lineno(self, lineno):
        self.lineno = lineno
    
    def set_lexpos(self, lexpos):
        self.lexpos = lexpos
    
    def set_linetable(self, linetable):
        self.linetable = linetable

    def input_text(self, text):
        # Chama a respetiva função de criação de mensagem de erro.
        self.create_message(text)

    @abstractmethod
    def create_message(self, file_text):
        pass

    def printMessage(self):
        print(self.message)


class dupKey(myException):

    def __init__(self, message="Erro de parsing.", dup_key = None, lineno = None, lexpos = None, linetable = None):
        self.dup_key = dup_key
        super().__init__(message, lineno=lineno, lexpos=lexpos, linetable=linetable)

    def create_message(self, file_text):
        lineno = self.lineno
        linetable = self.linetable
        dup_key = self.dup_key
        if dup_key and linetable:
            self.message = f"""\
Erro de parsing: sintaxe inválida na tabela da linha {linetable}.
Encontrada chave \"{dup_key}\" duplicada."""
        elif dup_key and lineno and self.lexpos:
            arr_of_lines = file_text.split('\n')
            line = arr_of_lines[lineno - 1]
            coluna = _find_column(file_text, self.lexpos)
            self.message = f"""\
Erro de parsing: sintaxe inválida na linha {lineno}, coluna {coluna+1}.
Encontrada chave \"{dup_key}\" duplicada.
  {line.rstrip()}
  {" " * (coluna)}^\
"""


class InvalidAtrib(myException):

    def __init__(self, message="Erro de atribuição de valor.", wrong_key = None, expected_type=None, actual_type=None, value=None, lineno = None, lexpos = None, linetable = None):
        """Argumento "value" serve para ser possível calcular o tipo de dados que foi recebido."""
        self.wrong_key = wrong_key
        self.expected_type = expected_type
        self.actual_type = actual_type
        if expected_type and not isinstance(expected_type, str):
            self.expected_type = type(expected_type).__name__
        if actual_type and not isinstance(actual_type, str):
            self.actual_type = type(actual_type).__name__
        if not self.actual_type and value:
            self.actual_type = type(value).__name__
        super().__init__(message, lineno=lineno, lexpos=lexpos, linetable=linetable)

    def create_message(self, file_text):
        linetable = self.linetable
        lineno = self.lineno
        lexpos = self.lexpos
        wrong_key = self.wrong_key
        actual_type = self.actual_type
        expected_type = self.expected_type
        if wrong_key:
            self.message = f"Erro de redefinição da chave \"{wrong_key}\""
            # Definição do texto indicativo da linha do erro.
            if linetable:
                self.message += f", na tabela da linha {linetable}.\n"
            elif lineno and lexpos:
                arr_of_lines = file_text.split('\n')
                line = arr_of_lines[lineno - 1].rstrip()
                coluna = _find_column(file_text, self.lexpos)
                self.message += f", na linha {lineno}, na coluna {coluna+1}."
                if line:
                    self.message += f"""
  {line}
  {" " * (coluna)}^\
  """                 
            else:
                self.message += ".\n"
            self.message += f"O valor deveria ser do tipo '{expected_type}'.\n" if expected_type else ""
            self.message += f"O valor recebido foi do tipo '{actual_type}'.\n" if actual_type else ""


class parsingError(myException):

    def __init__(self, message="Erro de parsing.", token = None):
        self.value = None
        lineno = None
        lexpos = None
        if token:
            self.value = "'" + str(token.value) + "'" if token.value != "\n" else r"'\n' (newline)" # Esta condição serve para o caso do token ser um newLine para que não seja printado uma nova linha na mensagem de erro.
            lineno = token.lineno
            lexpos = token.lexpos
        super().__init__(message, lineno=lineno, lexpos=lexpos)

    def create_message(self, file_text):
        arr_of_lines = file_text.split('\n')
        if self.value:
            value = self.value
            lineno = self.lineno
            line = arr_of_lines[lineno - 1].rstrip()
            coluna = _find_column(file_text, self.lexpos)
            self.message = f"""\
Erro de parsing: sintaxe inválida na linha {lineno}, coluna {coluna+1}.
Encontrado token {value} inesperado.
  {line}
  {" " * (coluna)}^"""
        else: # Caso de EOF inesperado
            lineno = len(arr_of_lines)
            line = arr_of_lines[-1].rstrip()
            coluna = len(line)
            self.message = f"""\
Erro de parsing: sintaxe inválida na linha {lineno}, coluna {coluna+1}.
Fim de ficheiro inesperado."""
            if line:
                self.message += f"""
  {line}
  {" " * (coluna)}^\
"""