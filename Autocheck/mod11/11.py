# # --- 11.2 ---

# # class Point:
# #     def __init__(self, x, y):
# #         self.__x = x
# #         self.__y = y

# #     @property
# #     def x(self):
# #         return self.__x

# #     @x.setter
# #     def x(self, value):
# #         self.__x = value

# #     @property
# #     def y(self):
# #         return self.__y

# #     @y.setter
# #     def y(self, value):
# #         self.__y = value

# # # Приклад використання класу Point
# # p1 = Point(3, 4)
# # print("Coordinates of point p1: ({}, {})".format(p1.x, p1.y))

# # p1.x = 5
# # p1.y = 6
# # print("New coordinates of point p1: ({}, {})".format(p1.x, p1.y))


# # --- 11.3 ---


# # class Point:
# #     def __init__(self, x, y):
# #         self.__x = None
# #         self.__y = None
# #         self.x = x
# #         self.y = y

# #     @property
# #     def x(self):
# #         return self.__x

# #     @x.setter
# #     def x(self, x):
# #         if type(x) == int or type(x) == float:
# #             self.__x = x           

# #     @property
# #     def y(self):
# #         return self.__y

# #     @y.setter
# #     def y(self, y):
# #         if type(y) == int or type(y) == float:
# #             self.__y = y


# # --- 11.4 ---

# # class Point:
# #     def __init__(self, x, y):
# #         self.__x = None
# #         self.__y = None
# #         self.x = x
# #         self.y = y

# #     @property
# #     def x(self):
# #         return self.__x

# #     @x.setter
# #     def x(self, x):
# #         if (type(x) == int) or (type(x) == float):
# #             self.__x = x

# #     @property
# #     def y(self):
# #         return self.__y

# #     @y.setter
# #     def y(self, y):
# #         if (type(y) == int) or (type(y) == float):
# #             self.__y = y


# # class Vector:
# #     def __init__(self, coordinates: Point):
# #         self.coordinates = coordinates

# #     def __setitem__(self, index, value):
# #         if index == 0:
# #             self.coordinates.x = value
# #         elif index == 1:
# #             self.coordinates.y = value

# #     def __getitem__(self, index):
# #         if index == 0:
# #             return self.coordinates.x
# #         elif index == 1:
# #             return self.coordinates.y


# # --- 11.5 ---


# # class Point:
# #     def __init__(self, x, y):
# #         self.__x = None
# #         self.__y = None
# #         self.x = x
# #         self.y = y

# #     @property
# #     def x(self):
# #         return self.__x

# #     @x.setter
# #     def x(self, x):
# #         if (type(x) == int) or (type(x) == float):
# #             self.__x = x

# #     @property
# #     def y(self):
# #         return self.__y

# #     @y.setter
# #     def y(self, y):
# #         if (type(y) == int) or (type(y) == float):
# #             self.__y = y

# #     def __str__(self):
# #         return f"Point({self.x}, {self.y})"


# # class Vector:
# #     def __init__(self, coordinates: Point):
# #         self.coordinates = coordinates

# #     def __setitem__(self, index, value):
# #         if index == 0:
# #             self.coordinates.x = value
# #         if index == 1:
# #             self.coordinates.y = value

# #     def __getitem__(self, index):
# #         if index == 0:
# #             return self.coordinates.x
# #         if index == 1:
# #             return self.coordinates.y

# #     def __str__(self):
# #         return f"Vector({self.coordinates.x}, {self.coordinates.y})"
    

# # point = Point(1, 10)
# # vector = Vector(point)

# # print(point)  # Point(1,10)
# # print(vector)  # Vector(1,10)


# # --- 11.6 ---


# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value is None:
#             return self.coordinates.x, self.coordinates.y
#         else:
#             return self.coordinates.x * value, self.coordinates.y * value

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"


# # --- 11.7 ---


# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         new_x = self.coordinates.x + vector.coordinates.x
#         new_y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(new_x, new_y))

#     def __sub__(self, vector):
#         new_x = self.coordinates.x - vector.coordinates.x
#         new_y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(new_x, new_y))

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"


# # --- 11.8 ---

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x, y))

#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(x, y))

#     def __mul__(self, vector):
#         x = self.coordinates.x * vector.coordinates.x
#         y = self.coordinates.y * vector.coordinates.y
#         return x + y

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"


# # --- 11.9 ---


# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x, y))

#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(x, y))

#     def __mul__(self, vector):
#         return (
#                 self.coordinates.x * vector.coordinates.x
#                 + self.coordinates.y * vector.coordinates.y
#         )

#     def len(self):
#         return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"


# # --- 11.10 ---


# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x, y))

#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(x, y))

#     def __mul__(self, vector):
#         return (
#                 self.coordinates.x * vector.coordinates.x
#                 + self.coordinates.y * vector.coordinates.y
#         )

#     def len(self):
#         return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"

#     def __eq__(self, vector):
#         return self.len() == vector.len()

#     def __ne__(self, vector):
#         return self.len() != vector.len()

#     def __lt__(self, vector):
#         return self.len() < vector.len()

#     def __gt__(self, vector):
#         return self.len() > vector.len()
    
#     def __le__(self, vector):
#         return self.len() <= vector.len()
    
#     def __ge__(self, vector):
        return self.len() >= vector.len()