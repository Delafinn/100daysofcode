import smtplib
import datetime as dt
import random

# creating the connection to email
my_email = "youremailaddress@email.com"
password1 = "yourpassword here"

# pulling the date time for now
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
weekday = now.weekday()
print(year)
print(month)
print(day)
print(weekday)
print(now)

#creating a date time from scratch
date_of_birth = dt.datetime(year = 12, month =12 , day =12, hour = 4)
print(date_of_birth)



## TODO: open the quotes file as a dictionary

with open("quotes.txt") as data:
    data_lines = data.readlines()
    rquote = random.choice(data_lines)
    print(rquote)

## TODO: if the day is monday send a random quote from the quotes.txt
if weekday == 1:
    with smtplib.SMTP("smtp.gmail.com",port = 587) as connection:
        connection.starttls()
        connection.login(user = my_email, password = password1)
        connection.sendmail(from_addr = my_email,to_addrs = "other_email@email.com", msg = f"Subject:Monday Quotes!\n\n {rquote}. ")
        connection.close()
