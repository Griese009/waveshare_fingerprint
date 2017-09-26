import tkinter as tk
import os
import sql
import app
import hex_try


class App:
    def __init__(self):
        self.sql = sql.Database()
        self.math = hex_try
        self.reader = app

    def check_db(self):
        try:
            path = os.listdir(".")
            if "schuelerdatenbank.db" in path:
                return True
            else:
                self.sql.initialise_table()
                return True
        except Exception as e:
            print(e)
            return False



if __name__ == "__main__":
    App()
    print(App().check_db())
