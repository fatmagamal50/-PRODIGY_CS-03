#Task-03 password complexity checker

def Check_Password(input_Pass):
    x=len(input_Pass)
    is_lower=False
    is_upper=False
    is_num = False
    is_special=False
    not_special="0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"

    for i in range(x):
        if input_Pass[i].islower():
            is_lower=True
        if input_Pass[i].isupper():
            is_upper=True
        if input_Pass[i].isdigit():
            is_num=True
        if input_Pass[i] not in not_special:
            is_special=True

    if (is_upper and is_lower and is_num and is_special and (8<x<=16)):
            print("Strong Password")

    elif ((is_upper or is_lower) and is_special and (4<x<=8)):
            print("Moderate Password")
    else:
            print("Weak Password")




print(" to get strong pass you must enter at least one upper and one lower letter and one character and length between 8-16")
Password=input("Enter Password:")
Check_Password(Password)

