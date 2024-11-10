import smtplib
import datetime as dt
import random

from dateutil.rrule import weekday

my_email = "hackersiva847@gmail.com"
password = "ccnffohqpwivwijz"
Now = dt.datetime.now()
year = Now.year
month = Now.month
day_of_week = Now.weekday()

if day_of_week == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="sivam4266@gmail.com",
                                msg=f"subject:Your_today_quotes\n{quote}"
                                )
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


