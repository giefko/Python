#!/usr/bin/python
# -*- coding: utf-8-*-

import commands, os, string,sys

print('-----Process name------')
print('|         firefox        |')
print('|         chrome         |')
print('--------------------------')



tmp = os.popen("ps -Af").read()

program = raw_input("Enter the name of the program to check: ")
output = commands.getoutput("ps -fA|grep " + program)
proginfo = string.split(output)
k = str(proginfo[1])



if k not in tmp[:]:
    print ('Process not running')
else:
    answer = raw_input("Are you sure that you want ot kill this process?(Y/N) ")
    if answer=='Y':
        print ("You are a 'Killer'" )
        os.system("kill "+k)
    else:
        sys.exit('Termination')

