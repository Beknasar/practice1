def read_random_numbers(filename="data.txt"):
    with open(filename, 'r') as file:
        data = file.read()
    # map для использования функции на каждый элемент в списке
    numbers = list(map(int, data.split()))
    return numbers
