from typing import Dict, List, Type
from src.domain.models.users import Users
from src.domain.use_cases import FindUser as FindUserInterface
from src.data.interfaces import UserRepositoryInterface as UserRepository


class FindUser(FindUserInterface):
    """Class to define use case Finde User"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Select User By Id

        Args:
            user_id (int): _description_

        Returns:
            Dict[bool, List[Users]]: Dictionary with information os the process
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id)
        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Select User By name

        Args:
            name (str): name of the user

        Returns:
            Dict[bool, List[Users]]: Dictionary with information os the process
        """
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.user_repository.select_user(name=name)
        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """Select User By id and name

        Args:
            user_id (int): Id of user
            name (str): name of the user
        Returns:
            Dict[bool, List[Users]]: Dictionary with information os the process
        """
        validate_entry = isinstance(name, str) and isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id, name=name)
        return {"Success": validate_entry, "Data": response}
