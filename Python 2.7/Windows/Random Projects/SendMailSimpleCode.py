import smtplib  
  
fromaddr = 'your email address'  
toaddrs  = '<email address you want to send mail'
msg = 'Yes man!'  
   
# Credentials (if needed)
username = 'yourusername'  
password = '<yourpassword>'  
  
 # The actual mail send  
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(username,password)  
server.sendmail(fromaddr, toaddrs, msg)  
server.quit()  
