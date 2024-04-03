#14. Python program to display all integers within the range 100-200 whose sum of digits is an even number    

#default end of print is \n new line. replacing it with " " using print(____,end=" ") doesn't create a new line, 
#as we loop it will end each print statement with only a space and start the next one right after

for number in range(100,201):
    if (number + 2) % 20 == 0:
        print(number)
    elif number%2 == 0:
        print(number,end=" ")