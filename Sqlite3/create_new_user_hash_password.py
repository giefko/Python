#!/usr/bin/python
# -*- coding: utf-8-*-
import sqlite3
import uuid
import hashlib
from sqlite3 import Error




def newUser():
   
    fname = raw_input("Please enter you First Name:  ")
    lname = raw_input("Please enter your Last Name ")
    found = 0
    while found == 0:
        new_uname = raw_input("Please enter your username:  ")




        try:
            conn = sqlite3.connect("/path/mydatabase2.db")
            print("Connection!!!")
            cursor = conn.cursor()

            findUser = ("SELECT * FROM NAMES WHERE usrn = ? ")
            cursor.execute(findUser ,[(new_uname)])


            if cursor.fetchall():
                print ("Username Taken ")
            else:
                found = 1
                new_pass = raw_input("Please enter your password:  ")
                hashed_password = hash_password(new_pass)
                insertDataPass = '''INSERT INTO NAMES(first_name,last_name,usrn,pwd) VALUES(?,?,?,?)'''
                cursor.execute(insertDataPass, [(fname), (lname),(new_uname),(hashed_password)])
                conn.commit()


        except Error as e:
            print("Connection error")
            print(e)
        finally:
            conn.close()


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ':' + salt






if __name__ == '__main__':
    newUser()
    
    

