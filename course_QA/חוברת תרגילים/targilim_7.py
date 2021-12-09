num = 0
sum = 0
for i in range (1,6,1):
    num = int(input("enter number"))
    num = num % 10
    sum += num
print (sum)