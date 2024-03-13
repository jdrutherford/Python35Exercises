count = int(float(input("Enter the amount of numbers you want to average : ")))
entered = 0
sum = 0
print(f"This program will find the average of {count} integers")

while entered < count:
    sum = sum + int(float(input("Enter an integer : ")))
    entered = entered + 1
else:
    print(f"The average of these numbers is: {round(sum/count,2)}!")