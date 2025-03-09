from random import randint


def write_random_numbers(filename="data.txt", count=10):
    with open(filename, 'w') as file:
        for i in range(count):
            file.write(str(randint(1, count)) + "\n")
