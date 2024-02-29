
# class Animal:
#     def __init__(self, nickname, is_vaccinated):
#         self.nickname = nickname
#         self.is_vaccinated = is_vaccinated
    

#     def get_info(self):
#         return(f"It is animal. His name is {self.nickname}, vaccinated {self.is_vaccinated}")


# class Cat(Animal):
#     def __init__(self, nickname, is_vaccinated, color="black"):
#         super().__init__(nickname, is_vaccinated)
#         self.color = color


#     def get_info(self):
#         base_info = super().get_info()
#         print(base_info + f", color {self.color}")

# class Dog(Animal):
#     pass

# cat  = Cat(nickname="Myron", is_vaccinated=True, color="red")
# cat.get_info()

# dog = Dog("Baili", True)
# dog.get_info()