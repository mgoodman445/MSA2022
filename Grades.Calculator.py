#Print the menu
print("Select option from Menu\n-----------------------")
print("1. Login")
print("2. Create User")

#Prompt and get the option the user selected
while True:
    user_option = input("Would you like to (1) login or (2) create an account? ")
    #Ensure the user entered a valid option (1 or 2)
    if user_option != "1" and user_option != "2":
        # - if not, prompt user again
        print("\nERROR: Enter a 1 or 2")
        continue
    else: 
        break

if user_option == "1":
    while True:
        #If user chose 1, ask for user name and password and  
        user_name = input("Please enter your username: ")
        user_pass = input("Please enter your password: ")
        # - validate username and password combination in the users.txt file
        #open the users files
        user_file = open("users.txt", "r")
        user_found = False
        for line in user_file:
            credentials = line.split(", ")
            if user_name == credentials[0] and user_pass == credentials[1].rstrip():
                print(f"User {user_name} successfully logged in\n")
                user_found = True
                break

        if user_found:
            print(f"User {user_name} successfully logged in\n")
            break
        else:
            print(f"User {user_name} not found\n")


        #read the lines from the file
        #compare username and password for a match
        # - if not valid combination reprompt the user
        # - if valid then move on to the next prompt

#If user chose 2, ask for user name and password and
# - validate username and password length. If valid, write to users.txt file
# - and move on
#If not valid reprompt user

#Ask user how many students to enter data for
#Prompt user to enter student name and number score
#Store data somewhere
#Convert number to a letter grade
#Print student data
#Calculate and print class average
