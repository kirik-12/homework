
words = input().split()

d = {}
for i in words:
    i = i.upper()
    if i not in d:
        d[i] = 0
    if i in d:
        d[i] += 1

print('Слово: Количество:')
for i in d:
    print(i, d[i])
    