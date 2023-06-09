from pathlib import Path

directory = Path('./demos')

file_paths = list(directory.glob('**/*'))
file_paths = [str(path) for path in file_paths if path.is_file()]
file_paths.sort()

file_paths = ([path for path in file_paths if 'error_msg' not in path],
              [path for path in file_paths if 'error_msg' in path])

corrects = []
wrongs = file_paths[1]
i = 0
while i+1 < len(file_paths[0]):
    corrects.append((file_paths[0][i+1], file_paths[0][i]))
    i += 2

print('correctos = [')
for p in corrects: print(f'    {p},')
print(']')
print()
print('errados = [')
for p in wrongs: print(f'    \'{p}\',')
print(']')
