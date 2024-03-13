count = int((float(input("Enter the amount of numbers you want to multiply : "))))
entered = 0
product = 1
print(f"This program will find the product of {count} numbers")

while entered < count:
    product = product * float(input("Enter an number : "))
    entered = entered + 1
else:
    print(f"The product of these numbers is: {round(product,2)}!")