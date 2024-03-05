# --- 10.2 ---

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#
#     def say(self):
#         pass
#
# animal = Animal("m", 12)

# --- 10.3 ---

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#
#     def say(self):
#         pass
#
#     def change_weight(self, weight):
#         self.weight = weight
#
#
# animal = Animal("Simon", 10)
#
# animal.change_weight(12)


# --- 10.4 ---

# class Animal:
#     color = "white"
# 
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
# 
#     def say(self):
#         pass
# 
#     def change_weight(self, weight):
#         self.weight = weight
# 
#     def change_color(self, new_color):
#         Animal.color = new_color

# 
# first_animal = Animal("m", 10)
# second_animal = Animal("l", 13)
# second_animal.change_color("red")