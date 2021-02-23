name = input('Введите имя ')
sname = input('Введите фамилию ')
age = int(input('Введите возраст '))
weight = int(input('Введите вес'))
if age<30 and ( weight>50 and weight<120):
    print(name,sname,',',age,'год,','вес',weight,'- хорошее состояние')
else:
    if (age>30 and age<40) and (weight<50 or weight>120):
        print(name, sname, ',', age, 'год,', 'вес', weight, '- следует заняться собой')
    else:
        if age>40:
            print(name, sname, ',', age, 'год,', 'вес', weight, '- следует обратится к врачу!')



