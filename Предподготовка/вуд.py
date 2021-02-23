import random

print('загадайте чиcло')
print('а я попытаюсь его угадать')

min = 1
max = 100

while True:
    number = random.randint(min, max)
    print(min)
    print(max)
    print ('вы загадали число: ', number)
    znak = input('я угадал? или укажите больше или меньше:  ')
    if znak == '=':
        print('ура!!! я угадал')
        break
    elif znak == '>':
        min = number
        print('Ваше число больше, попытаюсь еще раз')
    elif znak == '<':
        max = number
        print('Ваше число меньше, попытаюсь еще раз')
    print('end')