"""Произвести следующую обработку 10 вещественных чисел:
найти количество чисел, равных нулю, и найти сумму чисел, входящих в диапазон [-15..15]
"""

a = [-15, -2, 3, 4, -5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
number_null = []
numbers_list = []

for i in a:
    if i == 0:
        number_null.append(i)
    elif -15 <= i <= 15:
        numbers_list.append(i)
    else:
        pass

print("Колличество чисел равных 0: {0}".format(len(number_null)))
print("Сумма чисел в диапазоне [-15..15] : {0}".format(sum(numbers_list)))