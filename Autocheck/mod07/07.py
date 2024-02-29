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

# def all_sub_lists(data: list):
#     n = len(data)
#     fun_list = [[]]
#     for i in range(n):
#         for j in range(i+1, n+1):
#             fun_list.append(data[i:j])
#     return sorted(fun_list, key=len)

# l = [4, 6, 1, 3]
# print(all_sub_lists(l))

# --- 7.6 ---

# def make_request(keys: list, values: list):
#     fin_dict = {}
#     if len(keys) != len(values):
#         return fin_dict
#     else:
#         for i in keys:
#             ind_i = keys.index(i)
#             fin_dict[i] = values[ind_i]
#     return fin_dict
#
#
# k = ['name', 'age', 'email']
# v = ['Nick', '23', 'nick@test.com']
# print(make_request(k, v))

# --- 7.7 ---

# def file_operations(path, additional_info, start_pos, count_chars):
#     with open(path, "a") as f_w:
#         f_w.write(additional_info)
#
#     with open(path, "r") as f_r:
#         f_r.seek(start_pos)
#         return f_r.read(count_chars)

# --- 7.8 ---

# def get_employees_by_profession(path, profession):
#     # rjadok = ""
#     spysok = []
#     with open(path, 'r') as f:
#         lines = f.readlines()
#     for line in lines:
#         # if line.find(profession):
#         if profession in line:
#             spysok.append(line.replace(profession, "").strip())
#     rjadok = " ".join(spysok)
#
#     return rjadok
#
#
# p = "worker.txt"
# print(get_employees_by_profession(p, "courier"))
# # file = ['John courier\n', 'Pipe doc\n', 'Dan courier\n']
# # Функція працює неправильно. Необхідно повернути строку з імен через пробіл, ви повернули: 'John Pipe doc Dan'

# --- 7.9 ---

# def to_indexed(source_file, output_file):
#     output_text = []
#     with open(source_file, "r") as sf:
#         source_text = sf.readlines()
#     for line in source_text:
#         output_text.append(f"{source_text.index(line)}: " + line)
# 
#     with open(output_file, "w") as of:
#         of.writelines(output_text)
# 
# 
# to_indexed("source_file", "output_file")

