"""Произвести следующую обработку 10 целых чисел:
найти количество отрицательных чисел, а числа, входящие в диапазон [0..10], умножить на 10.
"""

a = [1, -2, 3, 4, -5, 6, 7, 8, 9, 10]
negative_number = []
numbers = []

for i in a:
    if i < 0:
        negative_number.append(i)
    elif 0 <= i <= 10:
        numbers.append(i*10)
    else:
        pass

print("Колличество отрицательных чисел: {0}".format(len(negative_number)))
print("Числа в диапазоне [0..10] умноженные на 10: {0}".format(numbers))