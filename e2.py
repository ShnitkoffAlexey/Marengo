lst = [1, 2, 3, 4, 5, 6, 1, 2, 3, 3, 3]
c = 0
for i in lst:
    if lst.count(i) % 2 == 0:
        c += 1
print(c/2)