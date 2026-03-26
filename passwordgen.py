import random
import string


letters=string.ascii_letters
digits=string.digits
pun=string.punctuation
b=input("Do you want special characters?(y/n)")
if b=="y":
	pool=letters+digits+pun
else:
	pool=letters+digits
	

a=input("Enter lenght you want your pass to be")
c=input("How many password do you want?")
for j in range(int(c)):
	password=""
	for i in range(int(a)):
		password += random.choice(pool)
	print (password)
