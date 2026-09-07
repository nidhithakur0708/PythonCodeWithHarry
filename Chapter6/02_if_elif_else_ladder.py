age=int(input("Enter your age: "))
#If elif else ladder
if(age>18):
	print("You are eligible to vote.")
	print("Good for you!")

elif(age<0):
	print("You are not born yet.")
elif(age==0):
	print("You are a newborn baby.")
else:
	print("You are not eligible to vote.")

print("End of program")
