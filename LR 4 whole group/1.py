"""Произвести следующую обработку 15 целых чисел:
найти количество отрицательных чисел, количество нулевых и подсчитать сумму положительных чисел.
"""

a = [-1, -2, -3, -4, -5, 6, 7, 0, 9, 0, 11, 12, 13, 14, 15]
negative_numbers = []
numbers_null = []
positive_numbers = []
for i in a:
    if i < 0:
        negative_numbers.append(i)
    elif i == 0:
        numbers_null.append(i)
    else:
        positive_numbers.append(i)

print("Колличество отрицательных чисел: {0}".format(len(negative_numbers)))
print("Колличество нулевых чисел: {0}".format(len(numbers_null)))
print("Cумма положительных чисел: {0}".format(sum(positive_numbers)))