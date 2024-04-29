import datetime as dt
import smtplib
import random

now = dt.datetime.now()
day = now.weekday()
my_email = "Elderhorror@outlook.com"
password = "Prekunmi1@"

if day == 2:
    with open(file="quotes.txt") as text:
        quote = random.choice(text.readlines())

    with smtplib.SMTP("smtp.office365.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
                    from_addr=my_email,
                    to_addrs="adebayoadedeji413@gmail.com",
                    msg=f"Subject: Have a quote today\n\n {quote}"
            )



# now = dt.datetime.now()
# year = now.year
# month = now.month
# print(type(now))
#
# date_of_birth = dt.datetime(year=2005, month=2, day=19, hour=4)
# print(date_of_birth)
