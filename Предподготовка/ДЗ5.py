'''
asd
asd
asd
asd
'''


import random
pcNumber=[]
number = int(input('Я загадываю Число :'))
end = 100
start =1
pcNumber.append(random.randint(1,100))
print('PC вводит число : ', pcNumber)
i=0
while number != pcNumber[i]:
    stepN = input('Указываю горячо или холодно\n')
    i+=1
    print('start ', start)
    print('end ', end)
    if stepN == '>':
        start = pcNumber[i-1]
        pcNumber.append(random.randint(start, end))
        print('PC вводит число : ', pcNumber[i], ' колво попыток ' , i )
    elif stepN == '<':
        end=pcNumber[i-1]
        pcNumber.append(random.randint(start, end))
        print('PC вводит число : ', pcNumber[i], ' колво попыток ' , i )
print('PC угадал')



