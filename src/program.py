import sys
import json
from grammar import parser

### Main
# python3 program.py (<ficheiro_input>) (<ficheiro_output>)
in_file = "examples/invalid/float/exp-double-us.toml"
out_file = "result.json"
if len(sys.argv) > 2:
    out_file = sys.argv[2] 
if len(sys.argv) > 1:
    in_file = sys.argv[1]

print(f"Ficheiro de input: {in_file}.")
print(f"Ficheiro de output: {out_file}.")
print("\nA analisar..")

with open(in_file) as rf:
    parser.parse(rf.read())
    with open(out_file,'w') as wf:
        json.dump(parser.result,wf,indent=2,ensure_ascii=False)
        print(f"\nResultado escrito no ficheiro {out_file}.")