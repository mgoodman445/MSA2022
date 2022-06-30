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

def login_user():
# - validate username and password combination in the users.txt file
    #open the users files
    while True:
        user_name = input("Please enter your username: ")
        user_pass = input("Please enter your password: ")
       
        user_file = open("users.txt", "r")
        user_found = False

                #read the lines from the file
        for line in user_file:
            credentials = line.split(", ")
        #compare username and password for a match
            if user_name == credentials[0] and user_pass == credentials[1].rstrip():
                user_found = True
                break

        if user_found:
                # - if valid then move on to the next prompt
                print(f"User {user_name} successfully logged in\n")
                break
        else:
                # - if not valid combination reprompt the user
                print(f"User {user_name} not found\n")
    
    return user_found

def create_user():
    while True:
        user_name = get_valid_username_or_password("Please enter your username (4-12 characters): ", 4, 12)
        user_pass = get_valid_username_or_password("Please enter your password (6-16 characters): ", 6, 16)
        #write username and password to file
        try:
            user_file = open("users.txt", "a")
            user_file.write(f"\r{user_name}, {user_pass}")
        except:
            print("Error creating user.\n")
            continue
        else:
            print(f"User: {user_name} created")
        finally:
            user_file.close()
            break
    return

def get_valid_username_or_password(prompt, min_length, max_length):
    while True:
        user_input = input(prompt)
        input_length = len(user_input)
        if (input_length >= min_length and input_length <= max_length):
            break
        else:
            #If not valid reprompt user
            print("ERROR: Input length invalid.\n") 
    
    return user_input

def get_integer_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
        except:
            print("ERROR: input must be a number.\n")
        else:
            break
    return user_input

def get_letter_grade(score):
    if score >= 60 and score < 70:
        return "D"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 90:
        return "A"
    else:
        return "F"

def load_students_scores_and_grades(number_of_students):
    student_names, scores_list, student_letter_grades = [], [], [],
    for counter in range(number_of_students):
        #Prompt user to enter student name and number score
        student_name = input("Enter student name: ")
        student_score = get_integer_input("Enter student score: ")
        #Store data in the lists
        student_names.append(student_name)
        scores_list.append(student_score)
        student_letter_grades.append(get_letter_grade(student_score))
    return student_names, scores_list, student_letter_grades


def main():
    print_main_menu()
    user_option = get_user_option()
    if user_option == "1":
       login_user()
    elif user_option == "2":
        create_user()

    #Create 3 empty list for student name, scores, letter grades
    #Ask user how many students to enter data for
    number_of_students = get_integer_input("How many student's grades would you like to calculate? ")
    student_names, student_scores, student_letter_grades = load_students_scores_and_grades(number_of_students)
    for index in range(len(student_names)):
        print(f"{student_names[index]} : {student_scores[index]} : {student_letter_grades[index]}")

    #Calculate and print class average
    class_average = statistics.mean(student_scores)
    print(f"Average: {class_average}")

main()