
#задача 1

a = int(input())
b = int(input())
c = int(input())
if (a * b == c):
    print('Ты правильно посчитал! Поздравляю!')
    print('Твой ответ правильный:', c)
else:
    print('Увы, вы не правильно посчитали.')


#задача 2
'''
#по хорошему предметы тоже можно запихать в переменные
#идеальнее создать массив...
a= int(input('Введите номер дня недели: '))
d2 = '2 пара (10:15-11:45)'
d3 = "3 пара (12:00-13:30)"
d4 = '4 пара (14:15-15:45)'
d5 = '5 пара (16:00-17:30)'
if a == 1:
    print('Ну понедельник...')
    print('Поэтому таки у вас нет пар в сей прекрасный день')
    print('Спасибо военной кафедре')
elif a == 2:
    print('Вторник')
    print('1-2 пары (8:30-11:45) Биология Л')
    print( d3, 'Физика Л')
    print( d4, 'Биотехнологии Л')
elif a == 3:
    print('Среда')
    print( d2, 'Прикладная механика Л')
    print( d3, 'Физ-ра')
    print( d4, 'ФКП Пр')
    print( d5, 'Линейная Алгебра Пр')
    print(' вечерние пары (17:45- 20:35) Python Пр и Л')
elif a == 4:
    print('Какой хороший день после среды...')
    print( d2, 'ФКП Л')
    print( d3, 'Физика Л')
    print( d4, 'Биотехнологии Лаба')
elif a == 5:
    print('Пятница разв...')
    print( d2, 'ОПД Пр, которого всё нет...')
    print( d3, 'Физра')
    print( d4, 'Линейная алгебра Пр')
    print( d5, 'Физика лаба')
elif a == 6 or a == 7:
    print('Каеф')
    print('Жызн прекрасна')
'''

#задача 3
'''
сначала выполняются операции умножения сложения 
 после операция сравнения 
 и в конце операторы "and" и "or"
 в ответе получим TRUE, 
 т.к. операторы сравнения и "and" и "or" 
выдают только bool тип данных
x = 5
y = 10
print( y > x * x  or  y >= 2 * x  and  x < y )
'''

#задача 4
'''
a=int(input())
if a // 100 == 0 and (a // 10 ) % 10 != 0: 
    print('Двузначное число')
else:
    print('число не двузначное')    
'''

#задача 5
'''
a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c: 
    print(a)
elif c >= b and c >= a :
    print(c)
elif b >= c and b >= a:
    print(b)
'''

#задача 6
'''
# суть задачи определить что за оперцию надо выполнить
a = int(input("прошу, введите число: "))
b = int(input("прошу, введите число: "))
c = input('введите операцию, \
    которую надо выполнить между числами: ')
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '/':
    print(a / b)
elif c == '*':
    print(a * b)
elif c == 'mod':
    print(a % b)
elif c == 'pow':
    print(a ** b)
elif c == 'div':
    print(a // b)
else:
    print('введены не правильные данные')
'''

#задача 7 
'''
a = int(input())
b = int(input())
if a % b == 0:
    print('число',a,'делится нацело на',b)
else:
    print('число',a,'не делится нацело на',b)
#проверим обратное, делится ли нацело число b на число a
a,b = b,a 
if a % b == 0:
    print('число',a,'делится нацело на',b)
else:
    print('число',a,'не делится нацело на',b)
'''

#задача 8 
'''
#создаём 3 переменные, в которые записываем  цифры
a = int(input())
num1 = a // 100
num2 = a // 10 % 10
num3 = a % 10
if num1 == num2 or num1 == num3 or num2 == num3:
    print('в этом числе есть одинаковые цифры')
else:
    print('в этом числе нет одинаковых цифр')
'''