#importing the current date
from datetime import date
#Asking the user to enter their birthday
birth_year=int(input("What is your birth year?: "))
birth_month=int(input("What is your birth month? (1-12): "))
birth_day=int(input("When is your birthday? (1-31): "))
#Making the current date and the user's birthday as variables
today=date.today()
birth_date=date(birth_year,birth_month,birth_day)

#Calculating the differnce
year=today.year-birth_date.year
month=today.month-birth_date.month
day=today.day-birth_date.day

#Adjust days and months if needed
if day<1:
    month-=1
    day+=30

if month<1:
    year-=1
    month+=12

print("you are {} years, {} months and {} days old".format(year,month,day))
print(today, birth_date)
