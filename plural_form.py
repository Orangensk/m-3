def plural_form(number, f1, f2, f3):
    words = None
    if number == 1:
        words = f'{number} {f1}'
    elif number > 1 and number < 5:
        words = f'{number} {f2}'
    elif number >= 5:
        words = f'{number} {f3}'
    else:
        print('Неверное число')    
    return print(words)

plural_form(1, 'яблоко', 'яблока', 'яблок') #- 1 яблоко
plural_form(2, 'яблоко', 'яблока', 'яблок') #- 2 яблока
plural_form(11, 'студент', 'студента', 'студентов') #- 11 студентов
plural_form(15, 'студент', 'студента', 'студентов') #- 15 студентов
plural_form(3, 'студент', 'студента', 'студентов') #- 3 студента