def add_recurce(max_num):
    print(max_num)
    if max_num <= 0:
        return 0

    if max_num == 1:
        return 1
    
    return max_num + add_recurce(max_num - 1)

print(add_recurce(10))

def fibanace(n):
    if (n <= 1):
        return 1
    else:
        return fibanace(n-1) + fibanace(n-2)