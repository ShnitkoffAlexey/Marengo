text = 'An apple a day keeps the doctor away'
symbol_1 = input()
symbol_2 = input()
symbol_3 = input()
wok_1 = {}
wok_1[symbol_1] = text.count(symbol_1)
wok_1[symbol_2] = text.count(symbol_2)
wok_1[symbol_3] = text.count(symbol_3)
print(wok_1.items())
