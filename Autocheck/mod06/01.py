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

# --- 6.6 ---

# def save_applicant_data(source, output):

#     with open(output, "w") as f_out:
#         for i in source:
#             f_out.write(f"{i['name']},{i['specialty']},{i['math']},{i['lang']},{i['eng']}\n")
        


# source = [
#     {
#         "name": "Kovalchuk Oleksiy",
#         "specialty": 301,
#         "math": 175,
#         "lang": 180,
#         "eng": 155,
#     },
#     {
#         "name": "Ivanchuk Boryslav",
#         "specialty": 101,
#         "math": 135,
#         "lang": 150,
#         "eng": 165,
#     },
#     {
#         "name": "Karpenko Dmitro",
#         "specialty": 201,
#         "math": 155,
#         "lang": 175,
#         "eng": 185,
#     },
# ]
# output = "Autocheck/mod06/stude_o.txt"
# save_applicant_data(source, output)

# --- 6.7 ---

# def is_equal_string(utf8_string: bytes, utf16_string: bytes):
#     if utf8_string.decode('utf-8') == utf16_string.decode('utf-16'):
#         return True
#     else:
#         return False

# --- 6.8 ---

# def save_credentials_users(path, users_info: dict):
#     with open(path, "wb") as f:
#         for k, v in users_info.items():
#             f.write(f"{k}:{v}\n".encode())

# users_info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}
# path = "Autocheck/mod06/users.txt"
# save_credentials_users(path, users_info)

# --- 6.9 ---

# def get_credentials_users(path):
#     users = []
#     with open(path, "rb") as f:
#         for line in f.readlines():
#             users.append(line.decode().rstrip())
    
#     return users

# --- 6.10 ---

# import shutil



# def create_backup(path, file_name, employee_residence: dict):
#     file_path = path + "/" + file_name
#     with open(file_path, "wb") as f:
#         for k, v in employee_residence.items():
#             f.write(f"{k} {v}\n".encode())

#     backup_folder = shutil.make_archive("backup_folder", "zip", path)

#     return backup_folder

# employee_residence = {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}
# file_name = "file_b"
# path = "Autocheck/mod06/arch"

# create_backup(path, file_name, employee_residence)

# --- 6.11 ---

# import shutil


# def unpack(archive_path, path_to_unpack):
#     shutil.unpack_archive(archive_path, path_to_unpack)