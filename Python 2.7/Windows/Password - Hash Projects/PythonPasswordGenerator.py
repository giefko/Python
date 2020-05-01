#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import urandom
import lrange
charsets={

"0":"0123456789",\

}

def GeneratePassword(length=5,charset="aA0"):
	password="";lc="";charset_string=""
	for c in charset:
		if c in charsets.keys():
			charset_string+=charsets[c]
	while len(password)<length:
		c=urandom(1)
		if c in charset_string and c!=lc:
			password+=c;lc=c
	return password



        

if __name__=="__main__":
       
        s4=0
        for i in range(10):
                
                
                k=GeneratePassword(4,"aA0")
                k1=GeneratePassword(4,"aA0")
                k2=GeneratePassword(4,"aA0")
                k3=GeneratePassword(4,"aA0")
                k4=GeneratePassword(4,"aA0")
                
                
                print i,")",k,"|",k1,"|",k2,"|",k3,"|",k4,"\n"
                
