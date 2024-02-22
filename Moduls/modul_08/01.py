

# #### comprehantions #####





# fruits = ["mango", "kiwi", "strawberry", "guava", "pineapple", "mandarin", "orange"]
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# print([fruit for fruit in fruits if len(fruit) > 5])

# print([fruit.upper() if "o" in fruit else "$" + fruit for fruit in fruits])

# fruits_with_two_vowels = [
#     fruit
#     for fruit in fruits
#     if len([ch for ch in fruit if ch in "aeiou"]) == 2
# ]

# print(fruits_with_two_vowels)

original_dict = {
    "The Legend of Zelda: Ocarina of Time": 1998,
    "Grand Theft Auto IV": 2008,
    "Red Dead Redemption": 2018,
    "Perfect Dark": 2000,
    "The Orange Box": 2007,
}

res = {}

for name, year in original_dict.items():
    if year > 2005:
        res[name] = year
print(res)

res = {name: year if (year > 2005) else (name, None) for name, year in original_dict.items()}

print(res)