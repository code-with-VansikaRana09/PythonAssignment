# WAP that acts as a simple calculator . It should take two numbers and an operator as input and print the result
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
operator = input("Enter an operator: ")
if operator == "+" :
    print("The sum of numbers is: ",num1+num2)
elif operator == "-" :
    if num1>num2:
        print("The subtraction of numbers is: ", num1 - num2)
    else:
        print("The subtraction of two numbers is: ", num2-num1)
elif operator == "*" :
    print("The multiplication of two numbers is: ",num1*num2)
elif operator == "/" :
    if num2!=0:
      print("The division of two numbers is: ", num1 / num2)
    else:
        print("The division is not defined!!")


