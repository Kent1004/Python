top5='Первые пять мест : 1. Иванов 2. Петров 3. Сидоров 4. орлов 5. соколов'
# Поздравить топ 3 участников

startIndex = top5.find('1')
endIndex = top5.find('4')
top3 = top5[startIndex:endIndex]
result = 'Поздрравляем {} c успехом'.format(top3.upper())
print(result)
hero = 'Superman'
#hero = 'Super'
if hero.find('man') != -1:
    print('Ест')

if 'man' in hero:
    print ('Есть2')

print ('ChampionShip')
count = int (input ('Number of members: '))
i = count
members = []
while i>0:
    name = input('Who win  {} place'.format(i))
    members.append(name)
    i-=1
members.reverse()
result = members[:3]
result = 'Победители: {}. Поздравляем!'.format(result)
print(result)
# сортировка по алфавиту
print( sorted(members))

 # RANGE
 #numbers= [1,2,3,5,6,78,9]
 numbers2=range(10)
print(list(numbers2))
winners=['ssd','sdasdasd','aqasedqw3']
for i in range(len(winners))
    #print (i)
    print( i , ')' , winners[i])

#  нечетные числа
print(list(range(1,1000,2)))

for number in range(1,1000,2):
    print (number)