# https://projecteuler.net/problem=3

import math


def is_prime_number(number: int):
    # Que solo sea divisible por si mismo y la unidad
    for x in range(2, int(math.sqrt(number) + 1)):
        if number % x == 0:
            return False

    return True


def prime_numbers():
    count = 2

    while True:
        if is_prime_number(count):
            yield count

        count += 1


def find_prime_factors(number: int):
    prime_factors = []

    for prime in prime_numbers():
        if number % prime == 0:
            prime_factors.append(prime)

            # Esto siempre sera un integer conceptualmente
            number = int(number / prime)

            if number == 1:
                break

    return prime_factors


number = 600851475143

prime_factors = find_prime_factors(number)

print(prime_factors)
