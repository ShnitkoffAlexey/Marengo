c_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
c_2 = (45, 21, 124, 76, 5, 23, 91, 234)
res_1 = 0
res_2 = 0
lst_1 = []
lst_2 = []
for i in c_1:
    res_1 += i
    lst_1.append(i)
for i in c_2:
    res_2 += i
    lst_2.append(i)
if res_1 > res_2:
    print('Сумма элементов c_1 больше суммы элементов c_2')
else:
    print('Сумма элементов c_2 больше суммы элементов c_1')
lst_1.sort()
lst_2.sort()
print(lst_1[0], lst_1[len(lst_1)-1])
print(lst_2[0], lst_2[len(lst_2)-1])
