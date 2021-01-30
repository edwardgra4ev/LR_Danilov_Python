
"""Произвести следующую обработку 10 вещественных чисел:
найти количество чисел, больших или равных 1,5, и подсчитать сумму отрицательных чисел."""


def parsing_arr(arr, constant):
    """Функция парсинга входных данных
    Формирует 2 списка:
    list_result - числа больше константы
    list_negative_numbers - отрицательыне числа"""
    list_result = []
    list_negative_numbers = []
    for i in arr:
        if i >= constant:
            list_result.append(i)
        elif i < 0:
            list_negative_numbers.append(i)
    return list_result, list_negative_numbers


def sum_negative_numbers(list_negative_numbers):
    """Функция используется для подсчета суммы отрицательынх чисел"""
    return sum(list_negative_numbers)


def information_output(list_result, sum_result, constant, list_negative_numbers):
    """Функция обработки и вывода сообщения пользователю"""
    text = f"Колличество чисел, больших или равных {constant} : {len(list_result)}" \
           f"\nСписок числе больших или равных {constant}: {list_result}" \
           f"\nСумма отрицательных чисел: {sum_result}" \
           f"\nВсе отрицательные числа: {list_negative_numbers}"
    print(text)


if __name__ == '__main__':
    arr = [1.1, 2.2, 3.3, -1.2, -5.6, 2.22, 74.1, -5.3, 6.6, -10.10]
    constant = 1.5
    list_result, list_negative_numbers = parsing_arr(arr, constant)
    sum_result = sum_negative_numbers(list_negative_numbers)
    information_output(list_result, sum_result, constant, list_negative_numbers)


