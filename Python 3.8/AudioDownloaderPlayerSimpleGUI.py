import urllib.request
from playsound import playsound
from tkinter import*
from pathlib import Path

url = input("Enter your url with the audio: ")
name = input("Enter the name of the audio with wav format: ")
urllib.request.urlretrieve(url, name)

root = Tk()
root.title('Python sound player')  # giving the title for our window
root.geometry("500x400")


# making function
def play():

    audio = Path().cwd() / name

    print (audio)
    playsound(str(audio))


# title on the screen you can modify it
title = Label(root, text="Music", bd=9, relief=GROOVE,
              font=("times new roman", 50, "bold"), bg="white", fg="green")
title.pack(side=TOP, fill=X)

# making a button which trigger the function so sound can be playeed
play_button = Button(root, text="Play Song", font=("Helvetica", 32),
                     relief=GROOVE, command=play)
play_button.pack(pady=20)

info = Label(root, text="Click on the button above to play song ",
             font=("times new roman", 10, "bold")).pack(pady=20)
root.mainloop()






