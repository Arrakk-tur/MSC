import math


a = float(input("Side a >>> "))
b = float(input("Side b >>> "))
c = float(input("Side c >>> "))

P = a + b + c
p = P / 2

S = math.sqrt(p * (p-a)*(p-b)*(p-c))

message = f"The square is {S}"

print(message)
