from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UserModel


User = namedtuple("User", ["id", "user_name", "email", "password", "active"])


class UserRepository:
    """Class to manage User Repository"""

    @classmethod
    def inserted_user(cls, user_name: str, password: str):
        """Insert data in user entity
        :params - name: person name
                - password: user password
        :return - tuple with new user inserted
        """

        with DBConnectionHandler() as connection:
            try:
                new_user = UserModel(user_name=user_name, password=password)
                connection.session.add(new_user)
                connection.session.commit()

                return User(
                    id=new_user.id,
                    user_name=new_user.user_name,
                    email=new_user.email,
                    password=new_user.password,
                    active=new_user.active,
                )
            except:
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

        return None
