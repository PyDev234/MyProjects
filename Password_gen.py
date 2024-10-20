# Program to generate unique password and unique IDs
import string                               # for getting all the character that occur in password          
# Need to install shortuuid from pip
import shortuuid                            # for generating short unique IDs
import uuid                                 # for generating Unique IDs
from random import randint, shuffle         # for generating random password

# Storing all the letters, digits, and special symbols in lookup_dictionary
lookup_dictionary = list(string.ascii_letters + string.digits + string.punctuation)

# randomizing the elements in lookup_dictionary using shuffle
shuffle(lookup_dictionary)

# A empty list for storing the password
password = []

# Menu
print("\tMenu\n1.Generate Password\n2.Generate Short Uuid\n3.Generate long Uuid")
print("Give only the choice number")

# Taking user choice
ch = input("Enter your choice : ")

# Using match case in python for matching the choice of user
match(ch):
    case '1':
        # Taking the length of password
        n = int(input("Enter the length of password : "))
        for i in range(n):
            password.append(lookup_dictionary[randint(0,93)])

        password = "".join(password)
        print("Your Random password is -> "+password)

    case '2':
        print("Your Random Short Uuid is -> "+shortuuid.uuid()) 

    case '3':
        print("Your Random Uuid is -> "+str(uuid.uuid4()))

    case _:
        print("Oops! Wrong input\nTry Again")