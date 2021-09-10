choice = {
    'Торт': ['Состав:мука, сахар, вода ...', 2.6, 1800],
    'Пирожное': ['Состав: сахар-песок, масло сливочное, молоко цельное сухое ...', 6, 400],
    'Маффин': ['Состав: Мука пшеничная, масло растительное, молоко цельное сухое ...', 1.2, 600]
}
prod = input()
if prod == 'Вся информация':
    print(choice.items())
if prod == 'Покупка':
    info = input()
    if info == 'Торт':
        c = int(input())
        print(round(choice.get('Торт')[1]*c, 2))
        if choice.get('Торт')[2] - c * 100 < 0:
            print('Недостаточно продукции')
        else:
            print('Осталось:', choice.get('Торт')[2] - c * 100)
    elif info == 'Пирожное':
        c = int(input())
        print(round(choice.get('Пирожное')[1] * c, 2))
        if choice.get('Пирожное')[2] - c * 100 < 0:
            print('Недостаточно продукции')
        else:
            print('Осталось:', choice.get('Пирожное')[2] - c * 100)
    elif info == 'Маффин':
        c = int(input())
        print(round(choice.get('Маффин')[1] * c, 2))
        if choice.get('Маффин')[2] - c * 100 < 0:
            print('Недостаточно продукции')
        else:
            print('Осталось:', choice.get('Маффин')[2] - c * 100)
    elif info == 'n':
        exit
info = input()
if prod == 'Торт':
    if info == 'Состав':
        print(choice.get('Торт')[0])
    elif info == 'Цена':
        print('Цена за 100 гр.:', choice.get('Торт')[1], 'руб')
    elif info == 'Количество':
        print(f'Количество:', choice.get('Торт')[2], 'г')
elif prod == 'Пирожное':
    if info == 'Состав':
        print(choice.get('Пирожное')[0])
    elif info == 'Цена':
        print('Цена за 100 гр.:', choice.get('Пирожное')[1], 'руб')
    elif info == 'Количество':
        print(f'Количество:', choice.get('Пирожное')[2], 'г')
elif prod == 'Маффин':
    if info == 'Состав':
        print(choice.get('Маффин')[0])
    elif info == 'Цена':
        print('Цена за 100 гр.:', choice.get('Маффин')[1], 'руб')
    elif info == 'Количество':
        print(f'Количество:', choice.get('Маффин')[2], 'г')
print('До свидания')
