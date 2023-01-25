from django.core.exceptions import ValidationError
import re

def username_validator(username):
    pat = re.compile(r"[A-Za-z0-9]+")
    if re.fullmatch(pat, username):
        return username
    else:
        raise ValidationError("Invalid username!")

def email_validator(email):
    pat = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if re.fullmatch(pat, email):
        return email
    else:
        raise ValidationError("Invalid email!")
