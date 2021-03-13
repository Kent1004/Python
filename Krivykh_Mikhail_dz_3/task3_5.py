
from random import choice,choices,shuffle, randint, sample

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

"""Функция - генератор шуток из заданных списков"""

def get_jokes(number):
    jokes=[]
    jokes.append(','.join(f'"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"' for i  in range(number)))
    print(jokes)

"""repeat принимает значение 1 или 2 ( 1 - генерация с повторами, 2 - генерация без повторов"""

def get_jokes_adv (number, repeat):
    jokes_adv=[]
    """Проверка на  флаг повтора"""
    if repeat == 2 :
        """Проверка сравнения аргумента количества шуток и макс длины списка, тк возможно вывести 5 шуток без повторов"""
        if number > len(nouns):
            """Промежуточные списки без повторов"""
            nounsNR = sample(nouns, 5)
            adverbsNR = sample(adverbs, 5)
            adjectivesNR = sample(adjectives, 5)
            jokes_adv.append(','.join(f'"{nounsNR[i]} {adverbsNR[i]} {adjectivesNR[i]}"' for i  in range(5)))
            print('Возможно сгенерировать только 5 шуток без потворов\n',jokes_adv)
        else:
            nounsNR = sample(nouns, number)
            adverbsNR = sample(adverbs, number)
            adjectivesNR = sample(adjectives, number)
            jokes_adv.append(','.join(f'"{nounsNR[i]} {adverbsNR[i]} {adjectivesNR[i]}"' for i in range(number)))
            print(jokes_adv)
    else:
        get_jokes(number)


get_jokes(6)
get_jokes_adv(8,1)
get_jokes_adv(6,2)
get_jokes_adv(3,2)







