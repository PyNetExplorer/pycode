#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import paramiko
import subprocess
import os
import time
import getpass

# Define SSH parameters for setting up web server via Paramiko
hostname = '192.168.0.17'  # Remote server IP address
port = 22
username = 'katya'
private_key_path = '/home/ekaterina/.ssh/id_rsa'
output_file = "/home/ekaterina/ansible_quickstart/output_file.txt"
your_sudo_password = getpass.getpass(prompt="Enter your sudo password: ")

# Define SSH client for Paramiko
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname, port, username, key_filename=private_key_path)

# Define parameters for SFTP to transfer index.html file to remote server for Website setup
sftp = ssh_client.open_sftp()

# Define commands to execute on the remote host to set up web server
commands = [
    f'echo "{your_sudo_password}" | sudo -S apt install -y apache2',  # Install Apache
    f'echo "{your_sudo_password}" | sudo -S ufw allow Apache',  # Allow Apache through the firewall
    f'echo "{your_sudo_password}" | sudo -S systemctl start apache2',  # Start Apache
    f'echo "{your_sudo_password}" | sudo -S systemctl enable apache2'  # Enable Apache to start on boot
]

# Define paths and options for ansible playbook
private_data_dir = '/home/ekaterina/ansible_quickstart'
inventory_path = '/home/ekaterina/ansible_quickstart/inventory.ini'
playbook = 'upgrades.yaml'

# Function to show popup message
def show_popup():
    result = messagebox.askyesno("Task Completed", "Would you like to perform a different setup?")
    if result:
        # Perform another setup or take appropriate action
        pass
    else:
        # Quit the application
        close_connections()

# Function to execute basic configuration
def basic_config():
    os.chdir(private_data_dir)
    subprocess.run(["ansible-playbook", "-i", inventory_path, playbook, "--vault-id=/home/ekaterina/ansible_quickstart/pass_id.txt"])
    messagebox.showinfo("Basic Configuration", "Basic configuration was applied to all servers!")
    show_popup()

# Function to execute web server setup
def web_server_setup():
    # Define parameters for progress bar
    progress_window = tk.Toplevel()
    progress_window.title("Web Server Setup")
    
    progress_var = tk.DoubleVar()
    progress_bar = tk.ttk.Progressbar(progress_window, variable=progress_var, maximum=100)
    progress_bar.pack(padx=10, pady=10)
    
    progress_label = tk.Label(progress_window, text="Web Server Setup in Progress...")
    progress_label.pack(padx=10, pady=(0, 5))
    
    estimated_time_label = tk.Label(progress_window, text="Estimated time: ~2-4 minutes")
    estimated_time_label.pack(padx=10, pady=(0, 10))
    
    progress_window.geometry("400x200")

    for i, command in enumerate(commands):
        stdin, stdout, stderr = ssh_client.exec_command(command)
        stdout.channel.recv_exit_status()  # Wait for command to finish
        progress_var.set((i + 1) * 25)  # Update progress bar
        progress_window.update_idletasks()  # Update GUI
    
    messagebox.showinfo("Web Server Setup Complete", "Web Server setup completed successfully!")
    progress_window.destroy()
    show_popup()    

# Function to execute website setup
def website_setup():
    for x in os.listdir("/home/ekaterina/ansible_quickstart/web_files/"):
        if not os.path.isdir("/home/ekaterina/ansible_quickstart/web_files/"+x):
            sftp.put("/home/ekaterina/ansible_quickstart/web_files/"+x, "/var/www/html/"+x)
    #output_label.config(text="Website is up and running")
    time.sleep(2)
    messagebox.showinfo("Website status", "Website setup is complete!")
    show_popup()

# Close SSH and SFTP connections
def close_connections():
    ssh_client.close()
    sftp.close()
    window.quit()

# Create the main window
window = tk.Tk()

# Set the title of the window
window.title("Linux Configuration App")

# Set the dimensions of the window (width x height)
window.geometry("600x400")

# Set background color to dark purple
window.configure(bg="#4D1354")

# Create a label for the welcome message
welcome_label = tk.Label(window, text="Welcome to LinuxEZConfig!", font=("Arial", 20), bg="#4D1354", fg="white")
welcome_label.pack(pady=20)

# Create buttons
basic_config_button = tk.Button(window, text="Basic Config", bg="#75507B", fg="white", command=basic_config)
basic_config_button.pack(pady=10)

web_server_setup_button = tk.Button(window, text="Web Server Setup", bg="#75507B", fg="white", command=web_server_setup)
web_server_setup_button.pack(pady=10)

website_setup_button = tk.Button(window, text="Website Setup", bg="#75507B", fg="white", command=website_setup)
website_setup_button.pack(pady=10)

exit_button = tk.Button(window, text="Exit", bg="#75507B", fg="white", command=close_connections)
exit_button.pack(pady=10)

# Create a label for the output
output_label = tk.Label(window, text="", font=("Arial", 16), fg="white", bg="#4D1354")
output_label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
window.quit()
