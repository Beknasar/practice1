"""
3. Исключения, декораторы, генераторы
✅ Задания:

1. Напишите функцию, которая запрашивает у пользователя число и делит 100 на это число.
Обработайте исключение ZeroDivisionError и ValueError.
2. Напишите декоратор timeit, который измеряет время выполнения функции и выводит его в консоль.
3. Напишите генератор fibonacci(n), который возвращает n первых чисел Фибоначчи.
"""
# 2
from time import time


def timeit(function):
    def wrapper_function():
        start = time()
        function()
        end = time() - start
        print(f"Время выполнения программы: {end}")
    return wrapper_function



# 1
@timeit
def division_from_100():
    try:
        number = float(input("Введите, пожалуйста, число: "))
        print(100 / number)
    except ValueError as error:
        print(f"{error}. Нужно вводить только числа!")
    except ZeroDivisionError:
        print("Нельзя делить на ноль!")


division_from_100()


# F(n) = F(n-1) + F(n-2), F(0) = 1, F(1) = 1
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b


res_fib = list(fibonacci(10))
result = '\nF(n) = F(n-1) + F(n-2), F(0) = 1, F(1) = 1'
result += f'\n{"n":^4}'
for i in range(len(res_fib)):
    result += f'|{i+1:^4}'
result += "\n"+("-"*4+"|")*len(res_fib) +"-"*4+ "\n"
result += f'{"F(n)":^4}'
for i in range(len(res_fib)):
    result += f'|{res_fib[i]:^4}'
print(result)

# TIC TAC TOE Fields
# size = 3
# cells = []
# empty_cells = size ** 2
# for i in range(size):
#     cells.append(["-"] * size)
# result = '\n'
# result += " " * 3
# for i in range(size):
#     result += f'|{i:^3}'
# result += "\n"+("-"*3+"|")*size + "-"*3+ "\n"
#
# for i in range(2):
#     result += f"{i:<3}"
#     for j in range(size):
#         result += f"|{cells[i][j]:^3}"
#     result += "\n"+("-"*3+"|")*size +"-"*3+ "\n"
# print(result)
