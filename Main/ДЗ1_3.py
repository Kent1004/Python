number = int(input('Введите число от 0 до 20 '))

if number>=5 and number<=20 or number == 0:
    print(number,'процентов')
elif number < 5 and number > 1 :
    print(number, 'процента')
elif number == 1:
    print(number, 'процент')
else :
    print('Ввели число за указанным диапозоном')
#Проверка
print('Проверка склонения "процент" до 20:\n')
for i in range(0,20):
    number = i
    if number >= 5 and number <= 20 or number == 0:
        print(number, 'процентов')
    elif number < 5 and number > 1:
        print(number, 'процента')
    elif number == 1:
        print(number, 'процент')

