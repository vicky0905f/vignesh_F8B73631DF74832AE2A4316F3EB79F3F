#To find leap year or not.
def isLeapYear(year):
    if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
    
year= int(input("Enter a Year : "))
if isLeapYear(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not leap year.")