import pandas
import datetime
from datetime import timedelta
import smtplib
import sys


def number_of_classes(dictionary):
    num = 0
    for item in dictionary:
        if dictionary[item] != 'x' and dictionary[item] != 'Lunch':
            num += 1
    return num - 1


def first_class_time(dictionary):
    for item in dictionary:
        days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
        if dictionary[item] not in days and dictionary[item] != 'x' and dictionary[item] != 'Lunch':
            return item


email = 'your email'
password = 'password for this app thru gmail'
df = pandas.read_csv("./data/Timetable.csv")


today = datetime.datetime.now()
time_now = today.strftime('%H:%M')
today_10 = datetime.datetime.now() + timedelta(minutes=10)
time_now_10 = today_10.strftime('%H:%M')


day_name = today.strftime('%A')[0:3].upper()

if day_name == 'SUN':
    sys.exit()

today_schedule = df[df['Day'] == day_name].to_dict(orient="records")[0]

if time_now == '7:30':
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        subject = "First Class Alert"
        message = f'Subject:{subject}\n\n Total Classes: {number_of_classes(today_schedule)} || \n Time: {first_class_time(today_schedule)}'
        connection.sendmail(from_addr=email, to_addrs="reviever", msg=message)


try:
    if today_schedule[time_now_10] != 'x':
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            subject = "Class Alert"
            connection.login(user=email, password=password)
            message = f'Subject{subject}\n\n Upcoming class is: {today_schedule[time_now_10]}'
            connection.sendmail(from_addr=email, to_addrs="filcraze26@gmail.com", msg=message)
except KeyError:
    pass
















