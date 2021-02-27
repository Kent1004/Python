'''
duration = int(input('Для прекращение введите 911, введите промежуток времени в секундах  '))
d = duration // (3600 * 24)
h = duration % (3600 * 24) // 3600
m = duration % 3600 // 60
s = duration % 3600 % 60
'''
duration = 0
while duration != 911:
    duration = int(input('Для прекращение введите 911, введите промежуток времени в секундах  '))
    d = duration // (3600 * 24)
    h = duration % (3600 * 24) // 3600
    m = duration % 3600 // 60
    s = duration % 3600 % 60
    if d == 0 and h!=0 and m!= 0:
        print(f' {h} час, {m} мин, {s} сек')
    elif d == 0 and h == 0 and m!=0:
        print(f'{m} мин, {s} cек')
    elif d == 0 and h == 0 and m == 0:
        print(f'{s} сек')
    else:
        print(f' {d} сут,  {h} час, {m} мин, {s} сек')
