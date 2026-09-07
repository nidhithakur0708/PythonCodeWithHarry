#Sets in Python

emptyset=set() #empty set
s={}# this is a empty dictionary , not a set
print(type(emptyset)) #<class 'set'>

#sets will take unique values,not in a sorted order
s={1,2,3,4,5,5,6,6,7,1,34,5}
print(s)

#sets can have multiple datatype
p={"nidhi","ram","simran","siraj",23,34}
print(p,type(p))
