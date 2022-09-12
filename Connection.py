import sys
from psycopg2 import pool

class Connection:
    _DATABASE ="personas"
    _USERNAME = "postgres"
    _PASSWORD = "admin"
    _DB_PORT = "5432"
    _HOST = "127.0.0.1"
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def getPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                return cls._pool
            except Exception as ex:
                print(f"An exception occurred: {ex}")
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def getConnection(cls):
        connection = cls.getPool().getconn()
        return connection

    @classmethod
    def releaseConnection(cls, connection):
        cls.getPool().putconn(connection)

    @classmethod
    def closeConnections(cls):
        cls.getPool().closeall()

