import sqlite3 as sql


class Database:
    def __init__(self):
        self.sql = sql
        self.table = "fingerprint"
        self.path = "schuelerdatenbank.db"

    def open_connection(self):
        try:
            con = sql.connect(self.path)
            return con
        except self.sql.Error as e:
            print(e)

    def close_connection(self, con):
        assert isinstance(con, self.sql.Connection)
        try:
            con.close()
        except self.sql.Error as e:
            print(e)

    def initialise_table(self):
        try:
            con = self.open_connection()
            cursor = con.cursor()
            try:
                cursor.execute("DROP TABLE {0}".format(self.table))
            except self.sql.Error as e:
                print(e)
            cursor.execute("""CREATE TABLE {0}(id_nr INTEGER PRIMARY KEY AUTOINCREMENT,
                              username VARCHAR(255), berechtigungsstufe INTEGER)""".format(self.table))
            con.commit()
            self.close_connection(con)
        except self.sql.Error as e:
            print(e)
            try:
                self.close_connection(con)
            except self.sql.Error as e:
                print(e)

    def insert(self, username, berechtigungsstufe):
        try:
            assert isinstance(username, str)
            assert isinstance(berechtigungsstufe, int)
            con = self.open_connection()
            cursor = con.cursor()
            cursor.execute("""INSERT INTO fingerprint(username, berechtigungsstufe) VALUES (?, ?)""",
                           (username, berechtigungsstufe))
            con.commit()
            self.close_connection(con)
        except self.sql.Error as e:
            print(e)
            try:
                self.close_connection(con)
            except self.sql.Error as e:
                print(e)

if __name__ == "__main__":
    Database()
    Database().initialise_table()
    Database().insert("Galinski", 2)