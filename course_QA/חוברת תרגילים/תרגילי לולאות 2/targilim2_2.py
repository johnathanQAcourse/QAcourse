password = input("enter password")
count = 0
checkpass = input("enter verification password")
while count < 4:
    if checkpass == password:
        print("success")
        break
    else:
        count += 1
    checkpass = input("wrong verificaion password, try again")
if count == 4:
    print("too many tries")