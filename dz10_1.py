import os


def error(command):
    print(f'lol: command not found: {command}')


def lol(i, path):
    comands_action_dict = {
        'ls': os.listdir(path),
        'cd': os.chdir(path),
        'pwd': os.getcwd(),
        'mkdir': os.mkdir(path),
        'touch': open(path, 'w'),
        'rm': os.remove(path),
    }

    return comands_action_dict[i]

comands_name = ['ls', 'cd' , 'pwd', 'mkdir', 'touch', 'rm']

while True:
    a = input().split()

    if not(a[0] in comands_name):
        error(a[0])
        continue

    for i in comands_name:
        if i == a[0]:
            lol(i, a[1])
            break
    
