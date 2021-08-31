from faker import Faker

from src.infra.config import DBConnectionHandler
from .user_repository import UserRepository


faker = Faker()
user_repository = UserRepository()
db_connection = DBConnectionHandler()


def test_insert_user():
    """insert one user on database"""

    name = faker.name()
    password = faker.word()

    new_user = user_repository.inserted_user(user_name=name, password=password)

    engine = db_connection.get_engine()
    query_user = engine.execute(
        "SELECT * FROM users WHERE id='{}';".format(new_user.id)
    ).fetchone()

    engine.execute("DELETE FROM users WHERE id='{}'".format(new_user.id))

    assert new_user.id == query_user.id
    assert new_user.user_name == query_user.user_name
    assert new_user.password == query_user.password
