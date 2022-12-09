from faker import Faker
from src.infra.config import DBConectionHandler
from .user_repository import UserRepository

faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConectionHandler()


def test_insert_user():
    """_Shoul insert User_"""

    name = faker.name()
    password = faker.word()
    engine = db_connection_handler.get_engine()

    # SQL commands
    new_user = user_repository.insert_user(name, password)
    query_user = engine.execute(
        "SELECT * FROM users WHERE id ='{}';".format(new_user.id)
    ).fetchone()
    print(new_user)
    print(query_user)

    engine.execute("DELETE FROM users WHERE id ='{}';".format(new_user.id))

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password