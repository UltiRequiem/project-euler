import random

data = {"VENEZUELA": "CARACAS", "CANADA": "OTTAWA"}

country, capital = random.choice(
    list(data.items())
    # [(key,val) for key, val in data.items()]
)

print(country, capital)
