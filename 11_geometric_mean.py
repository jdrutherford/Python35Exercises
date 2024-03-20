#11. Python program to find the geometric mean of n numbers  
total = 1
count = 1
n = int(input("Provide the count of numbers you wish to find the geometric mean of (int):"))
print(n)

for i in range(n):
    total = total * float(input(f"Provide a number [{count} of {n}] :"))
    count += 1
print(total ** (1/n))