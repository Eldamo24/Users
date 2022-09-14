from Cursor import Cursor
from User import User

class UserDao:
    _SELECT = "SELECT * FROM users"
    _DELETE = "DELETE FROM users WHERE id_user = %s"
    _UPDATE = "UPDATE users set user_name = %s, password = %s WHERE id_user = %s"
    _INSERT = "INSERT INTO users (id_user, user_name, password) VALUES (%s, %s, %s)"

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

    @classmethod
    def updateUser(cls, user):
        with Cursor() as cursor:
            userData = (user.userName, user.password, user.userId)
            cursor.execute(cls._UPDATE, userData)

    @classmethod
    def insertUser(cls, user):
        with Cursor() as cursor:
            userData = (user.userId, user.userName, user.password)
            cursor.execute(cls._INSERT, userData)


