def is_valid_password(password):
    res = True
    set_pswd = set(password)
    if len(password) < 8:   # Довжина рядка пароля вісім символів.
        return False
    elif res:
        if ((str().islower() not in set_pswd)           # Містить хоча б одну літеру у верхньому регістрі.
                or (str().isupper() not in set_pswd)    # Містить хоча б одну літеру у нижньому регістрі.
                or (str().isdigit() not in set_pswd)):  # Містить хоча б одну цифру.
            res = False

    return res