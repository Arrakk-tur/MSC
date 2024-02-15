# def real_len(text: str):
#     n_text = text
#     spec = ["\n", "\f", "\r", "\t", "\v"]
#     for i in spec:
#         if i in n_text:
#             n_text = n_text.replace(i, "")
#     print(n_text)

#     return len(n_text)


# real_len('Alex\nKdfe23\t\f\v.\r')

# def is_check_name(fullname: str, first_name):
#     return fullname.startswith(first_name)

# print(is_check_name('Alex Old', 'Alex'))

# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone


# def get_phone_numbers_for_countries(list_phones):
#     clear_phones = []
#     phone_list = {
#     "UA": [],
#     "JP": [],
#     "TW": [],
#     "SG": []
#     }

#     for phone in list_phones:
#         clear_phones.append(sanitize_phone_number(phone))

#     for phone in clear_phones:
#         if phone.startswith("81"):
#             phone_list["JP"].append(phone)
#         elif phone.startswith("65"):
#             phone_list["SG"].append(phone)
#         elif phone.startswith("886"):
#             phone_list["TW"].append(phone)
#         else:
#             phone_list["UA"].append(phone)
    
#     return phone_list


# CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
# TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# TRANS = {}
# for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
#     TRANS[ord(c)] = l
#     TRANS[ord(c.upper())] = l.upper()
# # print(TRANS)

# def translate(name: str):
#     transcript = name.translate(TRANS)
#     return transcript

# print(translate("Дмитро Короб"))

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
# 
# 
# def formatted_grades(students: dict):
#     res = []
#     index = 0
#     for key, value in students.items():
#         index += 1
#         for g_key, g_val in grades.items():
#             if value == g_key:
#                 num_drade = g_val
# 
#         res.append(f"{index:>4}|{key:<10}|{value:^5}|{num_drade:^5}")
#     return res
# 
# 
# studen = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
# print(formatted_grades(studen))

# 
# def formatted_numbers():
#     res = [f"|{'decimal':^10}|{'hex':^10}|{'binary':^10}|"]
#     for i in range(16):
#         res.append(f"|{i:<10d}|{i:^10x}|{i:>10b}|")
#     return res

# import re
#
#
# def find_word(text, word):
#     result = re.search(word, text)
#     res = {
#         'result': (True if result is not None else False),
#         'first_index': (result.span()[0] if result is not None else None),
#         'last_index': (result.span()[1] if result is not None else None),
#         'search_string': word,
#         'string': text
#     }
#
#     return res
#
# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "Python"))
