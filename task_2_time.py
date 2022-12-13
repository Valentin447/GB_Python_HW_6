from timeit import timeit

print(timeit("my_func_1(value_x, value_y)",
             setup="from script_for_task_2 "
                   "import my_func_1, value_x, value_y"))
print(timeit("my_func_2(value_x, value_y)",
             setup="from script_for_task_2 "
                   "import my_func_2, value_x, value_y"))
print(timeit("my_func_test(value_x, value_y)",
             setup="from script_for_task_2 "
                   "import my_func_test, value_x, value_y"))
print(timeit("my_func_pow(value_x, value_y)",
             setup="from script_for_task_2 "
                   "import my_func_pow, value_x, value_y"))
'''
Результаты:
0.338670999975875
8.722956900019199
0.16139200003817677
0.1627489000093192

Функции возводили число 1.23 в степень -5. Первая с использованием оператора *,
вторая без * и без *, третья с помощю оператора **, четвертая с помощю 
функции pow модуля Math.
Самым быстрым оказался оператор **
'''
