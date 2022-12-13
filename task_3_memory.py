'''
Задайте число. Составьте список чисел Фибоначчи,
в том числе для отрицательных индексов.
Пример:
для k = 8 список будет выглядеть так:
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''
from memory_profiler import profile
import numpy


@profile
def my_func():
    k = 30000
    if k == 0:
        fib_list = [0]
    else:
        fib_list = [1, 0, 1]
    for el in range(1, k):
        fib_list.insert(0, fib_list[1] - fib_list[0])
        fib_list.append(fib_list[-1] + fib_list[-2])


@profile
def my_func_np():
    k = 30000
    if k == 0:
        fib_list = numpy.array([0])
    else:
        fib_list = numpy.array([1, 0, 1])
    for el in range(1, k):
        numpy.insert(fib_list, 0, fib_list[1] - fib_list[0])
        numpy.append(fib_list, fib_list[-1] + fib_list[-2])


my_func()
my_func_np()

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    12     37.7 MiB     37.7 MiB           1   @profile
    13                                         def my_func():
    14     37.7 MiB      0.0 MiB           1       k = 30000
    15     37.7 MiB      0.0 MiB           1       if k == 0:
    16                                                 fib_list = [0]
    17                                             else:
    18     37.7 MiB      0.0 MiB           1           fib_list = [1, 0, 1]
    19    122.6 MiB     -1.9 MiB       30000       for el in range(1, k):
    20    122.6 MiB     38.2 MiB       29999           fib_list.insert(0, fib_list[1] - fib_list[0])
    21    122.6 MiB     42.7 MiB       29999           fib_list.append(fib_list[-1] + fib_list[-2])


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    24     51.7 MiB     51.7 MiB           1   @profile
    25                                         def my_func_np():
    26     51.7 MiB      0.0 MiB           1       k = 30000
    27     51.7 MiB      0.0 MiB           1       if k == 0:
    28                                                 fib_list = numpy.array([0])
    29                                             else:
    30     51.7 MiB      0.0 MiB           1           fib_list = numpy.array([1, 0, 1])
    31     51.7 MiB -158555.9 MiB       30000       for el in range(1, k):
    32     51.7 MiB -158553.6 MiB       29999           numpy.insert(fib_list, 0, fib_list[1] - fib_list[0])
    33     51.7 MiB -158555.4 MiB       29999           numpy.append(fib_list, fib_list[-1] + fib_list[-2])
    
Использование numpy уменьшило потребляемую память с 122.6 MiB до 51.7 MiB
'''