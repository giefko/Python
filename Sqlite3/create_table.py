import sqlite3
 
conn = sqlite3.connect("/path/mydatabase2.db") 
 
cursor = conn.cursor()
 
# create a table
cursor.execute("""CREATE TABLE NAMES 
              (first_name text , last_name text ,
                   usrn text , pwd text PRIMARY KEY)""")

