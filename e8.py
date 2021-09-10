with open('src/input.txt', 'r', encoding='utf-8') as file:
    lst = []
    res = 0
    for s in file:
        lst.append(s.strip().split(' '))
    for student in lst:
        res += int(student[2])
        if int(student[2]) <= 3:
            print(student[0], student[1])
print(f'Средний балл по классу: {res/len(lst)}')