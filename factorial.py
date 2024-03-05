import math
# really big diference if you import inside de function

def factorialR(number: int):
    return 1 if number <= 1 else number * factorialR(number - 1)


def factorialL(number: int):

    return math.prod([item for item in range(1, number + 1)])


import time

print("---Recursive---")
recursive_start = time.time()

print(factorialR(500))

recursive_time = time.time() - recursive_start

print(f'The recursive function took {recursive_time} seconds.')

print("---Loop---")

loop_start = time.time()

print(factorialL(500))

loop_time = time.time() - loop_start
print(f'The loop function took {loop_time} seconds.')

print("---Comparition--")
# TODO
