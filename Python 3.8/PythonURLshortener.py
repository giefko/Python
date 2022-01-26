import pyshorteners as sh
import requests





link = input("Enter the url you want to short :")
s = sh.Shortener ()

print(s.tinyurl.short(link))
s2=s.tinyurl.short(link)



response = requests.get(s2)
if response.status_code == 400 or response.status_code == 300 or response.status_code == 200:
   print('The url works!!')
else:
   print('The url not working')
