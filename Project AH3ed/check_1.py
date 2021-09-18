def dishonest_dice(stat: int) -> bool:
    import random
    cont = 0
    lst = []
    res = 0
    while cont <= stat:
        a = random.randint(0, 100)
        lst.append(a)
        cont += 1
    for i in lst:
        if i in range(90, 100):
            res += 1
    if res > 0:
        return True
    else:
        return False
