# --- 9.1 ---

# def get_grade(key):
#     grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
#     return grade.get(key, None)


# def get_description(key):
#     description = {
#         "A": "Perfectly",
#         "B": "Very good",
#         "C": "Good",
#         "D": "Satisfactorily",
#         "E": "Enough",
#         "FX": "Unsatisfactorily",
#         "F": "Unsatisfactorily",
#     }
#     return description.get(key, None)


# def get_student_grade(option):
#     if option == "grade":
#         return get_grade
#     elif option == "description":
#         return get_description
#     else:
#         return None


# --- 9.2 ---

# DEFAULT_DISCOUNT = 0.05


# def get_discount_price_customer(price, customer: dict):
#     discount = DEFAULT_DISCOUNT
#     if "discount" in customer.keys():
#         discount = customer["discount"]
        
#     return price * (1 - discount)


# --- 9.3 ---

# def caching_fibonacci():
#     cahe = {}
#     def fibonacci(n):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         elif n not in cahe.keys():
#             cahe[n] = fibonacci(n - 1) + fibonacci(n - 2)
#         return cahe[n]
#     return fibonacci


# --- 9.4 ---

# def discount_price(discount):
#     def inner(price):
#         return price * (1 - discount)
#     return inner


# --- 9.5 ---

#
# def format_phone_number(func):
#     def inner(phone):
#         new_phone = (
#             phone.strip()
#             .removeprefix("+")
#             .replace("(", "")
#             .replace(")", "")
#             .replace("-", "")
#             .replace(" ", "")
#         )
#         return func(new_phone)
#
#     return inner
#
#
# @format_phone_number
# def sanitize_phone_number(phone):
#     if len(phone) == 12:
#         return "+" + phone
#     elif len(phone) == 10:
#         return "+38" + phone
#     else:
#         return phone
#
#
# print(sanitize_phone_number(' +38(050)123-32-34'))


# --- 9.6 ---

# def normal_name(list_name):
#     return list(map(lambda i: i.capitalize(), list_name))

# --- 9.7 ---


# def get_emails(list_contacts):
#     return list(map(lambda i: i["email"], list_contacts))
#
#
# n = [{
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": False,
#     }]
# print(get_emails(n))


# --- 9.8 ---
#
# def positive_values(list_payment):
#     return list(filter(lambda i: i > 0, list_payment))


# --- 9.9 ---
#
#
# def get_favorites(contacts):
#     return list(filter(lambda i: i["favorite"] is True, contacts))

# --- 9.10 ---

# from functools import reduce
#
#
# def sum_numbers(numbers):
#     return reduce(lambda x, y: x + y, numbers)
