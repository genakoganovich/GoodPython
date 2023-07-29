m = ['#', 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
list(map(lambda x: print(f'{m[0]}{m[x]}' if x in (1, 4) else f'{m[x]}', end=' '), map(int, input().split())))
