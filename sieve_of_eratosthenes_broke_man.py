# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


def primes():
    candidate = 2
    found = []

    while True:
        # We can put all this logic in a few lines with reduce
        # It will even be more legible ig
        is_prime = True

        for item in found:
            if candidate % item == 0:
                is_prime = False
                break

        if is_prime:
            found.append(candidate)
            yield candidate

        candidate += 1


count = 0
for num in primes():
    count += 1
    print(num)

    if count >= 10:
        break
