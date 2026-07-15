import random
import string

l=int(input("Enter length of password: "))
ch=string.ascii_letters+string.digits+string.punctuation
pswrd=""

for i in range(l):
    pswrd+=random.choice(ch)

print(pswrd)