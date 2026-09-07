#WAP to find wheter a givenusername contains less than 10 characters or not. If it contains less than 10 characters then print a message "Valid username" otherwise print "Invalid username"
username=input("Enter your username: ")
if(len(username)<10):
	print("Valid username,less than 10 characters")	
else:
	print("Invalid username")
