#Не понял как вернуть None при отсутствии Return
def num_translate(number):
    """Выводим перевод цифры с ENG to RU с соответствующм первым символом"""
    print(''.join(f'{key.title() if number.istitle() else key }' for key,value in dict.items() if value == number.lower()))

dict = {
    'один': 'one',
    'два': 'two',
    'три': 'three',
    'четыре': 'four',
    'пять': 'five',
    'шесть':'six',
    'семь' : 'seven',
    'восемь' : 'eight',
    'девять' : 'nine',
    'десять' : 'ten'
    }

num_translate(input("Enter number: "))
