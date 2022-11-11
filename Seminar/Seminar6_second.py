# 41. Напишите программу вычисления арифметического выражения заданного строкой.
# Возможные операции в выражении только: +,-,/,*. приоритет операций стандартный.
# Техническое задание:
# 1) Числа могут быть только целые, любой размерности
# 2) Унарный оператор минус не рассматриваем, т.е. '-2*3' недопустимо
# 3) Не используйте функцию eval.
# 4) Программа возвращает результат вычисления в виде числа.
# Пример:
# '2+2' -> 4
# '1+2*3' -> 7
# '1-2*3' -> -5
# '1-2*33' -> -65
# '2-1+3*7' -> 10
# '1-2*3/5' -> -0.2
# '1+2*3-6*5+78' -> 55
# Общая схема решения:
# 1) Выделить части алгоритма, использовать для них функции.
# 2) Протестировать функции на множестве примеров, убедиться в правильности работы. Создать "модуль тестирования".
# Усложнение:
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# - Скобки рассматриваем однократные, нет учета вложенных скобок.
# - Не забыть протестировать граничные случаи: скобка в начале и/или в конце строки
# Пример:
# '(1+2)*3' -> 9;
# '(1-2)*3/5' -> -0.6
# '(1+2)*3-6*(5+78)' -> -489
# '(1+2)*(3-6)*(5+78)' -> -747



##https://habr.com/ru/post/50196/

from operator import add, sub, mul, truediv
from typing import Union

generic_number = Union[int, float]


def parse_string(expr_str: str) -> list:
    """
    Функция парсинга строки, выделения операторов, операндов и занесения их в список
    Работает с операторами /*-+
    Работает с операндами: целые числа
    TODO Добавить скобочки, возведение в степень, рациональные числа вида 1.23
    :param expr_str: Строка для парсинга
    :return: Список
    """
    rez = []
    start_digit = 0
    for idx, el in enumerate(expr_str):
        if el in '()/*-+':
            number_string = expr_str[start_digit:idx]
            if number_string != "": rez.append(int(number_string))
            rez.append(el)
            start_digit = idx + 1
    number_string = expr_str[start_digit:]
    if number_string != "": rez.append(int(number_string))
    return rez


def one_calc(op: str, prev_el: int, next_el: int) -> int:
    """
    Выполнение одного арифметического действия и возвращение результата
    :param op: Оператор в в виде строки
    :param prev_el: Операнд 1
    :param next_el: Операнд 2
    :return: результат выполнения в виде int
    """
    if op == "*":
        return prev_el * next_el
    elif op == "/":
        return prev_el / next_el
    elif op == "+":
        return prev_el + next_el
    elif op == "-":
        return prev_el - next_el
    else:
        raise TypeError("Некорректная операция")


def operation_calc(expr_list: list, operations: str) -> list:
    """
    Выполнение арифмитических операций для заданного распарсенного списка
    :param expr_list: Список операций и операндов
    :param operations: Операции в виде строки: "*/"  "-+"
    :return: Копию исходного списка, с произведенными заменами выполненных операций на соответствующие результаты
    """
    tmp_list = expr_list.copy()
    idx = 1
    lenght = len(tmp_list) - 1
    while idx <= lenght:  # Здесь цикл for подойдет плохо
        el = tmp_list[idx]
        if str(el) in operations:
            result = one_calc(el, tmp_list[idx - 1], tmp_list[idx + 1])
            tmp_list[idx] = result
            tmp_list.pop(idx + 1)
            tmp_list.pop(idx - 1)
            lenght -= 2
        else:
            idx += 1
    return tmp_list


def total_calc(expr_list: list) -> generic_number:
    tmp_list = expr_list.copy()
    while True:
        if "(" in tmp_list:
            parent_open = tmp_list.index("(")
            parent_close = tmp_list.index(")", parent_open)
            parent_expression = tmp_list[parent_open + 1: parent_close]
            in_parent_list = operation_calc(parent_expression, "*/")
            in_parent_list = operation_calc(in_parent_list, "-+")
            tmp_list[parent_open] = in_parent_list[0]
            tmp_list[parent_open+1: parent_close+1 ] = []
        else: break
    tmp_list = operation_calc(tmp_list, "*/")
    tmp_list = operation_calc(tmp_list, "-+")
    return tmp_list[0]


def calculate(expr_str: str)-> generic_number:
    return total_calc(parse_string(expr_str))



"""
Файл тестирования функций: заход на автотесты

"""

import task41_ariphmetic as code


