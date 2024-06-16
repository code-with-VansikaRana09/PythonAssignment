# WAP that calculates the sum of the digits of a given number
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    temp = num % 10
    sum = sum + temp
    num = num//10
print("The Sum is: ",sum)

