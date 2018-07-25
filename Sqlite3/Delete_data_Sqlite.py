import os  
from sqlite3 import Error 
import sqlite3

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'db.sqlite3')

def db_connect(db_path=DEFAULT_PATH):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
 

        sql = """
        UPDATE albums 
        SET artist = 'John Doe' 
        WHERE artist = 'Andy Hunter'
         """
        cursor.execute(sql)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        conn.close()
   
 
if __name__ == '__main__':
    
    db_connect()
