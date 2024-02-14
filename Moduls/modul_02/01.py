

# age = int(input("how old you? "))

# if age > 18:
#     print("Here is your beer")
# elif age == 17:
#     print("Almost there.")
# elif age == 18:
#     print("Her is your first beer.")
# else:
#     print("You are a kid, go home!")


username = input('Enter username: ')
password = input('Enter password: ')


if "admin" in username:
    if password == "qwerty":
        print(f"Login succssful! Welcome {username}")
    elif password == "12345":
        print("Week password")
    else:
        print("Incorect password")
elif "guest" in username:
    if password == "guest123":
        print(f"Login succssful! Welcome {username}")
    else:
        print("Incorect password")
else:
    print("You not pass!")