# WAP that counts frequency of each character in a string
str1 = input("enter a string: ")
dict1 = {}
for i in str1:
    if i in dict1:
        dict1[i] +=1
    else:
        dict1[i] =1
print("count of all characters is:\n " , dict1)