# --- 8.1 ---

# from datetime import datetime
#
#
# def get_days_from_today(date: str):
#     today = datetime.now().date()
#     list_date = date.split("-")
#     new_date = datetime(year=int(list_date[0]),
#                         month=int(list_date[1]),
#                         day=int(list_date[2]))
#     difference = today - new_date.date()
#     return difference.days
#
#
# print(get_days_from_today("2022-02-24"))


# --- 8.2 ---

# from datetime import date
#
#
# def get_days_in_month(month, year):
#     given_date = date(year=year, month=month, day=1)
#     new_month = month+1
#     if new_month > 12:
#         next_month = given_date.replace(year=year+1, month=new_month - 12)
#     else:
#         next_month = given_date.replace(month=new_month)
#     days_in_month = next_month - given_date
#     return days_in_month.days
#
#
# print(get_days_in_month(12, 2023))


# --- 8.3 ---

# from datetime import datetime
#
#
# def get_str_date(date):
#     formatted_date = datetime.fromisoformat(date[:10]).date()
#
#     return formatted_date.strftime("%A %d %B %Y")
#
#
# print(get_str_date('2021-05-27 17:08:34.149Z'))


# --- 8.4 ---

# import random
#
# parti = {
#     "603d2cec9993c627f0982404": "test@test.com",
#     "603f79022922882d30dd7bb6": "test11@test.com",
#     "60577ce4b536f8259cc225d2": "test2@test.com",
#     "605884760742316c07eae603": "vitanlhouse@gmail.com",
#     "605b89080c318d66862db390": "elhe2013@gmail.com",
# }
#
#
# def get_random_winners(quantity, participants: dict):
#     if quantity > len(participants):
#         return []
#     else:
#         keys = list(participants.keys())
#         random.shuffle(keys)
#         win = random.sample(keys, k=quantity)
#         return win
#
#
# print(get_random_winners(4, parti))


# --- 8.5 ---

# from decimal import Decimal, getcontext
#
#
# def decimal_average(number_list, signs_count):
#     getcontext().prec = signs_count
#     summ = Decimal(0)
#     for i in number_list:
#         print(summ)
#         summ = Decimal(summ) + Decimal(i)
#     return Decimal(summ) / Decimal(len(number_list))
#
#
# print(decimal_average([4.5788689699797, 34.7576578697964, 86.8877666656633, 12], 6))

# --- 8.6 ---

# import collections
#
# Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
#
#
# def convert_list(cats):
#     cats_list = []
#     for cat in cats:
#         if isinstance(cat, tuple):
#             cats_list.append({"nickname": cat.nickname, "age": cat.age, "owner": cat.owner})
#         elif isinstance(cat, dict):
#             cats_list.append(Cat(cat["nickname"], cat["age"], cat["owner"]))
#
#     return cats_list
#     # print(cats_list)
#
#
# # convert_list([Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")])
# convert_list([
#     {"nickname": "Mick", "age": 5, "owner": "Sara"},
#     {"nickname": "Barsik", "age": 7, "owner": "Olga"},
#     {"nickname": "Simon", "age": 3, "owner": "Yura"},
# ])


# --- 8.7 ---
# 
# from collections import Counter
# 
# 
# def get_count_visits_from_ip(ips):
#     return Counter(ips)
# 
# 
# def get_frequent_visit_from_ip(ips):
#     return Counter(ips).most_common(1)[0]
