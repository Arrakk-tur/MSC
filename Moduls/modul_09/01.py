fruits = ["apple", "orange", "kiwi", "mango", "rosberry"]


def sorted_fruits(fruits):
    return fruits.sort(reversed=True)

sorted_fruits = lambda fruits: fruits.sort(reversed=True)