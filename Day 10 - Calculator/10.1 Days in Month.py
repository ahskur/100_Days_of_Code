def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1 :
        return "Invalid input."
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Let's check if it's a leap year first using true of false from the returns above
# So if the is_leap is True, then the function goes forward, if not, it just stops
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







