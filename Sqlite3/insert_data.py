import os  
from sqlite3 import Error 
import sqlite3

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'db.sqlite3')

def db_connect(db_path=DEFAULT_PATH):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
 

        # insert some data
        cursor.execute("INSERT INTO albums VALUES ('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3')")
 
        # save data to database
        conn.commit()
 
        # insert multiple records using the more secure "?" method
        albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
                  ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
                  ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
                  ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
        cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
conn.commit()
    except Error as e:
        print(e)
    finally:
        conn.close()
   
 
if __name__ == '__main__':
    
    db_connect()
