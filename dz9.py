# task 1
import json

with open('log_100.json', encoding = 'utf-8') as f:
    lst = json.load(f)

ip = {}

# подсчитаем сколько раз заходили с данного ip
for i in lst:
    if  i['ip'] not in ip:
        ip[i['ip']] = 0
    if i['ip'] in ip:
        ip[i['ip']] += 1

# подситаем количество ip с которых заходили один раз
count_1 = 0
for i in ip:
    if ip[i] == 1:
        count_1 += 1

#это список, состоящий из трёх наибольших значений. список состоит из кортежей
lol = sorted(ip.items(), key = lambda item: item[1], reverse = True)[:3] 
summ = 0
for i in range(len(lol)):
    summ += lol[i][1]

procent_max = summ / len(lst) * 100

print(procent_max, count_1)



# task 2

import csv
ip_c = {}
count_gen = 0
with open('log_full.csv', encoding = 'utf-8') as f:
    readed = csv.reader(f, delimiter = ',')
    for i in readed:
        count_gen += 1
        if i[1] == 'ip':
            continue
        if  i[1] not in ip_c:
            ip_c[i[1]] = 0
        if i[1] in ip_c:
            ip_c[i[1]] += 1
    # print(i[0], i[1], i[2])

ip_max = sorted(ip_c.items(), key = lambda item: item[1], reverse = True)[0]
proc_ip_max = ip_max[1] / count_gen * 100


# пройдёмся второй раз по файлу, т.к. нам известно какой уже ip больше всего встречается
# т.к. самая последняя запись встречается в конце, то нам достаточно просто запомнить последнее появление данного ip
with open('log_full.csv', encoding = 'utf-8') as f:
    readed = csv.reader(f, delimiter = ',')
    for i in readed:
        if i[1] == 'ip':
            continue
        if i[1] == ip_max[0]:
            last_time = i[0]
            last_user_agent = i[2]

suspicious_agent = {
    "ip": ip_max[0],                    # самый частовстречаемый ip в логах
    'fraction': proc_ip_max,            # процент запросов с таким ip от общего кол-ва запросов
    'count': ip_max[1],                 # число запросов с таким IP
    'last': {                           # вложенный словарь с 2-мя полями
        'agent': last_user_agent,       # последний user-agent для этого ip
        'timestamp': last_time,         # последний timestap для этого ip
    }
}

print(suspicious_agent)