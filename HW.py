#task 1
'''
print('введите 2 строки длиной более двух символов')
a = input()
b = input()
if len(a) >= 2 and len(b) >= 2:
    if a > b:
        print(a)
    else:
        print(b)
else:
    print('ERROR')
'''

#task 2
'''
a = input('введите строку с чётным количеством символов: ')
print(a[:len(a)//2:2] + a[len(a)//2::2])
'''

#task 3
'''
# в данной задаче проверили лишь только 3 домена gmail.com, mail.ru, yandex.ru
# так же не стал проверять количество точек 
a = input().strip().lower()
if a.count('@') == 1 and a.find(' ') == -1 and \
            (a.find('@gmail.com') != -1 or a.find('@mail.ru') != -1 or a.find('@yandex.ru') != 1) and \
            (a.endswith('@gmail.com') or a.endswith('@mail.ru') or a.endswith('@yandex.ru')): 
    if a.index('@') == 0 or a.index('.') == 0: #чтобы у нас не было таких ситуаций: "@gmail.com", ".dfd@gmail.com"
        print('ввели не корректно')
    else:
        print('адрес введён корректно')
else:
    print('ввели не корректно')
'''

#task 4
'''
a = input('Введите предложение:').split()
print(f'количество слов в предложении: {len(a)}')
'''

#task 5
'''
# если правильно понял задачу, то надо просто подсчитать 
# количество "ch" в введённой строке 
a = input('введите что-нибудь для создания чудес: ').lower()
print( f"в данной строке символов \'ch\' содержится в количестве: {a.count('ch')}" )
'''