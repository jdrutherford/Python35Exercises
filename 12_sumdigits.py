#12. Python program to find the sum of the digits of an integer using a while loop             
entered_integer = int(input("Enter a number (int): "))
calculated_sum = 0
digit_list = [int(i) for i in str(entered_integer)]
while len(digit_list) > 0:
    calculated_sum = calculated_sum + digit_list.pop()
print(f"The sum of the digits in {entered_integer} is {calculated_sum}")