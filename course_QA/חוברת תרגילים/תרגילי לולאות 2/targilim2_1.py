thisgrade = int(input("enter grade"))
higrade = thisgrade
count = 0
sum = 0
if (thisgrade >= 0) and (thisgrade <= 100):
    while (thisgrade >= 0) and (thisgrade <= 100):
        if higrade<thisgrade:
            higrade = thisgrade
        count += 1
        sum += thisgrade
        thisgrade = int(input("enter grade"))
print(f"the highest grade is:{higrade}\nthe average is:{sum/count}")
