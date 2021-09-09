d_list = ['tut.by', 'yahoo.com', 'vk.ru', 'mail.ru', 'yandex.ru', 'live.ru', 'list.ru', 'internet.ru', 'gmail.com', 'bk.ru','inbox.ru', 'mail.com']
exc_list = ['.', '-', '_']
with open('src/email.txt', 'r', encoding='utf-8') as file:
    lst = []
    for num_mail in file:
        lst.append(num_mail.strip())
with open('src/output.txt', 'w', encoding='utf-8') as file:
    for mail in lst:
        check_1 = mail.split('@')
        if len(check_1) != 2:
            print('Wrong!')
            file.write('\n Wrong!')
        elif check_1[0] == '':
            print('Wrong!')
            file.write('\n Wrong!')
            break
        elif check_1[1] in d_list and len(check_1) == 2:
            if not check_1[0][0].isalnum() or not check_1[0][len(check_1[0])-1].isalnum():
                print('Wrong!')
                file.write('\n Wrong!')
            else:
                for i in range(len(check_1[0])-1):
                    if check_1[0][i] == check_1[0][i + 1]:
                        if not check_1[0][i:i + 1].isalnum():
                            print('Wrong!')
                            file.write('\n Wrong!')
                            break
                    elif check_1[0][i] in exc_list or check_1[0][i + 1] in exc_list:
                        continue
                    elif not check_1[0][i].isalnum():
                        print('Wrong!')
                        file.write('\n Wrong!')
                        break
                else:
                    print('Correct!')
                    file.write('\n Correct!')
        else:
            print('Wrong!')
            file.write('\n Wrong!')
