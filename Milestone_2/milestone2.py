import re

while True:
    valid = True
    pswd=input("Please enter a password:\n")
    if len(pswd)<=8:
        print("Your password must have at least 8 characters")
        valid=False
    if not re.search(r"[a-z]", pswd):
        print("Your password must have at least one lower case letter")
        valid=False
    if not re.search(r"[A-Z]", pswd):
        print("Your password must have at least one upper case letter")
        valid=False
    if not re.search(r"[!@#$%^&*()-+`,.<>/?;:|]", pswd):
        print("Your password must have at least one special character")
        valid=False
    if valid:
        print("Your password meets all the requirements")
        break
    else:
        print("Please try again\n")
        

