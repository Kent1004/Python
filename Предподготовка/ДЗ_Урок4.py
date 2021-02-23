# первое задание
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

my_set_1 = set(my_list_1)
my_set_2 = set (my_list_2)
my_list_1 = list(my_set_1-my_set_2)
print((my_list_1))

# Второе задание
data = {
    'day':{
        '01':'первое',
        '02':'второе',
    },
    'month':{
        '01':'января',
        '02':'февраля',
    },
}
#userData=input('введите дату: ')
userData= '02.02.2016'
d, m, y = userData.split('.')
print (data['day'][d])
result = f'{data["day"][d]}  {data["month"][m]}  {y} года'
print(result)

# Третье задание
my_list_3 = [12, 2, 5, 12, 8, 2, 12]
result = []

for n in my_list_3:
     if my_list_3.count(n) == 1:
         result.append(n)
print (result)


