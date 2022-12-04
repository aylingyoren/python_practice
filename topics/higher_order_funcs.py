# Higher Order Functions

# def get_numbers_sqrt_multiplied(num, func):
#     result = 1
#     for i in range(1, num):
#         result *= func(i)
#     return result
#
# def num_sqrt(num):
#     return num ** 2
#
# numbers_multiplication = get_numbers_sqrt_multiplied(4, num_sqrt)     # use func as args
# print(numbers_multiplication)

# from random import choice

# def colorize(item):
#     def get_color():
#         colors = ["blue", "magenta", "cyan", "lilac"]
#         color = choice(colors)
#         return color
#     return get_color() + ' ' + item
#
# print(colorize("bag"))

# def colorize1():
#     def get_color():
#         colors = ["blue", "magenta", "cyan", "lilac"]
#         color = choice(colors)
#         return color
#     return get_color     # return func
#
# make_color = colorize1()
# print(make_color())

# def colorize2(item):
#     def get_color():
#         colors = ["blue", "magenta", "cyan", "lilac"]
#         color = choice(colors)
#         return color + ' ' + item     # inner func accessed outer func scope
#     return get_color
#
# print(colorize2('cat')())
# colorized_phone = colorize2('phone')
# print(colorized_phone())
