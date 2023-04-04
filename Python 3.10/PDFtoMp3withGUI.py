import tkinter as tk
from tkinter import filedialog
import PyPDF3
import pyttsx3
import pdfplumber


class App:
    def __init__(self, master):
        self.master = master
        master.title("PDF to Audio Converter")

        # Create a frame
        self.frame = tk.Frame(master)
        self.frame.pack()

        # Create a label to display selected file name
        self.filename_label = tk.Label(self.frame, text="No file selected")
        self.filename_label.pack()

        # Create a button to open a file dialog and select a PDF file
        self.choose_file_button = tk.Button(self.frame, text="Choose PDF File", command=self.choose_file)
        self.choose_file_button.pack()

        # Create a label to display voice gender options
        self.gender_label = tk.Label(self.frame, text="Select voice gender:")
        self.gender_label.pack()

        # Initialize voice gender
        self.gender = tk.StringVar(value="male")

        # Create a radio button for male voice
        self.voice_male = tk.Radiobutton(self.frame, text="Male", variable=self.gender, value="male")
        self.voice_male.pack()

        # Create a radio button for female voice
        self.voice_female = tk.Radiobutton(self.frame, text="Female", variable=self.gender, value="female")
        self.voice_female.pack()

        # Create a label to display audio speed options
        self.speed_label = tk.Label(self.frame, text="Select audio speed:")
        self.speed_label.pack()

        # Create a scale for audio speed
        self.speed_scale = tk.Scale(self.frame, from_=100, to=150, orient=tk.HORIZONTAL, length=200)
        self.speed_scale.pack()

        # Create a button to convert PDF to audio
        self.convert_button = tk.Button(self.frame, text="Convert to Audio", command=self.convert)
        self.convert_button.pack()

    def choose_file(self):
        # Open a file dialog and get the path of the selected file
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

        # Display the selected file name on the label
        self.filename_label.config(text=file_path)

        # Save the file path as a class attribute
        self.file_path = file_path

    def convert(self):
        # Read the PDF file and get the number of pages
        with open(self.file_path, 'rb') as book:
            pdfReader = PyPDF3.PdfFileReader(book)
            pages = pdfReader.numPages

        # Initialize an empty string variable for the final text
        finalText = ""

        # Extract text from each page of the PDF file using pdfplumber
        with pdfplumber.open(self.file_path) as pdf:
            for i in range(0, pages):
                page = pdf.pages[i]
                text = page.extract_text()
                finalText += text

        # Initialize the pyttsx3 engine
        engine = pyttsx3.init()

        # Set the voice gender
        if self.gender.get() == "male":
            engine.setProperty('voice', 'english+m3')
        elif self.gender.get() == "female":
            engine.setProperty('voice', 'english+f3')

        # Set the audio speed
        engine.setProperty('rate', self.speed_scale.get())

        # Convert the final text to audio and save it to a file
        engine.save_to_file(finalText, 'output.mp3')
        engine.runAndWait()


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
