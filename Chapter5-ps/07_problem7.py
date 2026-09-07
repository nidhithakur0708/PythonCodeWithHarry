#If the same of 2 friends are same,what will happen tothe program in Q6
d={}

name=input("Enter friends name: ")
lang=input("Enter friends favourite language: ")
d.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter friends favourite language: ")
d.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter friends favourite language: ")
d.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter friends favourite language: ")
d.update({name:lang})

print(d)

#If the same name of 2 friends are entered, the program will update the value for that name in the dictionary, effectively overwriting the previous entry. Therefore, only the last entered language for that name will be stored.
