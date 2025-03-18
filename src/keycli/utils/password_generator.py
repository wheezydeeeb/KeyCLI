import numpy as np
import string

class PasswordGenerator:
    @staticmethod
    def generate_password(length: int) -> str:
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(np.random.choice(list(chars), length))
