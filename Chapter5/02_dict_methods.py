#Dictionary methods

marks={
"Nidhi": 90,
"Ram":89,
"Simran":78,
"Siraj": 90,
0:"Harry"
}

#1.items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.
print(marks.items())

#2.keys() method returns a view object that displays a list of all the keys in the dictionary.
print(marks.keys())

#3.values() method returns a view object that displays a list of all the values in the dictionary.
print(marks.values())

#4.update() method updates the dictionary with the elements from another dictionary object or from an iterable of key-value pairs.)
marks.update({"Nidhi": 95, "Ram": 92})
#If item is  not present for update it adds it
marks.update({"Renuka":100})
print(marks)

#5.get() method returns the value for the specified key if key is in dictionary.
print(marks.get("Nidhi")) #Returns the value for the specified key if key is in dictionary
print(marks["Nidhi"])
#if nidhi is not there in the dict,.get will return none but [] will give error

#6.len
len(marks)


