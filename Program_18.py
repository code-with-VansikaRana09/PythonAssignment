str1 = input("enter string1: ")
str2 = input("enter string2: ")
if(sorted(str1) == sorted(str2)):
    print("The strings are anagram.")
else:
    print("The strings are not anagram.")
