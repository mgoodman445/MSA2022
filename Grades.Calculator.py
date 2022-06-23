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

#If user chose 1, ask for user name and password and
# - validate username and password combination in the users.txt file
# - if not valid combination reprompt the user
# - if valid, then move on to prompt for student data
#If user chose 2, ask for username and password and
# - validate username and password length. If valid, wrtie to users.txt file
# - and move on
#If not valid reprompt user

#Ask user how many students to enter data for
#Prompt user to enter student name and number score
#Store data somewhere
#Convert number score to a letter grade

#Print student data(name, score, grade)
#Calculate and print class average