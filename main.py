import datetime as dt
import smtplib
import random

my_email = "place your email here"
my_password = "place your password here"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("place where email will be sent to here") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"subject:Monday Motivation\n\n{quote}")
