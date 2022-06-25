#Print the menu
from ast import Store


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

        #read the lines from the file
        for line in user_file:
            credentials = line.split(", ")
            #compare username and password for a match
            if user_name == credentials[0] and user_pass == credentials[1].rstrip():
                print(f"User {user_name} successfully logged in\n")
                user_found = True
                break

        if user_found:
            # - if valid then move on to the next prompt
            print(f"User {user_name} successfully logged in\n")
            break
        else:
            # - if not valid combination reprompt the user
            print(f"User {user_name} not found\n")
        
elif user_option == "2":
    run_again = True
    while(run_again):
        #If user chose 2, ask for user name and password and
        user_name = input("Please enter your username (4-12 characters): ")
        user_pass = input("Please enter your password (6-16 characters): ")
        # - validate username and password length. If valid, write to users.txt file
        username_length = len(user_name)
        password_length = len(user_pass)
        if (username_length >= 4 and username_length <= 12) and (password_length >= 6 and password_length <= 16):
            user_file = open("users.txt", "a")
            user_file.write(f"{user_name}, {user_pass}\n")
            user_file.close()
            print("\nAccount successfully created\n")
            # - and move on
            run_again = False
        else:
            #If not valid reprompt user
            print("ERROR: Username and password must be within the character limit\n")

#Create 3 empty list for student name, scores, letter grades
list_of_student_names = []
list_of_student_scores = []
list_of_letter_grades = []
#Ask user how many students to enter data for
number_of_students = input("How many student's grades would you like to calculate? ")
 
for num in range(number_of_students):
    #Prompt user to enter student name and number score
    student_names = input("What is the name of the student? ")
    Store(student_names) in list_of_student_names
    student_score = input("What is the student's score? ")
    Store(student_score) in list_of_student_scores
#Store data somewhere
#Convert number to a letter grade
#Print student data
#Calculate and print class average