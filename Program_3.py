# WAP that calculates the factorial of a given number
num1 = int(input("Enter a number: "))
fact = 1
for i in range(1,num1+1,1):

    fact=fact*i
print("The Factorial is: ",fact)

