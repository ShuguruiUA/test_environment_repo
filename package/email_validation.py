import re
from field import Field


class Email(Field):
    def __init__(self, value):
        if not self.is_valid_email(value):
            raise ValueError("Invalid email address")
        super().__init__(value)

    def is_valid_email(self, email):
        pattern = r'[a-zA-Z][a-zA-Z0-9._-]+@[a-zA-Z]+\.[a-zA-Z]{2,}'
        return re.match(pattern, email) is not None
