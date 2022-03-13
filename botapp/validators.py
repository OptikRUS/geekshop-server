import re


def email_valid(email):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if re.match(pattern, email) is not None:
        return True
    return False


def password_valid(password):
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s).*$"
    # pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$"
    if re.match(pattern, password) is not None:
        return True
    return False


def login_valid(password):
    pattern = r"^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$"
    if re.match(pattern, password) is not None:
        return True
    return False
