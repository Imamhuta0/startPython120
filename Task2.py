# #Create
# a = 'привет' #Одинарные кавычки
# b = "привет" #Двойные кавычки
# c = "я 'знаю' Python" #Комбинированные кавычки
# d = 'Я "знаю" Python' #можно и так
# e = 'я "знаю 'Python" #так нельзя
#
# a = 123 #целочисленный тип
# a = sta(a) #результат 'a'
# str([1, 1.1, 'a']) #результат, "[1, 1.1, 'a']"
# str(True) #Результат, 'True'
# str(None) #Результат, 'None'
#
# a = 'привет'
# b = 'Иван'
# c = f"{a} я {b}" # "привет я Илья"
#
# #Retrive
# str #строка
# list #список
# tuple #кортеж
# set, frozenset #множество
# dict #ловарь
# bytes #байты
# bytearray #последовательность байтов
#
# a = 'привет'
# print(a)
# print('иван')
#
# a = 'привет'
#  a [0] #п
# a[1]  #р
# a[2]  #и
# a[3]  #в
# a[4]  #е
# a[5]  #т
# a[6]  #ошибка, выход за границы
#

print(f'задача №1')
length = 90
width = 50
perimeter = (length+width)*2
print(perimeter)

print(f'задача №2')
money = 10000
add = 5000
result = money+add
print(result)

print('задача №3')
days = 5000 // 24
print(days)
hours = 5000 % 24
print(hours)

print(f'задача №4')
volume = 1.44
pages = 100
lines = 50
characters = 25
bytes = 4
volume1 = (bytes*characters*lines*pages)
volume11 = volume1/1024/1024
colwo = volume//volume11
print(colwo)

print(f'задача №5')
pi = 3.1415
areasquare = 5**2
perimetersquare = 4*5
circumference = 2*pi*5
print(areasquare)
print(perimetersquare)
print(f"{circumference:.2f}")

print(f'задача №6')
str_numbers = 20 * '0' + 50 * '1' + 30 * '2'
print(str_numbers)

print('задача после задач')
word = "телефон"
reversed_word = word [::-1]
print("телефон", word, "задом наперед:", reversed_word)