# task 1


def read_last(lines: int, file: str):
    li = []
    with open(file, 'r') as f: 
        li = f.readlines()
    if lines == 0:
        return []
    return li[-lines::]

# print(read_last(3,'file.txt'))


# task 2

def longest_words(file: str):
    with open(file, 'r', encoding = 'utf8') as f:
        max_word = []
        for i in f.readlines(): # идём по тексту (по строкам или по столбцу)

            strin = sorted(i.strip().split(), key = len)[::-1] 
            # тут провели сортировку по длине и самые длиные слова поместили в начало
            
            list_max_word_strin = [strin[j] for j in range(len(strin)) if len(strin[0]) <= len(strin[j])]
            # создали список, в котором находятся самые длинные слова строчки, которую мы только что просмотрели
            # с помощью генератора сравниваем  по длине слова и сразу создаём по ним список самых длинных слов данной строки
            
            if len(max_word) == 0: # в даннх ветвелниях запомниаем самые длинные слова
                max_word = list_max_word_strin
            elif len(max_word[0]) < len(list_max_word_strin[0]):
                max_word = list_max_word_strin
            elif len(max_word[0]) == len(list_max_word_strin[0]):
                max_word = max_word + list_max_word_strin 
            
        #print(max_word)
        return max_word
      
# print(longest_words('article.txt'))

# task 3

def get_basket_amount(file: str) -> int:
    summ = 0
    with open(file, 'r', encoding='utf8') as f:
        for i in f.readlines(): #считаем уже сумму заказа
            strin = i.strip().split()
            summ = summ + int(strin[1]) * int(strin[2])
            
    return summ

# print(get_basket_amount('prices.txt'))

