import re

pas = input("Masukkan password : ")

def isPasswordValid(pas):
    char = "[`~!@#$%^&*()_+={}|:<>?',.]"

    if(len(pas) < 8):
        return False
    elif not re.search("[a-z]", pas):
        return False
    elif not re.search("[A-Z]", pas):
        return False
    elif not re.search("[0-9]", pas):
        return False
    elif not re.search(char, pas):
        return False

    else:
        return True

if isPasswordValid(pas) == True:
    print("Valid Password")
else:
    print("Not a Valid Password")

