import ply.yacc as yacc
import sys
import json

from tokenizer2 import tokens

# Gramática







### inicio do parsing
parser = yacc.yacc(debug=True)
parser.success = True
    
#? Input hardcoded do ficheiro de input.
filename = "examples/data1.toml"
with open(filename) as f:
    parser.parse(f.read())




#? Input na linha de comandos do ficheiro de input.
# if len(sys.argv) > 1:
#     filename = sys.argv[1]
# else:
#     print("Não foi especificado um ficheiro de input.")
#     exit()
# with open(filename) as f:
#     parser.parse(f.read())



# with open("res.json", "w") as wf:
#     json.dump(parser.json, wf, indent=4, ensure_ascii=False)