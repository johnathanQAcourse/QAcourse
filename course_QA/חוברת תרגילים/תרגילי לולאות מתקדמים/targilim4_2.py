num = int(input("enter number"))
count = 1
if num >= 10:
    while num > 9:
        num = num // 10
        count += 1
print(count)