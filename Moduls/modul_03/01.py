# print number of even squares from start to end

# start = 0, end = 10,    0, 2, 4,  

for i in range(0, 11):
    if i % 2 == 0:
        print(f"{i} : {i**2}")


def show_even_squares(start, end, step=1):
    for i in range(start, end + 1, step):
        if i % 2 == 0:
            print(f"{i} : {i**2}")


show_even_squares(0, 10, 4)
show_even_squares(2, 7)