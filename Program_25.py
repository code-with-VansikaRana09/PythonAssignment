# WAP that copies the content of one text file to another

def Copy(s,d):
    f1 = open(s, 'r')
    f2 = open(d, 'w')
    data = f1.read()
    f2.write(data)
    f1.close()
    f2.close()

source = input("Enter the source file Name: ")
destination = input("Enter the destination file Name: ")
Copy(source,destination)


