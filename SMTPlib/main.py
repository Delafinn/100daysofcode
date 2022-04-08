'''building a basic quote emailer.'''
import smtplib
import datetime as dt
import random

# creating the connection to email
MY_EMAIL = "youremailaddress@email.com"
PASSWORD1 = "yourpassword here"

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





with open("quotes.txt") as data:
    data_lines = data.readlines()
    rquote = random.choice(data_lines)
    print(rquote)

if weekday == 1:
    with smtplib.SMTP("smtp.gmail.com",port = 587) as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password = PASSWORD1)
        connection.sendmail(from_addr = MY_EMAIL,to_addrs = "other_email@email.com", msg = f"Subject:Monday Quotes!\n\n {rquote}. ")
        connection.close()
