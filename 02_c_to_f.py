#Get user input Celsius and display Fahrenheit
tempc = input("Enter a temperature in Celsius : ")
tempf = float(tempc) * (9/5) + 32 
print(f"This converts to {round(tempf,2)}° Fahrenheit")
