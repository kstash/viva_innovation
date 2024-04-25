import re


def validate_password(v):
    if not v:
        raise ValueError("Password cannot be empty")
    if not re.search(r"[a-z]", v):
        raise ValueError("Password must contain at least one lowercase letter")
    if not re.search(r"[A-Z]", v):
        raise ValueError("Password must contain at least one uppercase letter")
    if not re.search(r"[0-9]", v):
        raise ValueError("Password must contain at least one digit")
    if not re.search(r"[!@#$%^&*]", v):
        raise ValueError("Password must contain at least one special character")
    return v