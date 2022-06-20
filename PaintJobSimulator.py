import math
#Function Declarations
"""
Function: to get and validate float values
Input: user prompt
Output: a validated float value
"""
def get_float_value(prompt):
    #Convert to float
    #if error in input ask user to re-enter input. Input must be greater than 0
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

#INPUT
#Declare variables for known values
hourly_labor_cost = 62.25
unit_of_wall_area = 350
hours_labor_per_unit = 6
#prompt user to enter the area of the wall
wall_area = get_float_value("What is the area of wall in sq/ft: ")
#prompt user to enter cost of paint per gallon
paint_price = get_float_value("What is the price of paint per gallon: ")

#PROCESS
#Calculate the hours of labor
hours_of_labor = (wall_area / unit_of_wall_area) * hours_labor_per_unit
#Calculate the cost of labor
labor_cost = hours_of_labor * hourly_labor_cost
#Calculate the amount of paint
gallons_of_paint = math.ceil(wall_area / unit_of_wall_area)
#Calculate the cost of the paint
paint_cost = gallons_of_paint * paint_price
#Calculate total cost of the job
total_cost = paint_cost + labor_cost

#OUTPUT
#Print hours of labor, cost of labor, amount of paint, 
#cost of paint, total job cost
print("Report\n----------------------\n")
print(f"Hours of Labor: {hours_of_labor:.2f}")
print(f"Labor Cost: ${labor_cost:.2f}")
print(f"Gallons of Paint: {gallons_of_paint}")
print(f"Paint Cost: ${paint_cost:.2f}")
print(f"Total Job Cost: ${total_cost:.2f}")