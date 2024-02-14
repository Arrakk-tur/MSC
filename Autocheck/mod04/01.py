# def amount_payment(payment):
#     res = 0
#     for i in payment:
#         if i < 1:
#             continue
#         else:
#             res = res + i
#     return res


# def prepare_data(data: list):
#     data = data.sort()    
#     data_min = data.remove(data[0])
#     data_max = data_min.remove(data_min[-1])
#     return data_max


# def prepare_data(data):
#     data = sorted(data)    
#     data.remove(data[0])
#     data.remove(data[-1])
#     return data


# prepare_data([-3, 1, 0, 11, 10, 100, 1, -5])



# def get_grade(key):
#     grade = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5 }
#     try:
#         return grade[key]
#     except KeyError:
#         return None

# def get_description(key):
#     grade = {"F": "Unsatisfactorily", "FX": "Unsatisfactorily", "E": "Enough", "D": "Satisfactorily", "C": "Good", "B": "Very good", "A": "Perfectly"}
#     try:
#         return grade[key]
#     except KeyError:
#         return None


# def lookup_key(data: dict, value):
#     res = []
#     for key, value in data.items():
#         res.append(key)
#     return res

# def game(terra, power):
#     energy = power
#     for i in terra:
#         for j in i:
#             if j > energy:
#                 break
#             else:
#                 energy = energy + j
    
#     return energy
                
# print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1))     
                
# def is_valid_pin_codes(pin_codes):
#     res = True
#     if ((len(pin_codes) != len(list(set(pin_codes))))
#             or (len(pin_codes) == 0)):
#         return False  # Є дублікати
#     elif res:
#         for pin in pin_codes:
#             if (type(pin) is not str  # Не рядок
#                     or not pin.isdigit()  # Не число
#                     or len(pin) != 4):  # Не дорівнює 4
#                 res = False

#     return res

# def is_valid_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     set_pswd = set(password)
#     if len(password) < 8:  # Довжина рядка пароля вісім символів.
#         return False
#     else:
#         for ch in set_pswd:
#             if ch.isdigit():          # Містить хоча б одну цифру
#                 has_num = True
#             elif ch.islower():          # Містить хоча б одну літеру у нижньому регістрі.
#                 has_lower = True
#             elif ch.isupper():          # Містить хоча б одну літеру у верхньому регістрі.
#                 has_upper = True

#     return has_upper and has_lower and has_num

import pathlib


# def parse_folder(path):
#     files = []
#     folders = []
#     for i in path.iterdir():
#         if i.is_dir():
#             folders.append(i.name)
#         else:
#             files.append(i.name)

#     return files, folders