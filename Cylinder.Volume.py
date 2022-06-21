import math
#Functions
def get_value(prompt):
    run_again = True
    while (run_again):
        try:
            user_input = float(input(prompt))
            if(user_input <= 0):
                print("ERROR: Value must be greater than 0.\n")
                continue
        except:
            print("ERROR: Input must be a number.\n")
        else:
            run_again = False
    
    return user_input

def ask_again(prompt):
    
#Variables
pie = math.pi

#Input
radius = get_value("What is the radius of the cylinder in inches: ")
height = get_value("What is the height of the cylinder in inches: ")
#Process
volume = radius * height * pie * 2
#Output
print(f"The volume of the cylinder is {volume:.2f}")
#Ask Again
