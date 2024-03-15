#9. Python program to find the average of 10 numbers using while loop    
count = 0
numbers = []
sum = 0
print("Enter 10 numbers and I will display the average.")
while count < 10:
    count = count + 1
    input_num = float(input(f"Input number {count}:"))
    sum = sum + input_num
    numbers.append(input_num)
average = sum / 10
print(f"These are the numbers you entered \n {numbers}")
print(f"The sum of these numbers is {sum}")
print(f"The average is {average}")