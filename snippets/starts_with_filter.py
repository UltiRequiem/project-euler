def starts_with(text: list[str] | str, letter: str):
    return filter(lambda word: word.startswith(letter), text)


names = ["Anne", "Amy", "Bob", "David", "Carrie", "Barbara", "Zach"]

print(starts_with(names, "B"))



