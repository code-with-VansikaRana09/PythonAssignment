# WAP that counts the occurrences of a specific element in a list
List1 = [1,2,3,"hello","go",1,3,7,8,2,"hii",3,3,3]

element = 3
count = 0
for i in List1:
    if i == element:
        count = count + 1
print("The count of element",element," is: ",count)
