#7. Python program to check whether the given integer is a multiple of 5 
print("Check if a number is a multiple of 5:")
number = int(input("Provide an integer:"))
multiple = number % 5 == 0
if multiple:
    print(f"Yes, {number} is a multiple of 5!")
else:
    print(f"No, {number} is not a multiple of 5!")