#!/usr/bin/python
# -*- coding: utf-8-*-
import sqlite3
from sqlite3 import Error



def delete():


        answer='Y'
        while answer=='Y':
            try:

                conn = sqlite3.connect("/home/kokkinef/Desktop/python/mydatabase2.db")
                print("Connection!!!")
                cursor = conn.cursor()
                username = raw_input("Give the username you want to delete:  ")

                find_user  = """SELECT * FROM NAMES WHERE usrn = ? """

                cursor.execute(find_user, [(username)])

                if cursor.fetchall():

                    delete__user = """DELETE FROM NAMES  WHERE usrn = ? """

                    cursor.execute(delete__user, [(username)])

                    conn.commit()

                    print ('You have succefully delete username:',username)
                    answer = raw_input("Do you want to delete an other user (Y/N):  ")
                else:
                    answer = raw_input("Failed the user not exist, do you want to try again (Y/N):  ")


            except Error as e:
                print("Connection error")
                print(e)
            finally:
                conn.close()




if __name__ == '__main__':
    
    delete()
