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

# class Animal:
#     color = "white"

#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight

#     def change_color(self, color):
#         Animal.color = color


# first_animal = Animal("m", 10)
# second_animal = Animal("l", 13)
# second_animal.change_color("red")
# print(Animal.color)
# print(first_animal.color)