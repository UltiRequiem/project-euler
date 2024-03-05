# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


def primes():
    candidate = 2

    primes = []

    while True:
        if all(candidate % number != 0 for number in primes):
            primes += [candidate]
            yield candidate

        candidate += 1


counter = 0
for prime in primes():
    counter += 1
    if counter >= 10:
        break
    print(prime)
