#13 Python program to display all the multiples of 3 within the range 10 to 50   

#default end of print is \n new line. replacing it with " " using print(____,end=" ") doesn't create a new line, 
#as we loop it will end each print statement with only a space and start the next one right after

for number in range (10,50):
    if number % 3 == 0:
        print(number,end=" ")