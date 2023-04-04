import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import fitz

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        # Initialize variables
        self.pdf_file = None
        self.pdf_images = []
        self.current_page = 0
        self.total_pages = 0

    def create_widgets(self):
        self.choose_file_button = tk.Button(self, text="Choose PDF File", command=self.choose_pdf_file)
        self.choose_file_button.pack()

        self.preview_label = tk.Label(self)
        self.preview_label.pack()

        self.previous_button = tk.Button(self, text="Previous Page", command=self.previous_page, state=tk.DISABLED)
        self.previous_button.pack(side="left")

        self.next_button = tk.Button(self, text="Next Page", command=self.next_page, state=tk.DISABLED)
        self.next_button.pack(side="right")

    def choose_pdf_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.pdf_file = file_path
            self.pdf_images = self.get_pdf_images(self.pdf_file)
            self.total_pages = len(self.pdf_images)
            self.current_page = 0
            self.show_page()

    def get_pdf_images(self, file_path):
        pdf_images = []
        pdf_doc = fitz.open(file_path)
        for i in range(pdf_doc.page_count):
            pdf_page = pdf_doc.load_page(i)
            pix = pdf_page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            pdf_images.append(img)
        return pdf_images

    def show_page(self):
        if self.pdf_images:
            img = self.pdf_images[self.current_page].resize((500, 700))
            photo = ImageTk.PhotoImage(img)
            self.preview_label.configure(image=photo)
            self.preview_label.image = photo
            self.update_buttons()

    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.show_page()

    def next_page(self):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.show_page()

    def update_buttons(self):
        if self.current_page == 0:
            self.previous_button.configure(state=tk.DISABLED)
        else:
            self.previous_button.configure(state=tk.NORMAL)

        if self.current_page == self.total_pages - 1:
            self.next_button.configure(state=tk.DISABLED)
        else:
            self.next_button.configure(state=tk.NORMAL)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
