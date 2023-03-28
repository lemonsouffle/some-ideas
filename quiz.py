import random

def question(c):
    global used_countries
    while True:
        k = random.choice(list(c))
        try:
            if k not in used_countries:
                used_countries.append(k)
                break    
        except NameError:
            used_countries = []
            if k not in used_countries:
                used_countries.append(k)
                break
    ans = input(f'Введите столицы следующей страны: {k} ')
    if ans.title() == c[k]:
        print('Правильный ответ!')
        return 1
    else:
        print('Не правильный ответ!')
        return 0
        

countries = {
    'Нидерланды': 'Амстердам',
    'Турция': 'Анкара',
    'Греция': 'Афины',
    'Казахстан': 'Астана',
    'Таиланд': 'Бангкок',
    'Сербия': 'Белград',
    'Венгрия': 'Будапешт',
    'Польша': 'Варшава',
    'США': 'Вашингтон',
    'Австрия': 'Вена',
    'Германия': 'Берлин',
    'Франция': 'Париж',
    'Армения': 'Ереван',
    'Великобритания': 'Лондон',
    'Россия': 'Москва',
    'Украина': 'Киев',
    'Чехия': 'Прага',
    'Норвегия': 'Осло',
    'Китай': 'Пекин',
    'Япония': 'Токио',
    'Болгария': 'София',
    'Швеция': 'Стокгольм',
    'Грузия': 'Тбилиси',
    'Монголия': 'Улан-Батор'
}

score = 0
for i in range(10):
    score += question(countries)
print(f'Количество набранных очков: {score}')
