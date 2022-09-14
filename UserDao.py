from Cursor import Cursor
from User import User

class UserDao:
    _SELECT = "SELECT * FROM users"
    _DELETE = "DELETE FROM users WHERE id_user = %s"

    @classmethod
    def selectAll(cls):
        with Cursor() as cursor:
            cursor.execute(cls._SELECT)
            registers = cursor.fetchall()
            users = []
            for register in registers:
                users.append(User(register[0], register[1], register[2]))
            for user in users:
                print(user)

    @classmethod
    def deleteUser(cls, id_user):
        with Cursor() as cursor:
            id = (id_user, )
            cursor.execute(cls._DELETE, id)

UserDao.selectAll()