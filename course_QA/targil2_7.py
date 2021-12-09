day = int(input("enter day"))
month = int(input("enter month"))
year = int(input("enter year"))
if (day<31) and (day>0):
            if (month>0) and (month<=12):
                if (year<2021) and (year>1949):
                    year = str(year)
                    print(f"{day}/{month}/{year[1:3]}")
else:
    print("error")