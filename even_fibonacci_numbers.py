FOUR_MILLION = 4000000


def fibonacci():
    a = 1
    b = 2

    while True:
        yield a

        a, b = b, a + b # elegant lol


result = 0

for item in fibonacci():
    if item > FOUR_MILLION:
        break

    if item % 2 == 0:
        result += item


print(result)
