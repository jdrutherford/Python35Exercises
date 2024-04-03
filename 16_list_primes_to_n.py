#16. Python program to generate the prime numbers from 1 to N 
run = True

def isprime(num):
    prime = True
    for n in range(2,num-1):
        if num % n == 0:
            prime = False
    if num == 1:
        prime = True
    return prime 

def listprime(num):
    list = []
    for n in range(1,num):
        if isprime(n):
            list.append(n)
    return list



#if number 
while run:
    number = int(input("input an integer:"))
    print(listprime(number))
