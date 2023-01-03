import random


#задача 1     
def square(n: int, ch: str):
    space = ' ' * len(ch)
    if len(ch) > n:
        return print('Квадрат с заданными условиями невозможно напечатать')
    [print(ch * n) if i == 0 or i == n - 1 else print(ch + space * (n - 2) + ch) for i in range(n)]

square(5, '|')



#задача 2
# print(all([True if i > 50 else False for i in [random.randint(1,100) for _ in range(5)]]))



#задача 3
# lst3 = []
# Father = ['milk','cucumbers','PIVO','fish']
# Grandmather = ['tea','sugar','сrackers']
# Mather = ['PIVO', 'fish']
# lst3 = (Father + Grandmather)
# for i in Mather:
#     lst.remove(i)
# print(f'Список покупок состоит из {len(lst)} продуктов,\n \
#     а именно: ', ', '.join(lst) + '.' )



#задача 4
# def it_is_here(n:int, lst: list):
#     if n in lst:
#         return True
#     return False

# n4 = int(input())
# lst4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# if it_is_here(n4, lst4):
#     print(f'число {n4} содержится в списке: ', *lst4 )
# else:
#     print(f'число {n4} не содержится в списке: ', *lst4 )



#задача 5
# def k_count(n5, lst5):
#     inp = 0
#     for i in lst5:
#         if n5 == i:
#             inp += 1
#     return inp

# lst5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 1, 1, 2, 2, 4]
# n5 = int(input())
# print(f'Данное число {n5} встретилось {k_count(n5, lst5)} раз в списке: ', *lst5)
