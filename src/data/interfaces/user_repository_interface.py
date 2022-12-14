from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Users


class UserRepositoryInterface(ABC):
    """Interface to Pet Repository

    Args:
        ABC (_type_): _description_
    """

    @abstractmethod
    def insert_user(self, name: str, password: str) -> Users:
        """Abstract Method"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_user(self, user_id: int = None, name: str = None) -> List[Users]:
        """Abstract Method"""
        raise Exception("Method not implemented")
