import sys
import json
from grammar import parser
from myExceptions import *

### Main
# python3 program.py (<ficheiro_input>) (<ficheiro_output>)
# in_file = "/home/pedro/PL/Trabalho-PL-2022-2023/src/examples/strings.toml"
in_file = "/home/pedro/PL/Trabalho-PL-2022-2023/src/examples/zcurrent.toml"
out_file = "/home/pedro/PL/Trabalho-PL-2022-2023/src/result.json"
if len(sys.argv) > 2:
    out_file = sys.argv[2] 
if len(sys.argv) > 1:
    in_file = sys.argv[1]

print(f"Ficheiro de input: {in_file}")
print(f"Ficheiro de output: {out_file}")
print("\nA analisar..")

with open(in_file) as rf:
    text = rf.read()

try:
    parser.parse(text)
except myException as e:

    e.input_text(text)

    e.printMessage()

    # print("Execução interrompida!")##
else:
    with open(out_file, 'w') as wf:
        json.dump(parser.result, wf, indent=2, ensure_ascii=False)
        print(f"\nResultado escrito no ficheiro {out_file}.")