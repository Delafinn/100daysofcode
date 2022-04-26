age = input("What is your current age?")
totdays = 32850 # total days in 90 years
totweeks = 4680  # total weeks in 90 years
totmonths = 1080  # total months in 90 years

agendays = 365 * int(age)
agenweeks = 52 * int(age)
agenmonths = 12 * int(age)

x = totdays - agendays
y = totweeks - agenweeks
z = totmonths - agenmonths



print(f"You have " + str(x) + " days, " + str(y) + "weeks, and " + str(z) + " months left. until you are 90.")

print("press any key to exit")


# now ask the user their birthday to calculate the exact amount of days, weeks, months they have till 90.
