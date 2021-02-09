# Mini project - Random Password Generator !
# Importing the relevant modules
from random import randint
# Randint is a random integer

# All uppercase password
password1 = ""
for i in range(10):
    i = chr(randint(65,90)) # Generate a random Uppercase letter (based on ASCII code)
    password1 = str(password1) + i # Makes password1 a string and add random letters
print("Password1 Generated:", password1)

# Creates random password with mixture of lower and upper case
password2 = ""
for i in range(5): # creates password 10 letters long , accounts for uppercase letter
    i = chr(randint(65, 90)) # Generate a random Uppercase letter (based on ASCII code)
    for j in range(5): # accounts for the lower case letters in password2
        j = chr(randint(65, 90)).lower()
    password2 = str(password2) + i + j
print("Password2 Generated :", password2)



