from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List

class BaseHandler(ABC):
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    @abstractmethod
    def load_data(self) -> List[Dict]:
        pass

    @abstractmethod
    def save_data(self, data: List[Dict]) -> None:
        pass
