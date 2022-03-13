import re


def email_valid(email):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if re.match(pattern, email) is not None:
        return True
    return False


def password_valid(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$"
    if re.match(pattern, password) is not None:
        return True
    return False


def login_valid(password):
    pattern = r"^([A-Za-z0-9])"
    if re.match(pattern, password) is not None:
        return True
    return False
