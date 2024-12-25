import re
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    patterns = {
    "Afghanistan": r'^(\+93|0)?7\d{8}$',  # افغانستان
    "Iran": r'^(\+98|0)?9\d{9}$',         # ایران
    "USA": r'^(\+1|0)?\d{10}$',           # آمریکا
    "UAE": r'^(\+971|0)?5\d{8}$',         # امارات
    "Russia": r'^(\+7|8)?\d{10}$',        # روسیه
    }

    for country,pattern in patterns.items():
        if re.fullmatch(pattern,value):
            return 
        else:
            raise ValidationError("Your Phone number is not correct.")


def validate_password(value):
    if len(value)<8:
        raise ValidationError("the password must be 8 charecter.")
    if not any(chr.isupper() for chr in value):
        raise ValidationError("the password must be contain one uppercase letter.")
    if not any(chr.isdigit() for chr in value):
        raise ValidationError("the password must be contain one number")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]',value):
        raise ValidationError("the password must be contain on charecter")