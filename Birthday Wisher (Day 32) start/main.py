# import smtplib
#
# my_email = "moonknight196@gmail.com"
# password = "qrqmazreuirftjlo"
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     # Securing connection TLS
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="phuc.223002@student.hactech.edu.vn",
#                         msg="Subject:Hello\n\nThis is the body of my email!")

# import re
#
# text = "The brown quick brown fox jumps over the lazy dog brown."
# pattern = r"brown"
#
# match = re.search(pattern, text)
# if match:
#     print("Found the pattern at index", match.start())
# else:
#     print("Pattern not found")

# initializing the data and an empty list
# data = [[1, 2, 3], [4, 5], [6, 7, 8, 9, 10]]
# flat_list = []
#
# # iterating over the data
# for item in data:
#     # appending elements to the flat_list
#     flat_list += item
#
# # printing the resultant flat_list
# print(flat_list)

from datetime import datetime
import random
import smtplib
import datetime as dt

my_email = "moonknight196@gmail.com"
password = "qrqmazreuirftjlo"
now = dt.datetime.now()
weekday = now.weekday()
# week_day = now.weekday()
# print(type(now))
# print(week_day)
if weekday == 1:
# today_date = datetime.today().strftime('%A')
# print(today_date)

# date_of_birth = dt.datetime(year=1996, month=7, day=27, hour=11)
# print(date_of_birth)

    with open("quotes.txt", mode="r") as file:
        all_quotes = file.readlines()
        random_quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="phuc.le.it96@gmail.com",
            msg=f"Subject: Quote of the Day\n\n{random_quote}"
        )
    print(random_quote)

