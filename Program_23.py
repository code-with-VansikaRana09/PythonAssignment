# WAP that converts temperature from Celsius to Fahrenheit and vice versa based on user input
Ctemp = float(input("Enter temperature in celsius: "))
Ftemp = float(input("Enter temperature in fahrenheit: "))
# for Celsius to Fahrenheit
F = (Ctemp*9/5)+32
print("Celsius to Fahrenheit temperature is : ", F)
# for Fahrenheit to Celsius
C = ((Ftemp-32)/9)*5
print("Fahrenheit to Celsius temperature is : ", C)


