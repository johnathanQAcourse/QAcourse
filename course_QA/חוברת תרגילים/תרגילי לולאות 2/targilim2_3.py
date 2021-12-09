num = int(input("enter number"))
sum = 0
while num >10:
    sum += num % 10
    num = num // 10
if sum == 0:
    print(num)
if num < 10:
    sum += num
    print(sum)
