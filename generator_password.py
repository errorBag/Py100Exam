import string
from random import choice


def generate_password(length=6, special_chars='!@#$%^'):
    """
    Генерация пароля заданной длины с использованием специальных символов.

    :param length: Длина пароля. По умолчанию 6 символов.
    :type length: int
    :param special_chars: Специальные символы для включения в пароль.
    :type special_chars: str
    :return: Сгенерированный пароль.
    :rtype: str
    """

    alphabet = string.ascii_letters + string.digits + special_chars
    password = ''.join(choice(alphabet) for _ in range(length))
    return password


def validate_input(value, min_value=6):
    """
    Валидация введенного значения.

    :param value: Введенное значение.
    :type value: int
    :param min_value: Минимально допустимое значение.
    :type min_value: int
    :return: True, если значение валидно, иначе False.
    :rtype: bool
    """
    if not isinstance(value, int) or value < min_value:
        print('Значение должно быть больше 5')
        return False
    return True


def save_password(password, file_name):
    """
    Запись пароля в файл.

    :param password: Пароль для записи.
    :type password: str
    :param file_name: Название файла для записи.
    :type file_name: str
    """
    with open(file_name, 'w') as f:
        f.write(password)


def main():
    """
    Основная функция с приветствием, запросом длинны пароля,
    валидацией, запросом записи в файл
    """
    print("Привет! Это программа генерации паролей.")

    while True:
        try:
            length = int(input("Введите длину пароля: "))
            if validate_input(length):
                break
        except ValueError:
            print('Введённое значение не является числом, повторите ввод!')

    special_chars = input("Введите специальные символы через запятую (необязательно): ")
    file_name = input("Введите имя файла для сохранения пароля (необязательно): ")

    password = generate_password(length, special_chars.strip() if special_chars else '')

    if file_name:
        save_password(password, file_name)
    else:
        print(password)

if __name__ == '__main__':
   main()
