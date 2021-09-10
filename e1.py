lst = [1, 4, 6, 8, 1, 'abc', 4, 3, 0, 'cda', 'abc']
for i in lst:
    if not lst.count(i) > 1:
        print(i)