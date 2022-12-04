import time

# print(time.ctime(time.time()))  # ctime takes seconds n turns em into local date
# my_time = time.localtime()
# british_time = time.gmtime()
# print(time.strftime('%X', my_time))  # H:M:S
# print(time.strftime('%x %X', my_time))  # m/d/y H:M:S
# print(time.strftime('%d/%m/%Y, %H:%M', my_time))  # d/m/Y H:M
# print(my_time.tm_hour)

# time_string = '24 October, 2022'
# struct_time = time.strptime(time_string, '%d %B, %Y')  # 2nd arg same format as time string
# print(struct_time)

# input('Press Enter to start')
# start_time = time.monotonic()
# start_time = time.perf_counter()   # perf_counter is more lightweight n accurate
# for i in range(1000000):
#     x = i * i
# end_time = time.monotonic()
# end_time = time.perf_counter()
# print(end_time - start_time)

print(time.tzname)   # time constant, equal cuz dst is always 0
# better to use these two constants with local time
print(time.localtime().tm_zone)
print(time.localtime().tm_gmtoff / 60 / 60)  # to get bel time diff in hours
#
# time.sleep(2)
