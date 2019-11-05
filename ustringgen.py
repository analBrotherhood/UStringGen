from random import randint as rt

alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

def main():
    try:
        generated_string = ''
        print('\n<======UStringGen======>')
        print('Шалом! Я могу сгенерировать строку из случайных символов любой длины!')
        print('Я написал эту прогу для генерации паролей - меняю их везде где только можно раз в несколько дней, или каждый раз когда логинюсь на незнакомом устройстве\\с незнакомого WiFi.')
        length = input('Введи необходимую длину строки: ')
        if length == '0':
            print('Введи ненулевое число! Строка из нулей символов - пробел.')
            main()
        try:
            int(length)
        except ValueError:
            if length == 'exit' or length == 'quit':
                print('Всего доброго! :D')
                exit()
            else:
                print('Введи число! Длина - это число!')
                main()
        for i in range(int(length)):
            generated_string += alphabet[rt(0, len(alphabet) - 1)]
        print('Сгенерирована строка: ' + generated_string)
        choice = input('Сгенерировать еще одну? (y/д/n/н): ')
        if choice in 'yesда':
            main()
        elif choice in 'noнет':
            print('\nВсего доброго! :D')
            exit()
        else:
            print('Ну и ладно. Даже один из 4х символов написать не можешь..')
            exit()

    except KeyboardInterrupt:
        print('\nВсего доброго! :D')
        exit()

main()
