"""Переписать первые элементы каждой строки матрицы A (mn),
 большие С, в массив В. Если в строке нет элемента, большего С, то записать ноль в массив В. """
import numpy as np


def mat(nrows, ncols, constant):
    arr = np.random.randint(10, size=(nrows, ncols))
    arr_result = []
    for i in arr:
        if i[0] > constant:
            arr_result.append(i[0])
        elif i[0] < constant:
            arr_result.append(0)
    return arr, arr_result


def information_output(nrows, ncols, constant, arr, arr_result):
    text = f"При M = {nrows} и N = {ncols}, построена матрица:\n" \
           f"{arr}\n" \
           f"Из нее был получен массив:\n{arr_result}\n" \
           f"При константе = {constant}"
    print(text)

if __name__ == "__main__":
    nrows = int(input('Укажите значение M для матрицы A:  '))
    ncols = int(input('Укажите значение N для матрицы A:  '))
    constant = int(input('Укажите число C:  '))
    arr, arr_result = mat(nrows, ncols, constant)
    information_output(nrows, ncols, constant, arr, arr_result)
