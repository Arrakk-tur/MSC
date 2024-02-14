# CrazyFrogSoung > crazy_frog_soung


def convert_camel_to_snake(text):

    res = ""
    j = 0
    for char in text:
        if char.isupper():
            if j == 0:
                res = res + char.lower()
            else:
                res = res + "_" + char.lower()
        else:
            res = res + char
        j += 1  # j = j + 1 
    return res


s = "CrazyFrogSound"

new_title = convert_camel_to_snake(s)
print(new_title)