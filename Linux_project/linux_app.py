#!/usr/bin/python3
"""Ekaterina Williams | Author
*******************************************
This is quick linux configuration app for basic configuration via Ansible, setting up web server and website via Paramiko""" 

import paramiko
import subprocess
import os
from tqdm import tqdm as tdq
import time
import getpass

# Define SSH parameters for web server
hostname = '192.168.0.17' # Remote server IP address
port = 22
username = 'katya'
private_key_path = '/home/ekaterina/.ssh/id_rsa'
output_file = "/home/ekaterina/ansible_quickstart/output_file.txt"

your_sudo_password = getpass.getpass(prompt="Enter your sudo password: ")

# Define SSH parameters for Paramiko
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname, port, username, key_filename=private_key_path)

# Define parameters for SFTP to transfer index.html file to remote server
sftp = ssh_client.open_sftp()

# Define parameters for SFTP to transfer index.html file to remote server
#t = paramiko.Transport((hostname, port))
#t.connect(username=username, key_filename=private_key_path) #password=your_sudo_password)
#sftp = paramiko.SFTPClient.from_transport(t)


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

# Define menu options
option_1 = "1. Basic Config"
option_2 = "2. Web Server"
option_3 = "3. Website Setup"
option_4 = "4. Quit."

title = "Quick Linux Configuration"
lines = "*"*33

# Function to display menu
def show_menu():
    print(lines)
    print(title)
    print(lines)
    print(option_1)
    print(option_2)
    print(option_3)
    print(option_4)
    print(lines)

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)    

# Main function
def main():
    time.sleep(1)
    choice = ' '
    while choice != '4':
        show_menu() # Print out manu options
        choice = input('Please make a selection. > ')
        time.sleep(1)

        if choice == '1':
            time.sleep(1)
            os.chdir(private_data_dir)
            # Run ansible-playbook command
            subprocess.run(["ansible-playbook", "-i", inventory_path, playbook, "--vault-id=/home/ekaterina/ansible_quickstart/pass_id.txt"])
            slow_print("Basic configuration is applied to all servers\n")
            time.sleep(2)

        elif choice == '2':
            print()
            slow_print("Installation in progress..... Wait time ~2-3min\n")
            print(lines)
            time.sleep(1)
            # Execute commands on the remote server via paramiko
            for command in tdq(commands, desc="Progress"):
                stdin, stdout, stderr = ssh_client.exec_command(command)
                cmd_output = stdout.read()


             # Write command output to file
            with open(output_file, "w+") as file:
                file.write(str(cmd_output))
          
            print(lines)
            slow_print("Web server is ready for website setup.\n") 
            print()
            time.sleep(2)
        
        elif choice == '3':
            # iterate across the files within directory
            for x in os.listdir("/home/ekaterina/ansible_quickstart/web_files/"): # iterate on directory contents
                if not os.path.isdir("/home/ekaterina/ansible_quickstart/web_files/"+x): # filter everything that is NOT a directory
                    sftp.put("/home/ekaterina/ansible_quickstart/web_files/"+x, "/var/www/html/"+x) # sftp.put("from_path_local", "to_path_remote") - move file to target location

            time.sleep(1)
            print()
            slow_print("""File transfer - SUCCESS
*************************
Website is up and running\n""")# transfer index.html and image to remote server    
            print()
            time.sleep(2)

        elif choice == '4':
            slow_print("You are exiting this program\n")
            break

        else:
            slow_print("Error, not a valid choice\n")

        repeat = input("Do you want to make another configuration? (yes/no): ")
        if repeat.lower() != 'yes':
            slow_print('Have a nice day!\n')
            break

# Close the SSH connection
    ssh_client.close()
 # Close the SFTP connection
    sftp.close()
    #t.close()

if __name__ == "__main__":
    main()
