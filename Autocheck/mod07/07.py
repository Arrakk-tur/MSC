# --- 7.1 ---

# setu = {
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
# }
# from setuptools import setup
#
#
# def do_setup(args_dict: dict):
#     setup(name=args_dict["name"],
#           version=args_dict["version"],
#           description=args_dict["description"],
#           url=args_dict["url"],
#           author=args_dict["author"],
#           author_email=args_dict["author_email"],
#           license=args_dict["license"],
#           packages=args_dict["packages"]
#     )

# --- 7.2 - 7.3 ---

# from setuptools import setup
#
#
# def do_setup(args_dict, requires, entry_points):
#     setup(name=args_dict['name'],
#           version=args_dict['version'],
#           description=args_dict['description'],
#           url=args_dict['url'],
#           author=args_dict['author'],
#           author_email=args_dict['author_email'],
#           license=args_dict['license'],
#           packages=args_dict['packages'],
#           install_requires=requires,
#           entry_points=entry_points
#           )

# --- 7.4 ---

# def data_preparation(list_data):
#     fin_l = []
#     for el in list_data:
#         if len(el) <= 2:
#             fin_l.extend(el)
#         else:
#             el.remove(min(el))
#             el.remove(max(el))
#             fin_l.extend(el)

#     return sorted(fin_l, reverse=True)

# # ml = [[1, 2, 3], [3, 4], [5, 6]]
# ml = [[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]
# print(data_preparation(ml))


# --- 7.5 ---

def all_sub_lists(data: list):
    fin_list = [[]]
    step = 1
    while step != len(data):
        for i in range(0, len(data)):
            fin_list.append(data[i:step])
        step += 1
    
    return fin_list

l = [4, 6, 1, 3]
print(all_sub_lists(l))