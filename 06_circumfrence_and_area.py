#6. Python program to find the circumference and area of a circle with a given radius
import math
print("This program will display the circumference and area of a circle.")
radius = float(input("Please enter the radius:"))
circumference = math.pi * radius * 2 
area = math.pi * radius ** 2 
print(f"Circumference: {round(circumference,2)}\nArea: {round(area,2)}")
