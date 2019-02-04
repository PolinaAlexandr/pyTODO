import sqlite3


class DBManager():

    def __init__(self, db_path):
        self.db_path = db_path

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)

        self.cursor = self.connection.cursor()

        return self
    
    def __exit__(self, exc_type, exc_value, tb):
        if self.cursor:
            self.cursor.close()
        
        if self.connection:
            self.connection.commit()
            
            self.connection.close()
        
        return True
