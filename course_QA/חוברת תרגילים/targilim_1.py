length = 1
sum = 0
while (length<=6):
    sum = sum+int(input("enter number"))
    if length<6:
        length += 1
    else:
        break
print(length)
print(f"the sum is {sum}, the average is{sum/length}")