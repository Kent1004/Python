name = input('Who creator ')
while name != 'Гвидо':
    print('Wrong!!!')
    name = input('Who creator ')
print('Success')










number = 43
value = int (input('Input number from 1 to 100'))
if value == number:
    print('Success')
else:
    if value > number:
        print ('Need smaller')
    else:
        print('Need more')