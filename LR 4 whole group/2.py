"""Произвести следующую обработку 15 целых чисел:
найти количество четных чисел, а нечетные числа, входящие в диапазон [1..11] возвести в квадрат.
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
even_number = []
odd_number = []

for i in a:
    if i % 2 == 0:
        even_number.append(i)
    elif 1 <= i <= 11:
        odd_number.append(i**2)
    else:
        pass

print("Колличество четных чисел: {0}".format(len(even_number)))
print("Не четные числа возведенные в квадрат: {0}".format(odd_number))