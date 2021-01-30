"""Произвести следующую обработку 15 вещественных чисел:
найти количество отрицательных чисел, а числа, входящие в диапазон [0..10] возвести в квадрат.
.
"""
a = [1, -2, 3, 4, -5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
negative_number = []
numbers_powers = []

for i in a:
    if i < 0:
        negative_number.append(i)
    elif 0 <= i <= 10:
        numbers_powers.append(i**2)
    else:
        pass

print("Колличество отрицательных чисел: {0}".format(len(negative_number)))
print("Числа в диапазоне [0..10] возведенные в квадрат: {0}".format(numbers_powers))