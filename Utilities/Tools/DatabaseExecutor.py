import mysql.connector as mysql


######################################################################################################################
############################## Class DatabaseExecutor ################################################################
######################################################################################################################

class DatabaseExecutor:
    """
    Class DatabaseExecutor
    :description: This class is used to execute queries on a database.
    """
    name: str
    user: str
    password: str
    host: str
    port: int
    connection = None
    cursor = None

    def __init__(self, user: str, password: str, host: str, port: int, name: str = None) -> None:
        """
        Constructor for the class DatabaseExecutor
        :param user: The user name of the database
        :param password: The password of the database
        :param host: The host of the database
        :param port: The port of the database
        :param name: The name of the database
        """
        self.name: str = name
        self.user: str = user
        self.password: str = password
        self.host: str = host
        self.port: int = port
        self.connection = None
        self.cursor = None

        if self.name is not None:
            self.connectDB()
        else:
            self.connect()

    def connectDB(self) -> None:
        """
        Connect to a database
        :return: None
        """
        try:
            self.connection = mysql.connect(
                database=self.name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)
            exit()

    def connect(self) -> None:
        """
        Connect to a database without a database name
        :return: None
        """
        try:
            self.connection = mysql.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)
            exit()

    def execute(self, query, isSelect: bool = False) -> list:
        """
        Execute a query
        :param query: The query to execute
        :param isSelect: True if the query is a select query
        :return:
        """
        try:
            self.cursor.execute(query)
        except Exception as e:
            print(e)
            exit()
        else:
            if isSelect:
                return self.cursor.fetchall()
            else:
                self.connection.commit()

    def fetchone(self) -> list:
        """
        Fetch one row from the cursor
        :return:
        """
        return self.cursor.fetchone()

    def fetchall(self) -> list:
        """
        Fetch all the rows from the cursor
        :return:
        """
        return self.cursor.fetchall()

    def close(self):
        """
        Close the connection
        :return: None
        """
        self.cursor.close()
        self.connection.close()

    def select(self, table: str, select: list[str], where: str = None, limit: int = None, order: str = None,
               having: str = None) -> list:
        """
        Select a row from a table
        :param table: The table to select from
        :param select: The columns to select
        :param where: The where clause
        :param limit: The limit of the select
        :param order: The order of the select
        :param having: The having clause
        :return:
        """
        query = "SELECT "
        for i in select:
            query += i + ","
        query = query[:-1]
        query += " FROM " + table
        if where is not None:
            query += " WHERE " + where
        if order is not None:
            query += " ORDER BY " + order
        if having is not None:
            query += " HAVING " + having
        if limit is not None:
            query += " LIMIT " + str(limit)
        return self.execute(query=query, isSelect=True)

    def update(self, table: str, set: list[[str, str]], where: str = None) -> None:
        """
        Update a row in a table
        :param table: The table to update
        :param set: The set clause
        :param where: The where clause
        :return:
        """
        query = "UPDATE " + table + " SET "
        for i in set:
            query += i[0] + "=" + i[1] + ","
        query = query[:-1]
        if where is not None:
            query += " WHERE " + where
        self.execute(query=query)
