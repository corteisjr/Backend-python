from src.infra.config import DBConectionHandler
from src.infra.entities import Users


class FakerRepo:
    """A simple Repository"""

    @classmethod
    def insert_user(cls):
        """Doc"""

        with DBConectionHandler() as db_connection:
            try:
                new_user = Users(name="Corteis", password="Debug")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
