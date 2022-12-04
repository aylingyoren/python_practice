import pytz
from datetime import datetime, date, timedelta

# UTC n then turn it into local time

# class datetime

# minsk = 'Europe/Minsk'
# tz_minsk = pytz.timezone(minsk)
# minsk_time = datetime.now(tz=tz_minsk)
# print(minsk_time)   # 2022-10-24 22:56:00.345411+03:00

# for tz in pytz.all_timezones:
#     print(tz)

# for country in pytz.country_names:
#     print(country, pytz.country_names[country], pytz.country_timezones.get(country))
    # if country in pytz.country_timezones:
    #     print(pytz.country_timezones[country])   # OR ^^

my_country_names = ['BY', 'PL', 'TR', 'AE', 'AM', 'TJ', 'TC']
for c in my_country_names:
    country = pytz.country_names[c]
    tz = pytz.country_timezones.get(c)[0]
    country_tuple = (country, tz)
    print(c, country_tuple)

while True:
    my_input = input('Please enter a two-letter code to choose the timezone or "q" to exit: ')
    if my_input == 'q':
        break
    my_tz = pytz.timezone(pytz.country_timezones.get(my_input)[0])
    my_time = datetime.now(my_tz)
    print(f'Local time: {my_time}')
    print(f'UTC time: {datetime.utcnow()}')

# today = datetime.today()
# hours = today.hour
# if hours <= 9:
#     hours = "0" + str(hours)
# minutes = today.minute
# if minutes <= 9:
#     minutes = "0" + str(minutes)
# print(f"{hours}:{minutes}")

# timestamp = today.timestamp()
# print(timestamp)
# today_from_timestamp = datetime.fromtimestamp(timestamp)
# print(today_from_timestamp)
# print(today.strftime('%A, %d %B, %Y'))
# print(today.isocalendar())   # datetime.IsoCalendarDate(year=2022, week=43, weekday=1)
# print(today.isoformat())

# class date

# today = date.today()
# my_birthday = date(today.year, 11, 21)
# if my_birthday < today:
#     my_birthday = my_birthday.replace(year=today.year + 1)
# print(my_birthday)
# days_until_bday = my_birthday - today
# print(f'Days until b-day: {days_until_bday.days}')

# Get weekday app
#
# my_year = int(input('Enter your year: '))
# my_month = int(input('Enter your month: '))
# my_day = int(input('Enter your day: '))
#
# weekdays = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
# my_date = date(my_year, my_month, my_day)
# week_day = my_date.isoweekday()
# match week_day:
#     case 1: week_day = weekdays[1]
#     case 2: week_day = weekdays[2]
#     case 3: week_day = weekdays[3]
#     case 4: week_day = weekdays[4]
#     case 5: week_day = weekdays[5]
#     case 6: week_day = weekdays[6]
#     case 7: week_day = weekdays[7]
#
# print(f'{my_date} is {week_day}')

# class timedelta

# year = timedelta(days=365)
# leap_year = timedelta(days=366)
# today = datetime.now()
# # print(year)
# # print(f'25 days from today will be {today + timedelta(days=25)}')
# last_birthday = datetime(2021, 11, 21)
# print(f'My last b-day was {(today - last_birthday).days} days ago')
# print(f'A regular year has {year.total_seconds()} seconds and a leap year has {leap_year.total_seconds()} seconds')
# print(f'There are {(year * 7).days} in 7 regular years and {(leap_year * 7).days} in 7 leap years')
