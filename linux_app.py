#!/usr/bin/python3

import paramiko
import getpass

option_1 = "1. Basic Configuration"
option_2 = "2. Web Server"
option_3 = "3. Mail Server"
option_4 = "4. Database Server"
option_5 = "5. Quit."

title = "Quick Linux Configuration"
lines = "*"*50

def show_menu():
    print(lines)
    print(title)
    print(lines)
    print(option_1)
    print(option_2)
    print(option_3)
    print(option_4)
    print(option_5)
    print(lines)

def sec_hardening():
    pass

def web_server():
    pass

def mail_server():
    pass

def database_server():
    pass

def main():
    choice = ' '
    while choice != 5:
        show_menu()
        choice = int(input('Please make a selection. > '))
        if choice == 1:
            print("Security hardening is applied to all servers") # apply security hardening to all servers
        
        elif choice == 2:
            print("Web Server is created on server1")# apply Web Server config to server1
        elif choice == 3:
            print("Mail server is created on server2")# apply Mail Server config to server2
        elif choice == 4:
            print("Database server is created on server3 ")# apply Database Server config to server3
        elif choice == 5:
            print("You are exiting this program")
            break

        repeat = input("Do you want to make another configuration? (yes/no): ")
        if repeat.lower() != 'yes':
                print('Have a nice day!')
                break


if __name__ == "__main__":
    main()

