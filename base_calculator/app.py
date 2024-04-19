print("Привет! Я простой калькулятор.")


def calculate_operation(a: int, b: int, operation: str):
    """
    Вычисляет результат математической операции между двумя числами.

    :param a: Первое число для операции.
    :type a: int or float
    :param b: Второе число для операции.
    :type b: int or float
    :param operation: Операция для выполнения (+, -, *, /)
    :type operation: str
    :return: Результат операции.
    :rtype: int or float
    """
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        raise ValueError("Недопустимая операция")


def validate_int_input(text: str):
    """
    Функция преобразовывает строковое значение в тип int,
    тем самым проверяя является ли введённое значение числом
    :return: int
    """
    while True:
        try:
        # Пользовательский ввод
            a = input(text)
            return int(a)
        except ValueError:
            print('Введённое значение не является числом, повторите ввод!')


def validate_operation():
    while True:
        operation = input("Введите операцию ( + , - , * , / ):  ")
        if operation not in ('+', '-', '*', '/'):
            print("Некорректный ввод. Пожалуйста, попробуйте снова.")
            continue
        return operation


if __name__ == '__main__':
    a = validate_int_input('Введите первое число: ')
    operation = validate_operation()
    b = validate_int_input('Введите второе число: ')

    # результат округляем до 3 знаков после запятой
    result = round(calculate_operation(a, b, operation), 3)
    print(f"Результат операции: {result}")