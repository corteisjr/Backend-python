from src.domain.models import Pets
from src.infra.config import DBConectionHandler
from src.infra.entities import Pets as PetsModel


class PetRepository:
    """Class to manage Pet repository"""

    @classmethod
    def insert_pet(cls, name: str, specie: str, age: int, user_id: int) -> Pets:
        """insert data in PetsEntitty

        Args:
            name (str): name of pet
            specie (str): specie of pet
            age (int): pet age
            user_id (int): id of owner (FK)

        Returns:
            Pets: tuple with new pet inserted
        """
        with DBConectionHandler() as db_connection:
            try:
                new_pet = PetsModel(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()

                return Pets(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie.value,
                    age=new_pet.age,
                    user_id=new_pet.user_id,
                )
            except:
                db_connection.session.rollback()
                raise
            return None
