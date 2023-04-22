class myException(Exception):

    def __init__(self, message="Erro de parsing.", flag = 0):
        self.message = message
        self.flag = flag
        super().__init__(self.message)
    
    def treat_exc(self, file_text):
        if self.flag == "EOF":
            self.create_EOF_message(file_text)

    def printErrorMessage(self):
        print(self.message)

    def create_EOF_message(self, file_text):
        """
        filename -> Conteúdo do ficheiro que foi inputed.
        """
        arr_of_lines = file_text.split('\n')
        lineno = len(arr_of_lines)
        line = arr_of_lines[-1]
        coluna = len(line)
        message = f"""
Erro de parsing: sintaxe inválida na linha {lineno}, coluna {coluna}.
Fim de ficheiro inesperado.
{line.rstrip()}
{" " * (coluna - 1)}^
"""
        self.message = message