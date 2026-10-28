# Project Euler

> **Status: archived.** Solutions and experiments from 2021, kept as a reference.

My Python solutions to some [Project Euler](https://projecteuler.net) problems, plus a few small experiments
I did on the way. Each file runs on its own with `python3 <file>.py` (Python 3.9+).

## Problems

| Problem | File | Answer |
|---|---|---|
| [#1 Multiples of 3 or 5](https://projecteuler.net/problem=1) | [multiples_of_3_or_5.py](./multiples_of_3_or_5.py) | 233168 |
| [#2 Even Fibonacci numbers](https://projecteuler.net/problem=2) | [even_fibonacci_numbers.py](./even_fibonacci_numbers.py), a generator that stops at four million | 4613732 |
| [#3 Largest prime factor](https://projecteuler.net/problem=3) | [prime_factors.py](./prime_factors.py) | 6857 (the largest of its factors) |
| [#5 Smallest multiple](https://projecteuler.net/problem=5) | [smallest_multiple.py](./smallest_multiple.py), solved on paper first ([the paper](./smallest_multiple.png)), then with `math.lcm` | 232792560 |
| [#13 Large sum](https://projecteuler.net/problem=13) | [large_sum.py](./large_sum.py) | 5537376230 |

## Experiments

| File | What it is |
|---|---|
| [fibonacci.py](./fibonacci.py) | the plain recursive Fibonacci ([diagram](./fibonacci.jpg)); slow, which is the point |
| [factorial.py](./factorial.py) | recursive versus `math.prod`, timed (it also notes how much slower it is to import inside the function) |
| [sieve_of_erastothenes.py](./sieve_of_erastothenes.py), [sieve_of_eratosthenes_broke_man.py](./sieve_of_eratosthenes_broke_man.py) | two generators of prime numbers |
| [snippets/](./snippets) | dictionary and dictionary comprehension examples |
| [evelin_homework.py](./evelin_homework.py) | an estimate of blood alcohol concentration I wrote for a friend's homework. Not medical advice |

## Notes

The first version of `large_sum.py` cut every number to ten digits before adding them, which loses the carry from the
digits that were dropped and gets the last digit wrong. It now adds the full numbers first.

## License

MIT, see [LICENSE](./LICENSE).
