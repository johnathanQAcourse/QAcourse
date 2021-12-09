count1 = 0
count2 = 0
sum = 0
while (count1<6):
    num = int(input("enter number"))
    if (num % 2 == 0):
        sum += num
        count2 += 1
    count1 += 1
if count2 == 0:
    print("no even numbers were entered")
else:
    print(f"the sum is {sum}, the average is{sum/count2}")