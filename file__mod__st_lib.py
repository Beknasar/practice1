"""
    4. Работа с файлами, модулями и стандартной библиотекой
    ✅ Задания:

    1) Напишите программу, которая создает текстовый файл data.txt, записывает в него 10 случайных чисел,
    а затем считывает их и выводит сумму.
    2) Разбейте программу из предыдущего задания на модули: один модуль для записи,
    другой для чтения и обработки данных.
    3) Используйте библиотеку datetime, чтобы вывести текущую дату и время в формате "DD-MM-YYYY HH:MM:SS".
"""
# 3
from datetime import datetime

# 2
from file_writer import write_random_numbers
from file_reader import read_random_numbers

write_random_numbers("data2.txt", 5)
numbers = read_random_numbers("data2.txt")
print(f"Числа из файла: {numbers}")
print(f"Сумма чисел: {sum(numbers)}")

# 1
from random import randint
with open('data.txt', 'w') as file:
    for i in range(10):
        file.write(str(randint(1, 10))+"\n")

with open('data.txt', 'r') as file:
    data = file.read()

print(data.split())
# map для использования функции на каждый элемент в списке
numbers = list(map(int, data.split()))
print(sum(numbers))

# 3 "DD-MM-YYYY HH:MM:SS" Вывод текущей даты и времени
current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(f"Текущее время: {current_time}")
