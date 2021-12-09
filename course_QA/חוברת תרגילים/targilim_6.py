grade = int(input("enter grade"))
if (grade >= 0) and  (grade <= 100):
    sum1 = 0
    sum2 = 0
    count1 = 0
    count2 = 0
    while (grade >= 0) and  (grade <= 100):
        if(grade>60):
            sum1 += grade
            count1 += 1
        if grade<60 :
            sum2 += grade
            count2 += 1
        grade = int(input("enter grade"))
    print(f"the average of passing grades is{sum1/count1}")
    print(f"the average of not passing grades is{sum2/count2}")
