import subprocess
from os import system
import json

light = lambda x: '\033[1m\033[91m' + x + '\033[0m'

correctos = [
    ('demos/demos/1_basic/basic.toml', 'demos/demos/1_basic/basic.json'),
    ('demos/demos/2_strings/1strings.toml', 'demos/demos/2_strings/1strings.json'),
    ('demos/demos/2_strings/2strings_lit.toml', 'demos/demos/2_strings/2strings_lit.json'),
    ('demos/demos/2_strings/3empty.toml', 'demos/demos/2_strings/3empty.json'),
    ('demos/demos/3_int/int.toml', 'demos/demos/3_int/int.json'),
    ('demos/demos/4_float/float.toml', 'demos/demos/4_float/float.json'),
    ('demos/demos/5_dates/milliseconds.toml', 'demos/demos/5_dates/milliseconds.json'),
    ('demos/demos/6_arrays/1array.toml', 'demos/demos/6_arrays/1array.json'),
    ('demos/demos/6_arrays/array_complex.toml', 'demos/demos/6_arrays/array_complex.json'),
    ('demos/demos/7_tables/1standard.toml', 'demos/demos/7_tables/1standard.json'),
    ('demos/demos/7_tables/2dotted.toml', 'demos/demos/7_tables/2dotted.json'),
    ('demos/demos/7_tables/dotted_keys.toml', 'demos/demos/7_tables/dotted_keys.json'),
    ('demos/demos/7_tables/empty_tables.toml', 'demos/demos/7_tables/empty_tables.json'),
    ('demos/demos/8_inlinetables/1inl_tables.toml', 'demos/demos/8_inlinetables/1inl_tables.json'),
    ('demos/demos/8_inlinetables/inl_tables_with_arr.toml', 'demos/demos/8_inlinetables/inl_tables_with_arr.json'),
    ('demos/demos/9_array_tables/1simple.toml', 'demos/demos/9_array_tables/1simple.json'),
    ('demos/demos/9_array_tables/2standard.toml', 'demos/demos/9_array_tables/2standard.json'),
    ('demos/demos/9_array_tables/3array-nest.toml', 'demos/demos/9_array_tables/3array-nest.json'),
    ('demos/demos/10_extra/dotted.toml', 'demos/demos/10_extra/dotted.json'),
    ('demos/demos/10_extra/key-dotted.toml', 'demos/demos/10_extra/key-dotted.json'),
    ('demos/demos/10_extra/tricky.toml', 'demos/demos/10_extra/tricky.json'),
]

errados = [
    'demos/error_msg/dupInDictInline.toml',
    'demos/error_msg/duplicateKey.toml',
    'demos/error_msg/eof.toml',
    'demos/error_msg/intToTable.toml',
    'demos/error_msg/strnoAtr.toml',
]


print(light('------------ Testes correctos ------------'))
for teste, esperado in correctos:
    subprocess.run(f'python3 ./src/program.py {teste}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    with open(teste) as teste_f:
        print(f'{light(f"TOML: {teste}")}\n{teste_f.read()}') 
    with open('result.json') as res_f: 
        result_json = json.load(res_f)
        print(f'{light("Resultado obtido em JSON: result.json")}\n{json.dumps(result_json, indent=2)}')
    with open(esperado) as esperado_f:
        result_json = json.load(esperado_f)
        print(f'{light(f"Resultado esperado em JSON: {esperado}")}\n{json.dumps(result_json, indent=2)}')
    input('Enter para continuar...')
    print('\n'*100)
    
print(light('------------ Mensagens de erro ------------'))

for errado in errados:
    system(f'python3 ./src/program.py {errado}')
    input('Enter para continuar...')
    print('\n'*100)
