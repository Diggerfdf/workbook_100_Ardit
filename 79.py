import regex as re

passwd = input("Input your password: ")
x = True

while x:
    if (len(passwd)<5 or len(passwd)>12):
        break
    elif not re.search("[a-z]", passwd):
        break
    elif not re.search("[0-9]", passwd):
        break
    elif not re.search("[A-Z]", passwd):
        break
    elif not re.search("[$#@]", passwd):
        break
    elif re.search("\\s", passwd):
        break
    else:
        print("Valid Password")
        x = False
        break


if x:
    print("Not a Valid Password")


# Ardit's Solution:

while True:
    psw = input("Enter new Password: ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is fine")

    else:
        print("Password is not good")
