#Список для варианта 1
temp  = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#Списки для варианта 2
temp2  = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
temp3 = []
result = ''
#Списки для варианта 3
temp4 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result2 = ''


#Вариант 1 : без добавления элементов в список, обработка уже имеющихся элементов
for i in range(len(temp)):
    if temp[i].isdigit():
            temp[i] = f'"{int(temp[i]):02d}"'
    else:
        for symbol in temp[i]:
            if symbol.isdigit():
                temp[i] = f'"{temp[i][0]}{int(temp[i][1:]):02d}"'
                break
print ('Вариант 1 без добавления элементов в список, обработка уже имеющихся элементов:\n',temp)
print (' '.join(temp))

#Вариант 2 : С добавленеим новых элементов в новый список

for lst in temp2:
    if lst.isdigit():
           temp3.extend(['"',f'{int(lst):02d}','"'])
           result += ''.join(f' "{int(lst):02d}"')
    elif lst.isalnum():
        temp3.append(lst)
        result += ''.join(f' {lst}')
    else:
        for symbol in lst:
            if symbol.isdigit():
                temp3.extend(['"', f'{lst[0]}{int(lst[1:]):02d}' , '"'])
                result += ''.join(f' "{lst[0]}{int(lst[1:]):02d}"')
                break

print ('Вариант 2 С добавленеим новых элементов в новый список:\n',temp3)
print (result)


#Вариант 3 : С добавленеим новых элементов в тот же список
j=0
while temp4[j] != temp4[-1]:
    if temp4[j].isdigit():
        temp4.insert(j,'"')
        temp4[j+1] = f'{int(temp4[j+1]):02d}'
        temp4.insert(j+2, '"')
        result2 += ''.join(f' "{int(temp4[j+1]):02d}"')
        j+=3
    elif temp4[j].isalnum():
        result2 += ''.join (f' {temp4[j]}')
        j+=1
    else:
        for symbol in temp4[j]:
            if symbol.isdigit():
                temp4.insert(j,'"')
                temp4[j+1] = f'{temp4[j + 1][0]}{int(temp4[j + 1][1:]):02d}'
                temp4.insert(j + 2, '"')
                result2+= ''.join(f' "{temp4[j + 1][0]}{int(temp4[j + 1][1:]):02d}"')
                break
        j += 3
else:
    result2+=''.join(f' {temp4[-1]}')
print('Вариант 3 С добавленеим новых элементов в тот же список:\n',temp4)
print (result2)




