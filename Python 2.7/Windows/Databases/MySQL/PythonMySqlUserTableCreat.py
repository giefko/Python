import MySQLdb

db=MySQLdb.connect(host="localhost",use_unicode="True",charset="utf8",user="",passwd="",db="new")


cursor=db.cursor()

cursor.execute("DROP TABLE IF EXISTS user")

sql="""CREATE TABLE user (
       id SMALLINT(5) UNSIGNED DEFAULT '0' ,
       username CHAR(10),
       password CHAR(16) BINARY,
       PRIMARY KEY MUL(id))"""



cursor.execute(sql)

db.close
