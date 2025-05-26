print(f'Пример 1')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x or y) and not (y == z) and not (w)
                if F == 1:
                    print(x, y, z, w, F)

print(f'Пример 2')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x or y) and not (y == z) and not (w)

                print(x, y, z, w, F)

#задания с презентации
print(f'Задание 1')
for A in 0, 1:
    for B in 0, 1:
        for C in 0, 1:
            F = not (A or B) and (C)
            if F == 1:
                print(A, B, C, F)

print(f'Задание 2')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            F = not x or not y <= z
            if F == 1:
                print(x, y, z, F)

print(f'Задание3')
count = 0
for s1 in 0, 1:
    for s2 in 0, 1:
        for s3 in 0, 1:
            F = s1 and not s2 or s3
            if F == 1:
                count += 1
                print(s1,s2, s3, F)
print(count)

print(f'Задание 4')
count = 0
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            F = not x == y or z
            if F == 1:
                count += 1
                print(x, y, z, F)
print(count)

print(f'Задание 5')
for A in 0, 1:
    for B in 0, 1:
        for C in 0, 1:
            F = A <= B or not C
            if F == 1:
                print(A, B, C, F)
print(count)

print(f'Задание 6')
for A in 0, 1:
    for B in 0, 1:
        for C in 0, 1:
            F = not(A and B) or C
            if F == 1:
                print(A, B, C, F)
print(count)

print(f'Задание 7')
count = 0
for x1 in 0, 1:
    for x2 in 0, 1:
        for x3 in 0, 1:
            F = (not x1 and not x2) or (x1 and x3)
            if F == 1:
                count += 1
                print(x1,x2, x3, F)
print(count)

print(f'Задание 8')
for A in 0, 1:
    for B in 0, 1:
        for C in 0, 1:
            F = (A and not C) == (not A and B)
            if F == 1:
                print(A, B, C, F)
print(count)