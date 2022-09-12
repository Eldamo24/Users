from Connection import Connection

class Cursor:
    def __init__(self):
        self._cursor = None
        self._connection = None

    def __enter__(self):
        self._connection = Connection.getConnection()
        self._cursor = self._connection.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self._connection.rollback()
        else:
            self._connection.commit()
        self._cursor.close()
        Connection.releaseConnection(self._connection)