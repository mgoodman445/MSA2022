import statistics

def print_main_menu():
   #Print the menu
    print("Select option from Menu\n-----------------------")
    print("1. Login")
    print("2. Create User")

def get_user_option():
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
    return user_option

def login_user(u_name, u_pass):
# - validate username and password combination in the users.txt file
    #open the users files
    user_file = open("users.txt", "r")
    user_found = False

            #read the lines from the file
    for line in user_file:
        credentials = line.split(", ")
    #compare username and password for a match
        if u_name == credentials[0] and u_pass == credentials[1].rstrip():
            print(f"User {u_name} successfully logged in\n")
            user_found = True
            break
    return user_found

def create_user(u_name, u_pass):
    pass

def validate_username_or_password(user_credential, min_length, max_length):
    if (user_credential >= min_length and user_credential <= max_length):
        return True
    else:
        #If not valid reprompt user
        print("ERROR: Username and password must be within the character limit\n")   
        return False
def main():
    print_main_menu()
    user_option = get_user_option()
    if user_option == "1":
        while True:
            #If user chose 1, ask for user name and password and  
            user_name = input("Please enter your username: ")
            user_pass = input("Please enter your password: ")
            user_logged_in = login_user(user_name, user_pass)

            if user_logged_in:
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
                user_file.write(f"\r{user_name}, {user_pass}")
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
    number_of_students = int(input("How many student's grades would you like to calculate? "))
    
    for counter in range(number_of_students):
        #Prompt user to enter student name and number score
        student_name = input("What is the name of the student? ")
        student_score = float(input("What is the student's score? "))
        #Store data in the lists
        list_of_student_names.append(student_name)
        list_of_student_scores.append(student_score)
        #Convert the current number to a letter grade and store in the letter grade list
        if student_score >= 60 and student_score < 70:
            list_of_letter_grades.append("D")
        elif student_score >= 70 and student_score < 80:
            list_of_letter_grades.append("C")
        elif student_score >= 80 and student_score < 90:
            list_of_letter_grades.append("B")
        elif student_score >= 90:
            list_of_letter_grades.append("A")
        else:
            list_of_letter_grades.append("F")

    #Print student data
    for index in range(len(list_of_student_names)):
        print(f"{list_of_student_names[index]} : {list_of_student_scores[index]} : {list_of_letter_grades[index]}")

    #Calculate and print class average
    class_average = statistics.mean(list_of_student_scores)
    print(f"Average: {class_average}")

main()