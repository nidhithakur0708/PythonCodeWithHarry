#A spam comment is defined as a text containing the keywords 
#"Make a lot of money" "buy now" "subcribe this" "click this"
#WAP to detect this spams

p1="Make a lot of money"
p2="buy now"
p3="subcribe this"
p4="click this"

message=input("Enter your message: ")
if(p1 in message or p2 in message or p3 in message or p4 in message):
	print("This is a spam comment.")
else:
	print("This is not a spam comment.")

#in-keyword-gives true or false
print("Harry" in "Harry is a good boy") #True
