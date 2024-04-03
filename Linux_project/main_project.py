#!/usr/bin/python3

option_1 = "1. Security Hardening"
option_2 = "2. Web Server"
option_3 = "3. Mail Server"
option_4 = "4. Database Server"
option_5 = "5. Quit."

title = "Quick Linux Server Configuration"
lines = "*"*33

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

def main():
    choice = ' '
    while choice != 5:
        show_menu()
        choice = int(input('Please make a selection. > '))
        if choice == 1:
            print("Security Hardening is applied to all servers") # apply Security Hardening ansible playbook to all servers
        
        elif choice == 2:
            print("Web Server is created on server1")# apply Web Server to server1 via paramiko
        elif choice == 3:
            print("Mail server is created on server2")# apply Mail Server to server2 via paramiko
        elif choice == 4:
            print("Database server is created on server3")# apply Database Server to server3 via paramiko
        elif choice == 5:
            print("You are exiting this program")
            break

        repeat = input("Do you want to make another configuration? (yes/no): ")
        if repeat.lower() != 'yes':
                print('Have a nice day!')
                break


if __name__ == "__main__":
    main()

