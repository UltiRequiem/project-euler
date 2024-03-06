def starts_with(text: list[str] | str, letter: str):
    return [word for word in text if word.startswith(letter)]


names = ["Anne", "Amy", "Bob", "David", "Carrie", "Barbara", "Zach"]

print(starts_with(names, "B"))
