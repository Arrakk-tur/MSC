# --- 6.1 ---

# def write_employees_to_file(employee_list, path):
#     formated_list = ""
#     for emp_list in employee_list:
#         for emp in emp_list:
#             formated_list += emp + "\n"
#     f = open(path, "w")
#     f.write(formated_list.lstrip())
#     f.close()


# em_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
# path = "Autocheck/mod06/em_l.txt"
# write_employees_to_file(em_list, path)

# --- 6.2 ---

# def read_employees_from_file(path):
#     f = open(path, "r")
#     emp = []
#     for i in f.readlines():
#         if "\n" in i:
#             emp.append(i.removesuffix("\n"))
#         else:
#             emp.append(i)
#     f.close()
#     return emp

# path = "Autocheck/mod06/em_l.txt"
# read_employees_from_file(path)

# --- 6.3 ---

# def add_employee_to_file(record, path):
#     f = open(path, "a")
#     f.write((record + "\n"))
#     f.close()

# --- 6.4 ---

# def get_cats_info(path):
#     cats_info = []
#     with open(path, "r") as f:
#         for cat in f.readlines():
#             cat = cat.strip().split(",")
#             cat_dic = dict(id=cat[0], name=cat[1], age=cat[2])
#             cats_info.append(cat_dic)

#     return cats_info

# path = "Autocheck/mod06/cats.txt"
# get_cats_info(path)

# --- 6.5 ---


# def sanitize_file(source, output):
#     text = ''
#     with open(source, "r") as f_sour:
#         for source_text in f_sour.readline():
#             for ch in source_text:
#                 if ch.isdigit():
#                     source_text = source_text.replace(ch, "")
#             text += source_text
#     print(text)

#     with open(output, "w") as f_out:
#         f_out.write(text)

# source = "Autocheck/mod06/tex.txt"
# output = "Autocheck/mod06/tex_o.txt"
# sanitize_file(source,output)
