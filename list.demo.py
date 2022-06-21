import random 
list_of_numbers = [6, 5, 3, 8, 4, 2, 5, 11, 53, 17, 27, 99, 62, 61, 51, 47]

for number in list_of_numbers:
    print(number)

print("\n\n")
number_of_items_in_list = len(list_of_numbers)
for index in range(number_of_items_in_list):
    print(f"Item {index + 1}: {list_of_numbers[index]}")

print("Add all numbers on the list")
total = 0
for number in list_of_numbers:
    total = total + number

print(f"Total: {total}")

print("\nRange Function Parameters")
for index in range(0, number_of_items_in_list, 2):
    print(f"Item {index}: {list_of_numbers[index]}")

print("Print random values from list")
for number in range(3):
    index = random.randint(0, number_of_items_in_list - 1)
    print(list_of_numbers[index])