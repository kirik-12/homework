import os


def error(command):
    print(f'lol: command not found: {command}')


# def lol(i, path):
#     comands_action = [os.listdir(path), os.chdir(path), os.getcwd(), os.mkdir(path)]
#     return comands_action[i]

comands_name = ['ls', 'cd' , 'pwd', 'mkdir', 'touch', 'rm']

while True:
    a = input().split()

    if not(a[0] in comands_name):
        error(a[0])
        continue

    if len(a) == 1:
        if a[0] == 'ls':
            print(os.listdir('.'))
        elif a[0] == 'pwd':
            print(os.getcwd())
    elif len(a) == 2:
        if a[0] == 'ls':
            print(os.listdir(a[1]))
        elif a[0] == 'cd':
            print(os.chdir(a[1]))
        elif a[0] == 'mkdir':
            print(os.mkdir(a[1]))
        elif a[0] == 'touch':
            open(str(a[1]) + '.txt', 'w')
        elif a[0] == 'rm':
            os.remove(a[1])
    elif len(a) == 3:
        if a[0] == 'rm' and a[1] == '-rf-':
            for f in os.listdir(a[2]):
                os.remove(os.path.join(a[2], f))
            os.rmdir(a[2])
            continue
    
    

