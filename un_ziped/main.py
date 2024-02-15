from mock import get_mocket_user
from pprint import pprint
import json


amount = int(input("How many users? >>> "))

users = list()

for _ in range(amount):
    users.append(get_mocket_user())

with open("users.json", "w") as f:
    text = json.dumps(users)
    f.writelines(text)