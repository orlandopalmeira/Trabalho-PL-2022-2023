import sys
import json
from grammar import Parser
from myExceptions import *

# python3 program.py [nome do ficheiro de input] [nome do ficheiro output]

# Construção do parser
myparser = Parser()
myparser.build()
# myparser.build(debug=True) # Para gerar o parser.out e outras informações de debug

in_file = "examples/default.toml"
out_file = "result.json"
if len(sys.argv) > 2:
    out_file = sys.argv[2] 
if len(sys.argv) > 1:
    in_file = sys.argv[1]

# print(f"Ficheiro de input: {in_file}")
# print(f"Ficheiro de output: {out_file}")

with open(in_file) as rf:
    text = rf.read()

print("\nA analisar..\n")

try:
    result = myparser.input_data(text)
except myException as exc:
    # Alimenta a exceção com o texto do ficheiro de input para poder ser gerada uma mensagem de erro mais detalhada
    exc.input_text(text)
    # Escreve a mensagem de erro gerada
    exc.printMessage()
else:
    print(json.dumps(result, indent=2, ensure_ascii=False)) # Printa na consola direto (DEBUG)
    with open(out_file, 'w') as wf:
        json.dump(result, wf, indent=2, ensure_ascii=False)
    # print(f"\nResultado escrito no ficheiro {out_file}.")