# Generator Function

# def my_gen_func(end):
#     count = 1
#     while count <= end:
#         yield count
#         count += 1
#
#
# my_gen = my_gen_func(5)
# for num in my_gen:
#     print(num)
#
# my_gen.__next__()
# print(my_gen.__next__())
# next(my_gen)
# print(next(my_gen))

# HW Generator Functions

# def get_week_day():
#     yield "Sunday"
#     yield "Monday"
#     yield "Tuesday"
#     yield "Wednesday"
#     yield "Thursday"
#     yield "Friday"
#     yield "Saturday"

# def get_week_day():
#     days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     for day in days_of_week:
#         yield day

# days = list(get_week_day())
# print(days)
#
# current_day = get_week_day()
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())

# def even_odd():
#     count = 1
#     while True:
#         if count % 2 == 0:
#             yield "even"
#         else:
#             yield "odd"
#         count += 1
#
# def even_odd():
#     value = "odd"
#     while True:
#         yield value
#         if value == "odd":
#             yield "even"
#         else:
#             yield value
#
# even_odd_generator = even_odd()
# print(next(even_odd_generator))
# print(next(even_odd_generator))
# print(next(even_odd_generator))
# print(next(even_odd_generator))
# print(next(even_odd_generator))
# print(next(even_odd_generator))

# Infinite Generator
#
# def infinite_week():
#     days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     i = 0
#     while True:
#         if i >= len(days_of_week):
#             i = 0
#         yield days_of_week[i]
#         i += 1
#
# next_day = infinite_week()
# print(next_day.__next__())
# print(next_day.__next__())
# print(next_day.__next__())
# print(next_day.__next__())
# print(next_day.__next__())
# print(next_day.__next__())
# print(next_day.__next__())
# print(next_day.__next__())
# print(next_day.__next__())

# HW Infinite Generator

# def get_infinite_square_generator():
#     number = 1
#     while True:
#         yield number ** 2
#         number += 1

# Generator Expression
#
# infinite_square_generator = get_infinite_square_generator()
# print(next(infinite_square_generator))
# print(next(infinite_square_generator))
# print(next(infinite_square_generator))
# print(next(infinite_square_generator))
# print(next(infinite_square_generator))

# counter = (num for num in range(10))
# print(counter)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# print(sum(counter))   # gen is lighter than list

# List & Gen Exp Comparison

# from time import time
#
# list_start_time = time()
# print(sum([num for num in range(1000000000)]))
# list_finish_time = time() - list_start_time  # ~ 226.76 sec
#
# gen_start_time = time()
# print(sum(num for num in range(1000000000)))
# gen_finish_time = time() - gen_start_time  # ~ 42.07 sec
