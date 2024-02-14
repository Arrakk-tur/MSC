def add(a,b,c):
    return a+b+c

res = add(1,5,3)
print(res)

def add1(*args):
    for i in args:
        count += i

        return count   

def add2(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

res = add2(1,5, page=5, iruna="Stude")
print(res)

res = add2(1, 24, "hfsjdfhs", page=5, iruna="Stude")
print(res)