from datetime import datetime
import pandas
import random
import smtplib
my_email = "hackersiva847@gmail.com"
password = "ccnffohqpwivwijz"
today = datetime.now()
today_tuple = (today.month, today.day)

file = open("../birthdays.csv")
Data = pandas.read_csv(file)
Birth_day_Dict = {(data_row["month"] , data_row["day"]): data_row for (index, data_row) in Data.iterrows()}

if today_tuple in Birth_day_Dict:
    birthday_person = Birth_day_Dict[today_tuple]
    file_path = f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as New_file:
        New_Data = New_file.read()
        New_Data = New_Data.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port= 587) as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"subject: Happy Birthday!\n\n{New_Data}"
                            )
