#WAP to find out whether a student passsed ot failed if it requires total 40% to and atleast 33% 
#in each subject to pass. Assume 3 subjects and take marks as input from the user

m1=int(input("Enter marks of subject 1: "))
m2=int(input("Enter marks of subject 2: "))
m3=int(input("Enter marks of subject 3: "))

total_perectage=(100*(m1+m2+m3))/300

if(total_perectage>=40 and m1>=33 and m2>=33 and m3>=33):
	print("Congratulations! You have passed the exam.")
else:
	print("You failed,try again next time.")
