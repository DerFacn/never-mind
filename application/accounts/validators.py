from django.core.exceptions import ValidationError
import re

def username_validator(username):
    pat = re.compile(r"[A-Za-z0-9]+")
    if re.fullmatch(pat, username):
        return username
    else:
        raise ValidationError("Invalid username!")

def email_validator(email):
    pat = re.compile(r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]')
    if re.fullmatch(pat, email):
        print(email)
    else:
        raise ValidationError("Invalid email!")
