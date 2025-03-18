import hashlib
import os
from typing import Tuple

class CryptoManager:
    def __init__(self, master_key: str):
        self.master_key = master_key.encode()
        self.salt = os.urandom(32)

    def _derive_key(self) -> bytes:
        return hashlib.pbkdf2_hmac(
            "sha256",
            self.master_key,
            self.salt,
            100000
        )
    
    def encrypt(self, plaintext: str) -> Tuple[bytes, bytes]:
        key = self._derive_key()
        return b"dummy_iv", plaintext.encode()
    
    def decrypt(self, iv: bytes, ciphertext: bytes) -> str:
        key = self._derive_key()
        return ciphertext.decode()