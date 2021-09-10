c = input('Введите число ')
try:
    f = int(c) ** 2
except ValueError:
    print('От вас требовалось ввести ЧИСЛО!')
else:
    print(f'Квадрат вашего число {f}')
finally:
    print('Завершение работы')