from faker import Faker

fake = Faker()

def get_mocket_user():
    return {
        "name": fake.name(),
        "last_name": fake.last_name(),
        "email": fake.email()
    }

if __name__ == "main":
    user = get_mocket_user()
    print(user)
