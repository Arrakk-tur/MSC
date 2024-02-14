text = "sjvksnhdvksjvh sdlkvjvskdh sdjfj hfhfhhfeeeeeee eeee ds k sa a bdfbdeeeeeeeee"


def find_max_vowels(text:str):
    vowels = "aeiou"
    for char in text:
        if char.lower() not in vowels:
            text = text.replace(char, ".")
    chains = text.split(".")
    print(chains)
    print(text)
    res = max(chains)
    return res, len(res)

chain, l = find_max_vowels(text)
print(chain, ":", l)