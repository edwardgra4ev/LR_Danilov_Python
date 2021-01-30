import math



def main(a, b, c, d):
    res = ((math.sin(c)**3) * (math.cos(a))**2)
    res_2 = (5 * (math.sin(b))**d)
    y = res/res_2
    return y


def information_output(y, a, b, c, d ):
    text_result = f"Из задачи:\n" \
                  f"y = (sin^3c * cos^2a) \ 5sin^db при a = {a} b = {b} c = {c} d = {d}" \
                  f"\nБыл получен следующий результат: {y}"
    print(text_result)


if __name__ == '__main__':
    a = 9.5
    b = 1.365
    c = 6.6
    d = 3
    y = main(a, b, c, d)
    information_output(y, a, b, c, d)