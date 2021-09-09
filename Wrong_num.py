code = ['33', '44', '29', '25']
with open('src/input.txt', 'r', encoding='utf-8') as file:
    lst = []
    for num in file:
        lst.append(num.strip())
with open('src/output.txt', 'w', encoding='utf-8') as file:
    for phone in lst:
        if phone[0] == '+':
            if phone[1:].isdigit() and len(phone) == 13 and phone[4:6] in code:
                print(phone)
                file.write(f'\n {phone}')
            else:
                print('Wrong number')
                file.write('\n Wrong number')
        elif phone[0:2] == '80':
            if phone.isdigit() and len(phone) == 11 and phone[2:4] in code:
                print(phone)
                file.write(f'\n {phone}')
            else:
                print('Wrong number')
                file.write('\n Wrong number')
        else:
            print('Wrong number')
            file.write('\n Wrong number')
