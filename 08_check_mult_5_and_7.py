#8. Python program to check whether the given integer is a multiple of both 5 and 7    
print("Check if a number is a multiple of 5:")
number = int(input("Provide an integer:"))
multiple_of_5 = number % 5 == 0
multiple_of_7 = number % 7 == 0
if multiple_of_5 and multiple_of_7:
    print(f"Yes, {number} is a multiple of 5 and 7!")
elif multiple_of_5:
    print(f"{number} is a multiple of 5 but not a multiple of 7!")
elif multiple_of_7:
    print(f"{number} is a multiple of 7 but not a multiple of 5!")
else:
    print(f"No, {number} is not a multiple of 5 or 7!")