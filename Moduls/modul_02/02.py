a = [3, 2, 5, -4, 54]

max_elem = a[0]
min_elem = a[0]


for elem in a:
    if elem > max_elem:
        max_elem = elem
print(max_elem)



for elem in a:
    if elem < min_elem:
        min_elem = elem
print(min_elem)


a = "Hello world! What is the weather"
count_char_a = 0

for char in a:
    if char.lower() == "a":
        count_char_a +=1
print(count_char_a)