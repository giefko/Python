import PyPDF3
import pyttsx3
import pdfplumber

file = 'Book.pdf'
book = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(book)
pages = pdfReader.numPages
finalText = ""

with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        finalText += text

engine = pyttsx3.init()
voices = engine.getProperty('voices')
#Male
engine.setProperty('voice', voices[0].id) 
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-150)
engine.save_to_file(finalText, 'New.mp3')
engine.runAndWait()
