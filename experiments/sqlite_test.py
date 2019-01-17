import sqlite3

con = sqlite3.connect("testbase.bd")
cursor = con.cursor()


cursor.execute("""CREATE TABLE notes
                  (first_note text, second_note text) 
               """)


cursor.execute("""INSERT INTO notes
                  VALUE('TODO_1', 'TODO_2')"""
               )

con.commit()
