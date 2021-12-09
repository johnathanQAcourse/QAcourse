number = int(input("enter number"))
rishoni = 'true'
if number>1:
    for i in range(2,number):
        if (number%i==0):
            rishoni = 'false'
            print(f"the number {number} is devided by {i}")
    if rishoni == 'true':
        print("number is rishoni")
    else:
        print("number is not rishoni")
else:
    print("number is not rishoni")