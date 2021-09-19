from Combat_check_1 import quick_punch
from Combat_check_2 import hard_fist
strength = 4
hp = 7
enemy_hp = 4
damage = 1
while hp >= 0 or enemy_hp >= 0:
    action = input(f'Выберите действие: 1 - быстрый удар; 2 - сильный удар;\n'
                   f'Ваше здоровье: {hp}\n'
                   f'Здоровье монстра: {enemy_hp}\n')
    if action == '1':
        res = quick_punch(strength)
        enemy_hp -= res
        hp -= damage
    elif action == '2':
        res = hard_fist(strength)
        enemy_hp -= res
        hp -= damage
    if hp <= 0:
        print('Вы погибли')
        break
    elif enemy_hp <= 0 :
        print('Монстр убит')
        break