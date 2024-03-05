# https://en.wikipedia.org/wiki/Fibonacci_sequence

def fibonacci(number: int):
    if number == 1:
        return 0
    if number == 2:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


for item in range(1, 14):
    print(fibonacci(item))
