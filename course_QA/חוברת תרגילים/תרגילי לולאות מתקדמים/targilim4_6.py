# num = input("enter number")
# print(num[::-1])
# print(2*int(num[::-1]))

num = input("enter number")
rev = ''
for i in range(len(num), 0, -1):
    rev += num[i-1]
print(int(rev))
