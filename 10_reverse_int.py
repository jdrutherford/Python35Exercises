#10. Python program to display the given integer in a reverse manner    
int_forward = (input("Enter an integer to reverse: "))
digits = len(int_forward)
int_reverse = int(str(int_forward)[::-1])
print(int_reverse)

#Breaking it down, 
#string[:] means: "take the string from beginning to end", 
# and string[::-1] means that the string should be taken one step at a time, 
# adding -1 to the index after each step.
#https://pythonprinciples.com/blog/ways-to-reverse-a-python-string/#:~:text=The%20usual%20way%20to%20reverse%20a%20string%20is,adding%20-1%20to%20the%20index%20after%20each%20step.