def error_message(callback, test_data, result, require_result):
    print(f"Функция {callback.__name__}: ERROR in {test_data}: Получено {result}  Ожидалось: {require_result}")


def pass_message(callback, test_data, result, require_result):
    print(f"Функция {callback.__name__}: PASS in {test_data}: Получено {result}  Ожидалось: {require_result}")


def test_callback(callback, tests_data):
    for test, require in tests_data:
        result = callback(*test)
        if result != require:
            error_message(callback, test, result, require)
        else:
            pass_message(callback, test, result, require)


# '2+2'           ->  4
# '1+2*3'         ->  7
# '1-2*3'         -> -5
# '1-2*33'        -> -65
# '2-1+3*7'       -> 10
# '1-2*3/5'       -> -0.2
# '1+2*3-6*5+78'  -> 55

parse_string_tests = [
    [('2+2',), [2, '+', 2]],
    [('1+2*3',), [1, '+', 2, '*', 3]],
    [('1-2*3',), [1, '-', 2, '*', 3]],
    [('1-2*33',), [1, '-', 2, '*', 33]],
    [('2-1+3*7',), [2, '-', 1, '+', 3, '*', 7]],
    [('1-2*3/5',), [1, '-', 2, '*', 3, '/', 5]],
    [('1+2*3-6*5+78',), [1, '+', 2, '*', 3, '-', 6, '*', 5, '+', 78]],
    [('6/10*10+4',), [6, '/', 10, '*', 10, '+', 4]],
    [('(11+2/7)',), ['(', 11, '+', 2, '/', 7, ')']],
    [('(11+2)/7',), ['(', 11, '+', 2, ')', '/', 7]],
    [('(1+2)*3-6*(5+78)',), ['(', 1, '+', 2, ')', '*', 3, '-', 6, '*', '(', 5, '+', 78, ')']],

]

test_callback(code.parse_string, parse_string_tests)

# [[(i[1],), None] for i in parse_string_tests ]
# code. total_calc
calculate_tests = [
    [([2, '+', 2],), 4],
    [([1, '+', 2, '*', 3],), 7],
    [([1, '-', 2, '*', 3],), -5],
    [([1, '-', 2, '*', 33],), -65],
    [([2, '-', 1, '+', 3, '*', 7],), 22],
    [([1, '-', 2, '*', 3, '/', 5],), -0.19999999999999996],
    [([1, '+', 2, '*', 3, '-', 6, '*', 5, '+', 78],), 55],
    [([6, '/', 10, '*', 10, '+', 4],), 10],
    [(['(', 11, '+', 2, '/', 7, ')'],), 11.285714285714286],
    [(['(', 11, '+', 2, ')', '/', 7],), 1.8571428571428572],
    [(['(', 1, '+', 2, ')', '*', 3, '-', 6, '*', '(', 5, '+', 78, ')'],), -489],
]
test_callback(code.total_calc, calculate_tests)






# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] -> [2, 10]
# [1, 2, 3, 5, 1, 5, 3, 10, 1] -> [2, 10]
# [1, 2, 3, 1, 5, 7, 2, 3, 4, 1, 9] -> [4,5,7,9]
# Примечание:
# В этой задаче есть вариант решения "в лоб"(используя списки) или решения ээфективного(используя множества)

from time import perf_counter
from random import randint

def unique_set(lst: list):
    unique = set()
    not_unique = set()
    for el in lst:
        if el in unique:
            unique.remove(el)
            not_unique.add(el)
        elif el not in not_unique:
            unique.add(el)
    return list(unique)


def unique_list1(lst: list):
    rez = []
    for el in lst:
        if lst.count(el) == 1:
            rez.append(el)
    return rez


def unique_list2(lst: list):
    return [el for el in lst if lst.count(el) == 1]




if __name__ == "__main__":
    # lst = [1, 2, 3, 1, 5, 7, 2, 3, 4, 1, 9]  # [4,5,7,9]
    # lst = [1, 2, 3, 5, 1, 5, 3, 10, 1]

    lst = [randint(1,15) for _ in range(1000)]

    t1 = perf_counter()
    print(unique_set(lst))
    t2 = perf_counter()
    print(unique_list1(lst))
    t3 = perf_counter()
    print(unique_list2(lst))
    t4 = perf_counter()


    print(f"set: {t2-t1:.2e}; list: {t3-t2:.2e} comp: {t4-t3:.2e}")

# 100:   set: 4.25e-05; list: 1.33e-04 comp: 1.23e-04
# 1000:  set: 8.94e-05; list: 1.49e-02 comp: 1.39e-02






