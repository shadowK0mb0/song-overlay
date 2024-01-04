import base64
import hashlib
import secrets
import string


def generate_random_string(length) -> str:
    possible = string.ascii_letters + string.digits
    return "".join(secrets.choice(possible) for _ in range(length))


def sha256(plain) -> str:
    encoded = plain.encode("utf-8")
    return hashlib.sha256(encoded).digest()


def base64encode(input) -> str:
    return base64.urlsafe_b64encode(input).decode('ascii').rstrip("=")
