"""Произвести следующую обработку 15 целых чисел:
найти количество отрицательных чисел и подсчитать разность положительных чисел.
"""


a = [-15, -2, 3, 4, -5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
negative_number = []
numbers = []

for i in a:
    if i < 0:
        negative_number.append(i)
    elif i > 0:
        numbers.append(str(i))
    else:
        pass

print("Колличество отрицательных чисел: {0}".format(len(negative_number)))
print("Разность положительных чисел: {0}".format(eval('-'.join(numbers))))