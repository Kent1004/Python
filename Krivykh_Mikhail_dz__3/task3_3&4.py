"""В задании предполагаем, что была введена поризвольная строка имен  или имен с  фамилиями"""

def thesaurus(names):
    dict1 = dict()
    for name in sorted(names.replace(' ','').split(',')):
        if dict1.get(name[0:1].title()) == None:
            dict1[name[0:1].title()] = name.title().split()
        else:
           dict1[name[0:1].title()].append(name.title())
    print(dict1)

def thesaurus_adv(fio):
    dict2 = dict()
    sn1 = []
    """Создаем список фамилий """
    for name in (fio.split(',')):
        sn=name.strip(' ').split(' ')
        sn1.append(sn[1].title())
    """Создаем в словаре отсортированные ключи ( первые букв фамилий) со значением словарь"""
    for surname in sorted(sn1):
        if dict2.get(surname[0:1].title()) == None:
            dict2[surname[0:1].title()] = {}
    """Для каждого ключа в в верхнем словаре проверяям первые буквы фамилий в цикле и добавляем при соответсвии вложенный словарь"""
    for key in dict2.keys():
        for name in sorted(fio.split(',')):
            if (name.strip(" ").title().split())[1][0] == key:
                """вводим переменную nm  - первая буква имени"""
                nm = (name.strip(" ").title().split())[0][0]
                if dict2[key].get(nm) == None:
                    dict2[key][(name.strip(" ").title().split())[0][0]] = [name.title()]
                else:
                    dict2[key][nm].append(name.title())
    print(dict2)

list = '  иван , Ильдар , илья , Денис , Жанна,Миахил, Эдуард  '
thesaurus (list)
list2 = 'Петр Алексеев, иван иванов ,Инна Ираидовна , Михаил Хорошев, Мага Харян, Анна Савельева ,Дмитрий Авакумов'
thesaurus_adv (list2)
