#task 1 закипание кастрюли
'''
temp = 7 #temp on celsius
time = 0 #time om sec
dtime = 2
dtemp = 1
while temp < 100:
    temp += dtemp
    time += dtime
print(time)
 '''

#task 2 закипание кастрюли V 2.0
'''
temp = 7 #temp on celsius
time = 0 #time om sec
dtime = 2
dtemp = 1
while temp < 100:
    temp += dtemp
    time += dtime
minute = time // 60
sec = time % 60
print(f'время на закипание надо: {minute} минут и {sec} секунд')
 '''

#task 3 таблица умножения
'''
n = int(input('введите число, к которому надо вывести таблицу умножения: '))
l = int(input('от какого числа начнём умножение: '))
k = int(input('каким числом закончим умножение: '))
while l <= k:
    print(f'{n} * {l} = ' + str(n * l))
    l += 1
'''

#task 4

#task 5 магазин
'''
bread = 100
milk = 120
cucumber = 60
orange = 450
score = 0
print('В магазине имеются такие продукты как:')
print(f'хлеб с ценой: {bread} рублей')
print(f'молоко с ценой: {milk} рублей')
print(f'огурцы с ценой: {cucumber} рублей')
print(f'апельсины с ценой: {orange} рублей')
print('для выхода введите \'EXIT\'')
print('что будете покупать? Пожалуйста введите:')
buy = input()
while True:
    if buy == 'EXIT':
        break
    elif buy == 'хлеб':
        score += bread
    elif buy == 'молоко':
        score += milk
    elif buy == 'огурцы':
        score += cucumber
    elif buy == 'апельсины':
        score += orange
    print(f'Ваш чек составляет: {score} рублей')
    buy = input()
print('Ваш заказ будет стоить:', score)
'''

#task 6 банковская задача с процентами
'''
m = int(input('Cколько вы положили в банк (в тыс): '))
k = int(input('Под какой процент вы положили деньги в банк: '))
s = int(input('Какую сумму денег вы хотите получить: '))
i = 0 #счётчик прошедших лет
while m <= s:
    m = m *(1 + k / 100) 
    i += 1
print(f'вам необходимо подождать всего лишь {i} лет (годов)')
'''

#task 7 подсчёт подстрок в строке
'''
s = input() + ' '
d = ''
j = 1
i = 1
while i < len(s):
    if s[i] == s[i-1]:
        j +=1
    else:
        d = d + str(s[i-1]) + str(j)  
        j = 1
    i += 1
print(d)
'''

#task 8 удаление текста внутри скобок
'''
#увы, программа по памяти весьма не эфективна
s = input()
i = 0
d = '' #создали пустую строку, что бы в неё записывать видоизменённую строку s
j = 0
while i < len(s):
    if s[i] == '(': #находим ту часть строки, откуда будем всё "вырезать"
        d = d + '(' #показываем в новой строке что тут есть открывающая скобка
        j = i
        while s[j] != ')': #идём по строке пока не находим закрывающую скобку
            j += 1
        i = j  #запомнили индекс закрывающей скобки, то есть дальше идёт та часть строки которая нужна, которую надо вывести на экран
    d = d + s[i] #записываем новую строку
    i += 1
print(d)
'''

#task 9 пароль
'''
print('Придумайте пароль из латинских букв(Заглавных и прописных), чисел и знаков: !"#%&\'()*+,-.')
print('Пароль должен быть длинее 8 символов')
password = input()
i = 0
m = False
M = False
s = False
d = False
if len(password) <= 8:
    print('Пароль короткий. Придумайте другой')
else:
    while i < len(password):
        if 122 >= ord(password[i]) >= 97:
            m = True
        elif 90 >= ord(password[i]) >= 65:
            M = True
        elif  46 >= ord(password[i]) >= 33:
            s = True
        elif 57 >= ord(password[i]) >= 48:
            d = True
        i += 1

    if not(m): print('Пороль не содержит прописные буквы')
    elif not(M): print('Пороль не содержит заглавные буквы')
    elif not(s): print('Пороль не содержит знаки: !"#%&\'()*+,-.')
    elif not(d): print('Пороль не содержит числа')
    else:
        print('Пароль надёжный')
'''

#task 10
'''
k = int(input('введите число, высоту пирамидки: '))
i = 0
while i <= k:
    print('*' * i)
    i += 1
i = k - 1
while i >= 0:
    print('*' * i)
    i -= 1
'''
