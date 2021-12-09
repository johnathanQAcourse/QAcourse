age = int(input("insert age"))
if (age>=0) and (age<=18):
    print("child")
if (age>18) and (age<60):
    print("adult")
if (age>=60) and (age<121):
    print("senior")
if(age<=0) or (age>120):
    print("error")
