import random
random_num = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')
def is_valid(s):
    if s.isdigit() and 1 <= int(s) <= 100:
        return True
    else:
        return False
while True:
    s = input()
    if is_valid(s) == True:
        integer_num = int(s)
        if integer_num == random_num:
            print('Вы угадали, поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        elif integer_num > random_num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif integer_num < random_num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
