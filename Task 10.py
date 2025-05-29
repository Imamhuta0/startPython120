from itertools import permutations

table = '457 567 45 136 123 247 126'.split()
graph = 'EF FA AB BG GE EC CB CD DF DA'.split()
print(*range(1, 8))

for p in permutations('ABCDEFG'):
    if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
        print(*p)

print(f'Задача 2')
table = '234 157 147 138 268 58 23 456' .split()
graph = 'AF FH HC CB BD DG GA GF EB EB EH' .split()
print(*range(1, 9))

for p in permutations('ABCDEFGH'):
    if all(str(p.index(b) + 1) in table [p.index(a)] for a, b in graph):
        print(*p)

print(f'Задача 3')
table = '268 134678 257 27 38 12 234 125' .split()
graph = 'АГ ГБ БД ДИ ИЖ ЖЕ ЕВ ВА ГЕ ГИ ГД' .split()
print(*range(1, 9))

for p in permutations ('АБВГДЖИЕ'):
    if all(str(p.index(b) + 1) in table [p.index(a)] for a, b in graph):
        print(*p)

print(f'Задача 4')
table = '47 345 27 1267 268 458 134 56' .split()
graph = 'АБ БГ ГД ДИ ИЖ ЖЕ ЕВ ВА ГА ГЕ ДЖ' .split()
print(*range(1, 9))

for p in permutations ('АБВГДЖИЕ'):
    if all(str(p.index(b) + 1) in table [p.index(a)] for a, b in graph):
        print(*p)