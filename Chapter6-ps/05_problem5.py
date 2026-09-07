#WAP to find if a name is present in the list or not
names=["John","Alice","Bob","Eve","Charlie"]
name=input("Enter a name to search: ")

if(name in names):
	print("Your name is in the list")
else:
	print("Your name is not in the list")
