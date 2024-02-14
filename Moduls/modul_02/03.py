
start = 10

while start <= 20:
    print(start)
    start += 1



# число яке одночасно ділиться на дво числа

first = int(input("First"))
second = int(input("Second"))

gcd = min(first, second)

while not (first % gcd == 0) and (second % gcd == 0):
    gcd = gcd - 1
print(gcd)