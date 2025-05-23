print('вычисление алгоритма №1')
a, s, p = 1, 150, 200
while True:
    if a >10:
        break
    a += 2
    p += a
    s += p
print(f'переменная s = {s}')

print('вычисление алгоритма №2')
c, d = 750, 90
while True:
    if d>0:
        break
    d =d-10
    c =c/2+50
print(f'переменная c = {c}')

print('вычисление алгоритма №3')
S = 1
for n in range (1,6):
    s*=n
    print(s)

print('вычисление алгоритма №4')
m, n = 12, 5
while True:
    if m == n:
        break
    elif m > n:
        m -= 2*n
    else:
        n -= 3
print(f'переменная m = {m}')

print('вычисление алгоритма №5')
k, l = [], []
for i in range (1, 11):
    k.append(10 -i)
for i in range (1, 11):
    l.append(k[5] - k[i - 1])
print(f'Массив к = {k}')
print(f'Массив l = {l}')
count_k = 0
for value in  k:
    if value < 0:
        count_k += 1
count_l = 0
for value in l:
    if value < 0:
        count_l += 1
print(f'Количество отрицательных элементов = {count_k + count_l}')
#другой вариант подсчета 
count_k = len([value for value in k if value < 0])
count_l = len([value for value in l if value < 0])
print(f'Количество отрицательных элементов = {count_k + count_l}')

