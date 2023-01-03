def k_isalpha(s: str) -> bool:
    '''This function determines if a string consists of only letters 
    \n Works for Russian and English'''
    i = 0
    while i < len(s):
        if not('Z' >= s[i] >= 'A' or 'z' >= s[i] >= 'a' or 'Я' >= s[i] >= 'А' or 'я' >= s[i] >= 'а'):
            return False
        i += 1
    return True


def k_islower(s: str) -> bool:
    i = 0
    j = 0
    while i < len(s):
        if k_isalpha(s[i]) == True:
            if 'Z' >= s[i] >= 'A' or 'Я' >= s[i] >= 'А':
                return False
            j += 1
        i += 1
    if j > 0: return True
    else: return False


def k_istitle(s: str) -> bool:
    i = 0
    d = s.split()
    while i < len(d):
        j = 1
        substring = d[i]
        if not(substring[0].isalpha()) or 'Z' <= substring[0] <= 'A' or 'z' >= substring[0] >= 'a':
            return False
        while j < len(substring):
            if 'Z' >= substring[j] >='A':
                return False
            j += 1
        i += 1
    return True


def  k_upper(s: str) -> str:
    i = 0
    d = ''
    while i < len(s):
        if s[i].isalpha():
            if 'Z' >= s[i] >= 'A':
                d = d + s[i]
            elif 'z' >= s[i] >= 'a':
                d = d + chr(ord(s[i]) - 32)
            elif 'я' >= s[i] >= 'а':
                d = d + chr(ord(s[i]) - 32)
            elif 'Я' >= s[i] >= 'А':
                d = d + s[i]
        else: d = d + s[i]
        i += 1 
    return d


def k_endswith(s: str, substring: str) -> bool:
    i = -len(substring)
    while i < 0:
        if s[i] != substring[i]:
            return False
        i += 1
    return True


def k_count(s: str, substring: str) -> int:
    i = 0
    inp = 0 # кол-во вхождения подстроки
    d = len(substring)
    if substring == '':
        return len(s) + 1
    while i < len(s):
        if s[i] == substring[0]: #проверка есть ли совпадения по первому символу, если есть, то переходим в цикл
            j = 0
            t = True
            while j < len(substring): #проверяем полностью ли соответсвует подстрока
                if s[i] != substring[j]: # если строка не соответствует то выходим из цикла
                    t = False #необходимо для подсчёта вхождений
                    break
                i += 1
                j += 1
            if t: inp += 1 #если из цикла не выходили, то t есть правда
            i -= 1 #необходимо для того чтобы мы не пропускали букву когда выхоим из цикла
        i += 1
    return inp


def k_strip(s: str) -> str:
    d = ''
    if s[-1] == ' ':
        i = -1
        j = -len(s)
        while i > -len(s) :
            if s[i] != ' ':
                j = i
                break
            i -= 1
        d = s[:j + 1]
    else:
        d = s
    
    if len(d) >= 2:
        if d[-1:] == '\n' or d[-1:] == '\t':
            d = d[:-1]  

    if d[0] == ' ':
        i = 0
        while i < len(d):
            if s[i] != ' ':
                break
            i += 1
        d = d[i:]
    else:
        d = d 

    return d


def k_replace(s: str, oldvalue: str, newvalue: str, count: int) -> str:
    ''' s - строка входящая, oldvalue - то что нам надо искать и заменить, newvalue - то на что мы заменим, count - сколько раз мы будем заменять'''
    i = 0
    time_count = 0      # для сравнения сколько раз уже вставили
    if len(oldvalue) > len(s):
        return s
    if oldvalue == s:
        return newvalue
    while i < len(s):
        if s[i] == oldvalue[0]:     #проверка есть ли совпадения по первому символу, если есть, то переходим в цикл
            i_inp = i               #запоминаем вхождение
            j = 0
            while j < len(oldvalue):    #проверяем полностью ли соответсвует подстрока
                if s[i] != oldvalue[j]: #если строка не соответствует то выходим из цикла
                    i_inp = -1          #необходимо для запоминания,что это вхождение не меняем
                    break
                i += 1
                j += 1
            if i_inp != -1 and time_count < count:  #если из цикла не выходили, то i_inp больше 0
                s = s[:i_inp] + newvalue + s[i:]    #тогда вырезаем oldvalue и в это место вставляем newvalue
                time_count += 1
            elif time_count == count: break      #это условие для экономии времени
            i -= 1                          #необходимо для того чтобы мы не пропускали букву когда выхоим из цикла
        i += 1

    return s



