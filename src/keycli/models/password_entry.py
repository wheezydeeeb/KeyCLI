from dataclasses import dataclass
from typing import Any

@dataclass
class PasswordEntry:
    _service: str
    _username: str
    _encrypted_password: str
    metadata: dict = None

    @property
    def service(self) -> str:
        return self._service
    
    @property
    def username(self) -> str:
        return self._username
    
    @property
    def encrypted_password(self) -> str:
        return self._encrypted_password
    
    def to_dict(self) -> dict:
        return {
            "service": self.service,
            "username": self.username,
            "encrypted_password": self.encrypted_password,
            "metadata": self.metadata or {}
        }
