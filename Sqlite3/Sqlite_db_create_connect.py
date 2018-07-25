import os  
from sqlite3 import Error 
import sqlite3

# create a default path to connect to and create (if necessary) a database
# called 'database.sqlite3' in the same directory as this script
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'db.sqlite3')

def db_connect(db_path=DEFAULT_PATH):
    try:
        conn = sqlite3.connect(db_path)
        print(sqlite3.version)
        print ('Works')
    except Error as e:
        print(e)
    finally:
        conn.close()
   
 
if __name__ == '__main__':
    
    db_connect()
