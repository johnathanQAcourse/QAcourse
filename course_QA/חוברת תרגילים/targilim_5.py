grade = int(input("enter grade"))
sum = 0
count = 0
while (grade >= 0) and  (grade <= 100):
    if(grade>60):
        sum += grade
        count += 1
    grade = int(input("enter grade"))
print(f"the average of passing grades is{sum/count}")