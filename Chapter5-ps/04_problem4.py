#What will be the length 
'''
s=set()
s.add(20)
s.add(20.0)
s.add('20')
'''
s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))

#20 and 20.0 are considered the same in a set because they are equal in value, while '20' is a string and is considered different. Therefore, the length of the set will be 2.
