# WAP that takes a string input from the user and writes it to a text file
Str = input("Enter a String: ")
SampleFile = open("C:/Users/dell/Desktop/PYTHON/Program5.txt",'w')
print("The String is: ",Str,end='',file=SampleFile)



