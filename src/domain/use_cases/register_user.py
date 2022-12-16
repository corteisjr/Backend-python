from abc import ABC, abstractmethod
from src.domain.models import Users
from typing import Dict


class RegisterUser(ABC):
    """Interface  to register use case"""

    @abstractmethod
    def register(cls, name: str, password: str) -> Dict[bool, Users]:
        """Case

        Args:
            name (str): _description_
            password (str): _description_

        Returns:
            Dict[bool, Users]: _description_
        """
        raise Exception("Should implemet method: register")
