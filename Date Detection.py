import re, calendar

dateDetection = re.compile(r"([0-2][0-9]|3[0-1])[/]([0][1-9]|1[0-2])[/]([1-2][0-9][0-9][0-9])")

def isDate(m):
    for word,number in shortMonth.items():
        if number == month:
            return word

a = dateDetection.search(" asdasdasd asda sdasd asdasdasd as 29/02/2019")

day = a.group(1)
month = a.group(2)
year = a.group(3)

shortMonth = {"April" : "04", "June" : "06", "September" : "09", "November" : "11"}

if month == "02" and day > "28" and not(calendar.isleap(int(year))):
    print("Found date: %s ,Invalid date, February has only 28 days in %s" % (a.group(),year))
elif month == "02" and day > "29" and calendar.isleap(int(year)):
    print("Found date: %s, Invalid date, February has only 29 days in the year of %s" % (a.group(),year))

elif month in shortMonth.values() and day > "30":
    print("Found date: %s it is not a valid date, %s has only 30 days!" %(a.group(), isDate(month)))

else:
    print("Found date: %s" % a.group())







