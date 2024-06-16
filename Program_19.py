# WAP that removes all punctuation from a given string
str = input("enter a string: ")
print("The original string is: ",str)
punc = '''!-:;'",.?'''
res = " "
for i in str:
    if i not in punc:
        res+=i
print("The string after removal of punctuation: ", res)