import re

def getLineColFromPos(text, pos):
    arr_of_lines = text.split('\n')
    current_pos = 0
    ant_pos = 0
    for i, l in enumerate(arr_of_lines, start=1):
        ant_pos = current_pos
        current_pos += len(l) + 1 # (+1) por causa dos \n
        if current_pos > pos:
            col = pos - ant_pos
            return i, col


class myException(Exception):

    def __init__(self, message="Erro de parsing.", flag = None, dupkey = None):
        self.message = message
        self.flag = flag
        self.dupkey = dupkey
        super().__init__(self.message)
    

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
        self.message = f"""
Erro de parsing: sintaxe inválida na linha {lineno}, coluna {coluna}.
Fim de ficheiro inesperado.
{line.rstrip()}
{" " * (coluna - 1)}^\
"""

    def set_search_init(self, linenumber):
        if not self.dupkey:
            # print("INESPERADO!!!!")##
            return
        self.dupkey["linebegin"] = linenumber

    def create_dupkey_message(self, file_text):
        """
        filename -> Conteúdo do ficheiro que foi inputed.
        """
        arr_of_lines = file_text.split('\n')
        ls = self.dupkey["linebegin"] - 1
        dup_key = self.dupkey["key"]
        area_of_text = "\n".join(arr_of_lines[ls:])
        regex = r'([\"\']{0,3})'+ dup_key + r'\1\s*\='
        dup_key_matches = re.finditer(regex, area_of_text)
        for i, m in enumerate(dup_key_matches):
            if i == 1:
                dup_key_match = m
        lineno, coluna = getLineColFromPos(area_of_text, dup_key_match.start())
        lineno += ls
        line = arr_of_lines[lineno-1]
        self.message = f"""
Erro de parsing: sintaxe inválida na linha {lineno}.
Encontrada chave \"{dup_key}\" duplicada.
{line.rstrip()}
{" " * (coluna)}^\
"""

    def treat_exc(self, file_text):
        if self.flag == "EOF":
            self.create_EOF_message(file_text)
        elif self.dupkey:
            self.create_dupkey_message(file_text)