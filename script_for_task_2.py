'''
4) Программа принимает действительное положительное число x и
целое отрицательное число y. Необходимо выполнить возведение числа
x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения
числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в
степень с помощью оператора *. Второй — более сложная реализация без
оператора *, предусматривающая использование цикла.
'''

from math import pow

value_x = 1.23
value_y = -5


def my_func_1(x, y):
    y = abs(y)
    count = 1
    res = x
    if y == 0:
        res = 1
    while count < y:
        res *= x
        count = count + 1
    return 1 / res


def my_func_2(x, y):
    '''
    Возведение в степень без использования операторов * и **
    :param x: Основание степени. Действительное положительное число (float)
    :param y: Значение степени. Целое отрицательное число (int)
    :return: Возвращает первый аргумент возведенный в степень равной
    второму аргументу
    '''
    y = abs(y)
    res_fractional = 0
    x_str = str(x)
    if x % 1 == 0:
        x_int = int(x)
        x_str_int = str(x_int)
    else:
        for fr in range(y):
            res_fractional += len(x_str) - (x_str.find(".") + 1)
        x_int = int(x_str.replace(".", ""))
        x_str_int = str(x_int)
    t1 = x_int
    res_x = x
    if y == 1:
        sum_x = x_int
    elif y == 0:
        sum_x = 1
    for i in range(1, y):
        ratings = "0"
        sum_x = 0
        count_x = x_int
        for j in range(len(x_str_int)):
            for k in range(count_x % 10):
                sum_x += t1
            count_x = count_x // 10
            t1 = int(str(t1) + ratings)
        t1 = sum_x
    if len(str(sum_x)) < res_fractional:
        res_str = str(sum_x)
        for el in range(res_fractional - len(str(sum_x))):
            res_str = "0" + res_str
        res_x = float("0." + res_str)
    elif res_fractional != 0:
        res_x = float(str(sum_x)[0:-res_fractional] +
                      "." + str(sum_x)[-res_fractional:])
    else:
        res_x = sum_x
    return 1 / res_x


def my_func_test(x, y):
    return x ** y


def my_func_pow(x, y):
    return pow(x, y)
