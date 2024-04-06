import numpy as np

# # a = np.array([[1, 2, 3, 4, 5]])
# # b = np.array([[1/2, 1, 2, 3, 4]])
#
# # sum = a + np.transpose(b)
# # print(sum)
#
# # mult = np.dot(a, np.transpose(b))
# # print(mult)
#
# # ad = a / np.transpose(b)
# # print(ad)
#
# x = np.array([2, 1])
#
# m1 = np.array([[2, 0],
#                [0, 3]])
#
# m2 = np.eye(2, dtype=int)
#
# rad = np.radians(60)
#
# m4 = np.array([[np.cos(rad), -np.sin(rad)],
#                 [np.sin(rad), np.cos(rad)]])
#
# rad_5 = np.radians(30)
#
# m5 = np.array([[np.cos(rad_5), -np.sin(rad_5)],
#                 [np.sin(rad_5), np.cos(rad_5)]])
# # t2 = np.eye(2, dtype=int)
# # print(t2)
#
# # combined_transformation = np.dot(transformation_5, np.dot(transformation_4, np.dot(transformation_3, transformation_1)))
#
#
# m6 = np.dot(m5, np.dot(m4, np.dot(m2, m1)))
#
# m6_x = np.dot(m6, x)
# print(m6_x)


#
# A = np.array([
#     [-1, 1, 2],
#     [0, -1, -3],
#     [4, -3, 2]
# ])
# B = np.array([1, -4, 7])
#
#
# def solve_cramer(a, b, verbose=False):
#     n = len(a)
#     solutions = []
#
#     # Знаходимо детермінант матриці A
#     det_a = np.linalg.det(a)
#
#     # Для кожного стовпця матриці A
#     for i in range(n):
#         # Копіюємо матрицю A
#         a_copy = a.copy()
#         # Замінюємо i-тий стовпець матриці A на вектор b
#         a_copy[:, i] = b
#         # Знаходимо детермінант отриманої матриці
#         det_a_i = np.linalg.det(a_copy)
#         # Знаходимо розв'язок рівняння xi = det(Ai) / det(A), де Ai - це матриця A замінена i-тим стовпцем на вектор b
#         xi = det_a_i / det_a
#         solutions.append(xi)
#
#     if verbose:
#         print("Розв'язки системи рівнянь:")
#         for i in range(n):
#             print(f"x_{i+1} =", solutions[i])
#
#     return solutions
#
#
# print(f"Вектор рішення: \r\n {solve_cramer(A, B, True)}")
