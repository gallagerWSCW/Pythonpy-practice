import re
while True:
    valid = True
    #Asking the user a password and store it
    pswd=input("Please enter a password:\n")
    #checking whether it meets the length requirement
    if len(pswd)<8:
        print("Your password must have at least 8 characters")
        valid=False
    #checking for at least one lowercase letter
    if not re.search(r"[a-z]", pswd):
        print("Your password must have at least one lower case letter")
        valid=False
    #Checking for at least one upper case letter
    if not re.search(r"[A-Z]", pswd):
        print("Your password must have at least one upper case letter")
        valid=False
    #Checking for a special character
    if not re.search(r"[!@#$%^&*()\-\+`,.<>/?;:\\|]", pswd):
        print("Your password must have at least one special character")
        valid=False
    #Tell whether their password meet requirements or have to make another one
    if valid:
        print("Your password meets all the requirements")
        break
    else:
        print("Please try again\n")