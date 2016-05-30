import string
import speech
import webbrowser

while True:
    print "Talk:"
    phrase = speech.input()
    speech.say("You said %s" % phrase)
    print "You said {0}".format(phrase)
    
  
    if phrase.lower() == "One": #it doesn't matter it's not case sensitive
        url="http://www.google.com"
        webbrowser.open_new(url)
