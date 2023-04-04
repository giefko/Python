import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Create a tkinter window
    root = tk.Tk()

    # Allow the user to select an Excel file
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if not file_path:
        return

    # Load the data from the Excel file into a Pandas DataFrame
    data = pd.read_excel(file_path)

    # Display a dialog box with a list of column names and allow the user to select the columns for the graph
    column_names = list(data.columns)
    selected_columns = []
    def ok_button_callback():
        nonlocal selected_columns
        selected_columns = [column_names[i] for i in listbox.curselection()]
        if len(selected_columns) < 2:
            messagebox.showerror("Error", "Please select at least two columns.")
        else:
            dialog.destroy()

    dialog = tk.Toplevel(root)
    dialog.title("Select Columns")
    dialog.transient(root)
    listbox = tk.Listbox(dialog, selectmode=tk.MULTIPLE)
    for column_name in column_names:
        listbox.insert(tk.END, column_name)
    listbox.pack(padx=10, pady=10)
    ok_button = tk.Button(dialog, text="OK", command=ok_button_callback)
    ok_button.pack(pady=10)

    # Make sure the root window is displayed after creating it
    root.deiconify()
    root.lift()

    dialog.wait_window()

    # Create a line plot of the selected columns
    plt.plot(data[selected_columns[0]], data[selected_columns[1]])
    plt.title("Data from Excel File")
    plt.xlabel(selected_columns[0])
    plt.ylabel(selected_columns[1])
    plt.show()

if __name__ == "__main__":
    main()
