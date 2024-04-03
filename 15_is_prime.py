#15. Python program to check whether the given integer is a prime number or not  
run = True
def isprime(num):
    prime = True
    for n in range(2,num-1):
        if num % n == 0:
            print(f"{num}/{n}={num % n}")
            prime = False
    if num == 1:
        prime = True
    return prime 


#if number 
while run:
    number = int(input("input an integer:"))
    print(f"Prime? {isprime(number)}")
