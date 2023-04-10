# Import datetime for using current date
from datetime import date

# ====Login Section====
# Open user.txt file as r as details
# Use for loop to convert every line to string, by ', '
# Save first index of list in lines as username, and second index as password
# Ask user to input username and password. Save in variables

with open('user.txt', 'r') as details:
    for line in details:
        user_info = line.split(", ")
        user_name = user_info[0]
        user_pass = user_info[1]
    credentials = []
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    credentials.append(username + " " + password)

# Username and password checks
# Use if statements.
# Use nested while statements to repeat input if username or password is entered incorrectly
if username != user_name and password == user_pass:
    print("\nInvalid username. Please try again!")
    username = input("Please enter your username: ")
    while username != user_name:
        print("\nInvalid username. Please try again!")
        username = input("Please enter your username: ")
        continue
    else:
        print("\nWelcome")
elif username == user_name and password != user_pass:
    print("\nInvalid password. Please try again!")
    password = input("Please enter your password: ")
    while password != user_pass:
        print("\nInvalid password. Please try again!")
        password = input("Please enter your password: ")
        continue
    else:
        print("\nWelcome")      #if u and p are wrong it continues. check
else:
    print("\nWelcome")

# Infinite while loop to print menu of options
# *** FOR COMPULSORY TASK 2 - used if/else to print different menu for admin and normal users
# Change input of user to lowercase
while True:
    if username == "admin":
        menu = input('''\nSelect one of the following options below:
        r - Register a new user
        a - Add a task
        va - View all tasks
        vm - View my task
        s - Statistics
        e - Exit
        : ''').lower()
    else:
        menu = input('''\nSelect one of the following options below:
        r - Register a user
        a - Add a task
        va - View all tasks
        vm - View my task
        e - Exit
        : ''').lower()

# If menu == r
# *** FOR COMPULSORY TASK 2, if/ else to allow only admin to make new user
    # if username was admin let admin create user, else don't
    # Save new username and password in different variables
    # Ask to re-enter password to check if it matches
    # Used a while loop to request password again if passwords do not match
        # Else statement prints the new username and password
# Used with open to write the new user in user.txt file in format of username, password
    if menu == 'r':
        if username == "admin":
            new_user = input("Please enter a username of your choice: ")
            new_user_pass = input("Please enter a password you will remember: ")
            new_user_pass_check = input("Please re-enter your password: ")
            while new_user_pass_check != new_user_pass:
                print("Your passwords do not match!")
                new_user_pass = input("Please enter a password you will remember: ")
                new_user_pass_check = input("Please re-enter your password: ")
                continue
            else:
                print(f"Your username is '{new_user}' and your password is '{new_user_pass}'. \n---Welcome---")
            with open('user.txt', 'a+') as details:
                details.write('\n' + new_user + ", " + new_user_pass)
        else:
            print("Only the ADMIN can register new users!")

# If menu == a
# Save the name of user task is assigned to in a variable
# Along with the title, description, and due date. Capitalize inputs for Grammar
# Assigned date was asked to be made into current date of using this code, so date.today() used
# Used a "with open tasks.txt" to append new task in correct format( separated by ', ')
    elif menu == 'a':
        username_task = input("Please enter the username of the person the task will be assigned to: ")
        task_title = input("Please enter the title of the task: ").capitalize()
        description = input("Please enter a description of the task: ").capitalize()
        due_date = input("Please enter the due date of the task: ")
        assigned_date = date.today()
        with open('tasks.txt', 'a+') as tasks:
            tasks.write('\n' + username_task + ", " + task_title + ", " + description + ", " + due_date + ", " +
                        str(assigned_date) + ", No")

# If menu == va
# Used with open tasks.txt as read+
# Used for loop to split lines into list
# Print the contents in ordered format as requested
# Used indexing to concatenate to printed output
    elif menu == 'va':
        with open('tasks.txt', 'r+') as tasks:
            for line in tasks:
                tasks_list = line.split(", ")
                print("Assigned to: " + tasks_list[0] + '\n' +
                      "Task: " + tasks_list[1] + '\n' +
                      "Task Description: " + tasks_list[2] + '\n' +
                      "Date assigned: " + tasks_list[3] + "\n" +
                      "Due date: " + tasks_list[4] + "\n" +
                      "Task Complete: " + tasks_list[5] + '\n' +
                      "*********************\n")

# If menu == vm
# Used with open tasks.txt as read+
# Used for loop to split lines at ", " and save in variable
# Used while loop to print the tasks of only the user that's using program
    # Used while loop, not for loop, to display ALL tasks that belong to a user
# Printed in format requested
    elif menu == 'vm':
        with open('tasks.txt', 'r+') as tasks:
            for line in tasks:
                tasks_list = line.split(", ")
                while username == tasks_list[0]:
                    print("Assigned to: " + tasks_list[0] + '\n' +
                          "Task: " + tasks_list[1] + '\n' +
                          "Task Description: " + tasks_list[2] + '\n' +
                          "Date assigned: " + tasks_list[3] + "\n" +
                          "Due date: " + tasks_list[4] + "\n" +
                          "Task Complete: " + tasks_list[5] + '\n' +
                          "*********************\n")
                    break

# *** FOR COMPULSORY TASK 2
# Used if menu == s BUT ALSO used and username == admin
# to make sure that only admin can use this feature
# Used with open tasks.txt as read
# set a counter variable to 0
# created variable to read contents of tasks.txt
# Split the txt file at new lines to count how many tasks
# Used for loop to add 1 to counter variable for each line in txt file
# Prints the counter variable as no. of tasks
    elif menu == 's' and username == 'admin':
        with open('tasks.txt', 'r') as users:
            i = 0  # counter variable
            j = 0
            contents = users.read()
            counter = contents.split('\n')  # separated by new line as split condition
            for x in counter:
                i += 1  # increased counter variable by 1
            print("Number of tasks: " + str(i))

# Used with open users.txt as read
# set a counter variable to 0
# created variable to read contents of users.txt
# Split the txt file at new lines to count how many users based on how many lines
# Used for loop to add 1 to counter variable for each line in txt file
# Prints the counter variable as no. of users
        with open('user.txt', 'r') as users:
            contents = users.read()
            counter = contents.split('\n')
            for line in counter:
                j += 1
            print("Number of users: " + str(j))

# If menu == e
    # Print goodbye and exit
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

# Else if any other inputs, print error
    else:
        print("You have made a wrong choice, Please Try again")
