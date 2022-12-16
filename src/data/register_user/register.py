from typing import Type, Dict
from src.domain.use_cases import RegisterUser as RegisterUserInterface
from src.domain.models import Users
from src.data.interfaces import UserRepositoryInterface as UserRepository


class RegisterUser(RegisterUserInterface):
    """Class to define usercase register user

    Args:
        RegisterUserInterface (_type_): _description_
    """

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """Register user use case

        Args:
            name (str): _description_
            password (str): _description_

        Returns:
            Dict[bool, Users]: _description_
        """
        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)
        if validate_entry:
            response = self.user_repository.insert_user(name, password)

        return {"Success": validate_entry, "Data": response}
