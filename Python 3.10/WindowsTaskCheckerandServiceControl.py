import os
import subprocess
import getpass
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

def check_task_running(task_name):
    task_list = subprocess.check_output(['tasklist']).decode('utf-8').split('\n')
    for task in task_list:
        if task_name.lower() in task.lower():
            return True
    return False

def get_task_username(task_name):
    task_list = subprocess.check_output(['tasklist', '/v', '/fi', f'imagename eq {task_name}']).decode('utf-8').split('\n')
    for task in task_list:
        if task_name.lower() in task.lower():
            return task.split()[1]
    return None

def start_service(service_name):
    current_username = getpass.getuser()
    service_username = get_service_username(service_name)

    if service_username and service_username == current_username:
        subprocess.run(['sc', 'start', service_name])
        return True
    else:
        return False

def stop_service(service_name):
    current_username = getpass.getuser()
    service_username = get_service_username(service_name)

    if service_username and service_username == current_username:
        subprocess.run(['sc', 'stop', service_name])
        return True
    else:
        return False

def get_service_username(service_name):
    result = subprocess.run(['sc', 'qc', service_name], capture_output=True, text=True)
    output_lines = result.stdout.split('\n')
    for line in output_lines:
        if line.strip().startswith('SERVICE_START_NAME'):
            return line.split(':')[1].strip()
    return None

def save_logs(log_message):
    folder_path = r'C:\Logs'  # Replace with your desired folder path
    file_path = os.path.join(folder_path, 'task_logs.txt')

    os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist

    with open(file_path, 'a') as file:
        file.write(log_message + '\n')

def check_task_status():
    task_name = 'notepad.exe'

    log_text.delete(1.0, tk.END)  # Clear log window

    if check_task_running(task_name):
        username = get_task_username(task_name)
        if username:
            log_message = f"The task '{task_name}' is running. User: {username}"
            log_text.insert(tk.END, log_message + '\n')
        else:
            log_message = f"The task '{task_name}' is running."
            log_text.insert(tk.END, log_message + '\n')
    else:
        log_message = f"The task '{task_name}' is not running."
        log_text.insert(tk.END, log_message + '\n')

    save_logs(log_message)

def start_service_click():
    service_name = 'wuauserv'

    log_text.delete(1.0, tk.END)  # Clear log window

    if start_service(service_name):
        log_message = f"The service '{service_name}' has been started."
        log_text.insert(tk.END, log_message + '\n')
        save_logs(log_message)
    else:
        log_message = f"Failed to start the service '{service_name}' due to different username."
        log_text.insert(tk.END, log_message + '\n')
        save_logs(log_message)

def stop_service_click():
    service_name = 'wuauserv'

    log_text.delete(1.0, tk.END)  # Clear log window

    if stop_service(service_name):
        log_message = f"The service '{service_name}' has been stopped."
        log_text.insert(tk.END, log_message + '\n')
        save_logs(log_message)
    else:
        log_message = f"Failed to stop the service '{service_name}' due to different username."
        log_text.insert(tk.END, log_message + '\n')
        save_logs(log_message)

# Create the main window
window = tk.Tk()
window.title("Task Status Checker")

# Create a log window
log_text = ScrolledText(window, width=50, height=10)
log_text.pack()

# Create a button to check the task status
check_button = tk.Button(window, text="Check Task Status", command=check_task_status)
check_button.pack(pady=5)

# Create a button to start the service
start_service_button = tk.Button(window, text="Start Service", command=start_service_click)
start_service_button.pack(pady=5)

# Create a button to stop the service
stop_service_button = tk.Button(window, text="Stop Service", command=stop_service_click)
stop_service_button.pack(pady=5)

# Run the main event loop
window.mainloop()
