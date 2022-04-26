'''building a basic quote emailer.'''
import smtplib
import datetime as dt
import random

# creating the connection to email
MY_EMAIL = "youremailaddress@email.com"
PASSWORD1 = "yourpassword here"

# pulling the date time for now
now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
print(now)

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
