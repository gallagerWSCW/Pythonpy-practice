#importing the current date
from datetime import date
print("Welcome to the age calculator")
name=input("Please enter your name before we get started.")
print(F"Hello {name.capitalize()}!!!")
#Asking the user to enter their birthday
while True:
    try:
        birth_year=int(input("What is your birth year?: "))
        birth_month=int(input("What is your birth month? (1-12): "))
        birth_day=int(input("What is the date of your birthday? (1-31): "))
        break
    except:
        print("Invalid input")
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

if month<0:
    year-=1
    month+=12

#Months day table
month_days={
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
#function to calculate the number days between 2 days
def days_between_dates(y, m1, d1, m2, d2):
    days = 0
    #birth month is before the current month
    if m1<m2:
        #Adding the number of days in every month
        for m in range (m1,m2):
            days += month_days[m]
    #birth month is after the current month
    else:
        for m in range (m1,13):
            days += month_days[m]
        for m in range (1,m2):
            days += month_days[m]
    #Finally get the difference between the current day and the birthday
    days += d2-d1
    return days #return the total number of days between the two dates
years=today.year-birth_date.year
if (today.month,today.day) < (birth_date.month,birth_date.day):
    years -=1
    days=days_between_dates(today.year-1, birth_date.month, birth_date.day, today.month, today.day)
else:
    days=days_between_dates(today.year, birth_date.month, birth_date.day, today.month, today.day)

while True:
        user_select=input("How would you like your age to be displayed? \n1. Age in years, months, and days \n2. Age in years and days\nEnter 1 or 2: ")
        if user_select==("1"):
            print("You are {} years, {} months and {} days old".format(year,month,day))
            break
        elif user_select==("2"):
            print("You are {} years and {} days old".format(years, days))
            break
        else:
            print("Invalid choice.")
while True:
    age_gap=input("WOuld you like to find the gap between your age and someone else's? (Yes / No) :").lower()
    if age_gap=="yes":
        print("Please enter the birthday details of the person you would like to compare your age with.")
        name_2=input("Please enter the person's name :").capitalize()
        while True:
            try:
                birth_year_2=int(input("Birth year : "))
                birth_month_2=int(input("Birth month? (1-12) : "))
                birth_day_2=int(input("Date of the birthday? (1-31) : "))
                birth_date_2=date(birth_year_2,birth_month_2,birth_day_2)
                break
            except:
                print("Invalid input")
        #METHOD 1        
        if user_select==("1"):#The method they wanna see the final result (Years, months, days )

            if (birth_date.year,birth_date.month,birth_date.day)<(birth_date_2.year,birth_date_2.month,birth_date_2.day):
            #If you are older than them
            #Calculating the differnce
                year2=birth_date_2.year-birth_date.year
                month2=birth_date_2.month-birth_date.month
                day2=birth_date_2.day-birth_date.day
                #Adjust days and months if needed
                if day2<1:
                    month2-=1
                    day2+=30

                if month2<0:
                    year2-=1
                    month2+=12
                print("You are {} years, {} months, {} days older than {}".format(year2, month2, day2, name_2))
            else:
            #If they are older than you
            #Calculating the differnce
                year2=birth_date.year-birth_date_2.year
                month2=birth_date.month-birth_date_2.month
                day2=birth_date.day-birth_date_2.day
                #Adjust days and months if needed
                if day2<1:
                    month2-=1
                    day2+=30

                if month2<0:
                    year2-=1
                    month2+=12
                print("{} is {} years, {} months, {} days older than you".format(name_2,year2, month2, day2))
        #METHOD 2
        elif user_select==("2"):#The method the user wanna see the final result (Years, days )
            
            if (birth_date.year,birth_date.month,birth_date.day)<(birth_date_2.year,birth_date_2.month,birth_date_2.day):
                years2=birth_date_2.year-birth_date.year
                if (birth_date_2.month,birth_date_2.day) < (birth_date.month,birth_date.day):
                    years2 -=1
                    days2=days_between_dates(birth_date_2.year-1, birth_date.month, birth_date.day, birth_date_2.month, birth_date_2.day)
                else:
                    days2=days_between_dates(birth_date_2.year, birth_date.month, birth_date.day, birth_date_2.month, birth_date_2.day)
                print("You are {} years and {} days older than {}".format(years2, days2, name_2))

            else:
                years2=birth_date.year-birth_date_2.year
                if (birth_date.month,birth_date.day) < (birth_date_2.month,birth_date_2.day):
                    years2 -=1
                    days2=days_between_dates(birth_date.year-1, birth_date_2.month, birth_date_2.day, birth_date.month, birth_date.day)
                else:
                    days2=days_between_dates(birth_date.year, birth_date_2.month, birth_date_2.day, birth_date.month, birth_date.day)
                print("{} is {} years and {} days older than you".format(name_2,years2, days2))
        
        break
    elif age_gap=="no":
        break
    else:
        print("Invalid input")
print("\nThank you very much for using this age calculator\n")

