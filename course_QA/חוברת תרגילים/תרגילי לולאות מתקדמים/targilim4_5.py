num = 0
hnum = 0
count = 1
hcount = 1
while count <= 7:
    num = int(input("enter number"))
    if hnum < num:
        hnum = num
        hcount = count
    count += 1
print(f"the highest number is {hnum} and the serial number is {hcount}")
