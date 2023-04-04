import tkinter as tk
import subprocess

class ImportDatabaseGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Database name
        self.db_name_label = tk.Label(self, text="Database name:")
        self.db_name_label.grid(row=0, column=0)
        self.db_name_entry = tk.Entry(self)
        self.db_name_entry.grid(row=0, column=1)

        # Database user
        self.db_user_label = tk.Label(self, text="Database user:")
        self.db_user_label.grid(row=1, column=0)
        self.db_user_entry = tk.Entry(self)
        self.db_user_entry.grid(row=1, column=1)

        # Database password
        self.db_password_label = tk.Label(self, text="Database password:")
        self.db_password_label.grid(row=2, column=0)
        self.db_password_entry = tk.Entry(self, show="*")
        self.db_password_entry.grid(row=2, column=1)

        # Database host
        self.db_host_label = tk.Label(self, text="Database host:")
        self.db_host_label.grid(row=3, column=0)
        self.db_host_entry = tk.Entry(self)
        self.db_host_entry.grid(row=3, column=1)

        # Database port
        self.db_port_label = tk.Label(self, text="Database port:")
        self.db_port_label.grid(row=4, column=0)
        self.db_port_entry = tk.Entry(self)
        self.db_port_entry.grid(row=4, column=1)

        # Backup file name
        self.backup_file_label = tk.Label(self, text="Backup file name:")
        self.backup_file_label.grid(row=5, column=0)
        self.backup_file_entry = tk.Entry(self)
        self.backup_file_entry.grid(row=5, column=1)

        # Import button
        self.import_button = tk.Button(self, text="Import", command=self.import_database)
        self.import_button.grid(row=6, column=1)

    def import_database(self):
        # Get values from the entry widgets
        db_name = self.db_name_entry.get()
        db_user = self.db_user_entry.get()
        db_password = self.db_password_entry.get()
        db_host = self.db_host_entry.get()
        db_port = self.db_port_entry.get()
        backup_file = self.backup_file_entry.get()

        # Construct the pg_restore command as a list of arguments
        cmd = ['pg_restore', '-h', db_host, '-p', db_port, '-U', db_user, '-d', db_name, backup_file]

        # Set the PGPASSWORD environment variable to the database password
        env = {'PGPASSWORD': db_password}

        # Execute the pg_restore command
        subprocess.run(cmd, env=env)

# Create the main window and run the GUI
root = tk.Tk()
app = ImportDatabaseGUI(master=root)
app.mainloop()
