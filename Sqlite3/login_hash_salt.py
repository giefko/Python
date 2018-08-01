#!/usr/bin/python
# -*- coding: utf-8-*-
import sqlite3
import uuid
import hashlib



def login():


        answer='Y'
        while answer=='Y':
            try:

                conn = sqlite3.connect("/path/mydatabase2.db")
                print("Connection!!!")
                cursor = conn.cursor()
                username = raw_input("Give you username ")
                passwd = raw_input("Give you password ")




                find_user = ("SELECT pwd FROM NAMES WHERE usrn = ? ")

                cursor.execute(find_user,[(username)])

                rows = cursor.fetchall()


                for row in rows:
                    for i in row:
                        k=check_password(i, passwd )
                        if k==True:

                            print ('You are in')
                            answer='N'
                        else:
                            answer = raw_input("Failed Do you want to try again (Y/N):  ")
                        break
                    break



            except Error as e:
                print("Connection error")
                print(e)
            finally:
                conn.close()




def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha512(salt.encode() + user_password.encode()).hexdigest()



if __name__ == '__main__':

    login()
