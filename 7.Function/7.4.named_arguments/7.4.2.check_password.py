def check_password(password, chars='$%!?@#'):
    return len(password) > 7 and any(x in password for x in chars)
