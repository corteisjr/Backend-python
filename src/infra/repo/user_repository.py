from typing import List
from src.domain.models import Users
from src.infra.config import DBConectionHandler
from src.infra.entities import Users as UsersModel


class UserRepository:
    """Class to manage user repository"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """Insert data in user entity
        :param - name: person name
               - password: user password
        :return - tuple with new user inserted
        """

        with DBConectionHandler() as db_connection:
            try:
                new_user = UsersModel(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
                return Users(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None

    @classmethod
    def select_user(cls, user_id: int = None, name: str = None) -> List[Users]:
        """Select data in user entitty by id and/or name

        Args:
            user_id (int, optional): _id of the register_. Defaults to None.
            name (str, optional): _users name_. Defaults to None.

        Returns:
            List[Users]: _Users selected_
        """

        try:
            query_data = None

            if user_id and not name:

                with DBConectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id)
                        .one()
                    )
                    query_data = [data]
            elif not user_id and name:
                with DBConectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]
            elif user_id and name:
                with DBConectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id, name=name)
                        .one()
                    )
                    query_data = [data]
            return query_data
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
        return None
