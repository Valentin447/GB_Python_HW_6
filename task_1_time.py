'''
1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ,
что вы сделали и чего удалось добиться
'''

from timeit import timeit

print(timeit("my_func()", setup="from script_for_task_1 import my_func"))
print(timeit("sorted_func()",
             setup="from script_for_task_1 import sorted_func"))
print(timeit("sort_func()", setup="from script_for_task_1 import sort_func"))

'''
Результат:
0.3323196000419557
0.3980855999980122
0.3174532998818904

Функция №-1 my_func() - начальная, без использования встроиных функций 
сортировки. Для сравнения добавил функции с использованием sort() и sorted(). 
В результате самой быстрой оказалась с использованием sort(), 
а самой медленной с использованием sorted()
'''
