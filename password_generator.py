import random
DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
chars = ''
how_much_password = int(input('Количество паролей для генерации'))
lenght_password = int(input('Длину одного пароля'))
numbers_in_password = input('Включать ли цифры 0123456789?; нет = н, да = д')
if 'д' in numbers_in_password:
    chars += DIGITS
uppercase_in_password = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?; нет = н, да = д')
if 'д' in uppercase_in_password:
    chars += UPPERCASE_LETTERS
lowercase_in_password = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?; нет = н, да = д')
if 'д' in lowercase_in_password:
    chars += LOWERCASE_LETTERS
symbol_in_password = input('Включать ли символы !#$%&*+-=?@^_?; нет = н, да = д')
if 'д' in symbol_in_password:
    chars += PUNCTUATION
fake_symbol_in_password = input('Исключать ли неоднозначные символы il1Lo0O; нет = н, да = д')
if 'д' in fake_symbol_in_password:
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')
def generate_password(lenght, chars):
    password = ''
    for i in range(lenght):
        password += random.choice(chars)
    return password
for _ in range(how_much_password):
    print(generate_password(lenght_password, chars))
