thisnum = int(input("enter number"))
lownum = thisnum
while thisnum != 0:
    if (thisnum < lownum) and (thisnum > 0):
        lownum = thisnum
    thisnum = int(input("enter number"))
print(lownum)