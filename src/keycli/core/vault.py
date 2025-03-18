from typing import List
from ..models.password_entry import PasswordEntry
from ..data_handlers.json_handler import JSONHandler

class Vault:
    def __init__(self, handler_type: str = 'json'):
        self.handler = self._get_handler(handler_type)
        self.entries = self._load_entries

    def _get_handler(self, handler_type: str):
        handlers = {
            'json': JSONHandler('vault.json')
        }
        return handlers[handler_type]
    
    def _load_entries(self) -> List[PasswordEntry]:
        return [PasswordEntry(**entry) for entry in self.handler.load_data()]
    
    def save_entries(self) -> None:
        data = [entry.to_dict() for entry in self.entries]
        self.handler.save_data(data)


        

