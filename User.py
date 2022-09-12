class User:
    def __init__(self, userId, userName, password):
        self._userId = userId
        self._userName = userName
        self._password = password

    @property
    def userId(self):
        return self._userId

    @userId.setter
    def userId(self, userId):
        self._userId = userId

    @property
    def userName(self):
        return self._userName

    @userName.setter
    def userName(self, userName):
        self._userName = userName

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def __str__(self):
        return f"User: User ID: {self._userId}, User name: {self._userName}, password: {self._password}"