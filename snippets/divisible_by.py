def divisible_by(numbers: list[int], number: int):
    return [divisible for divisible in numbers if divisible % number == 0]

numbers = [4, 6, 18, 32, 24, 20, 42, 16, 54, 96, 112]

print(divisible_by(numbers, 6))
