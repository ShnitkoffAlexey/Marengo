lst_1 = [35, 78, 21, 37, 2, 98, 6, 100, 231]
lst_2 = [45, 21, 124, 2, 6, 23, 91, 234]
c = 0
for i in lst_1:
    if i in lst_2:
        c += 1
print(c)