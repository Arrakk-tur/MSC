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

def data_preparation(list_data: list):
    fin_l = []
    m_f = []
    for el in list_data:
        while len(el) > 2:
            el.remove(min(el))
            el.remove(max(el))
        else:
            fin_l.extend(el)

    m_f = fin_l.sort(reverse=True)
    return m_f


ml = [[1, 2, 3], [3, 4], [5, 6]]
print(data_preparation(ml))
