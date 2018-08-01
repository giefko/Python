#!/usr/bin/python
# -*- coding: utf-8-*-
import sqlite3
import uuid
import hashlib
from sqlite3 import Error
import unicodedata


def resetpass():


    answer = 'Y'
    while answer=='Y':


        try:
            conn = sqlite3.connect("/path/mydatabase2.db")
            print("Connection!!!")
            cursor = conn.cursor()
            new_uname = raw_input("Please enter the username to reset the pass:  ")

            checkifuser_exist = '''SELECT  usrn FROM NAMES WHERE usrn = ?'''
            cursor.execute(checkifuser_exist, [ (new_uname)])

            if cursor.fetchall():
                print ("Username Exist ")
                new_pass = raw_input("Please enter your new password:  ")
                hashed_password = hash_password(new_pass)
                insertDataPass = '''UPDATE NAMES SET pwd = ? WHERE usrn = ?'''

                cursor.execute(insertDataPass, [(hashed_password), (new_uname)])
                conn.commit()
                answer='N'
            else:
                print ("Username not exist")
                answer = raw_input("Do you want to search again (Y/N): ")


        except Error as e:
            print("Connection error")
            print(e)
        finally:
            conn.close()


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha512(salt.encode() + user_password.encode()).hexdigest()


if __name__ == '__main__':
    resetpass()
