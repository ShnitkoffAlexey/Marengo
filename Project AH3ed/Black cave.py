import random
num = random.randint(1,1)
with open('src/Rivertown/Rivertown_Contacts.txt','r',encoding= 'utf-8') as file:
    print(file.readlines()[num])
from check_1 import dishonest_dice
knowledge = 5
res = dishonest_dice(knowledge)
Clue = 0
input()
if res is True:
    with open('src/Rivertown/Rivertown_Success.txt', 'r', encoding='utf-8') as file:
        print(file.readlines()[num])
    Clue += 1
else:
    with open('src/Rivertown/Rivertown_Failure.txt', 'r', encoding='utf-8') as file:
        print(file.readlines()[num])
