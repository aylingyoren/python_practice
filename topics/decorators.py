from functools import wraps
from time import time, sleep

# Speed decorator

# def calculate_processing_time(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time()
#         func(*args, **kwargs)
#         return time() - start_time
#     return wrapper
#
#
# @calculate_processing_time
# def sum_with_list(range_value):
#     return sum([num for num in range(range_value)])
#
# print(sum_with_list(100000000))
#
#
# @calculate_processing_time
# def sum_with_gen(range_value):
#     return sum(num for num in range(range_value))
#
# print(sum_with_gen(100000000))


# HW Hello from decorator

# def hello_from_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         hello = " Hello from decorator!"
#         return str(result) + hello
#     return wrapper

# Metadata decorator

# def print_func_metadata(func):
#     @wraps(func)     # allows us to save func's metadata
#     def wrapper(*args, **kwargs):
#         print(f"Function name is {func.__name__}")
#         print(f"Function documentation: \n{func.__doc__}")
#         return func(*args, **kwargs)
#     return wrapper

# @print_func_metadata
# def cubes_sum(*args):
#     """
#     :param args: numbers
#     :return: sum of cubes of numbers
#     """
#     result = 0
#     for num in args:
#         num **= 3
#         result += num
#     print(result)
#     return result
#
# cubes_sum(2, 3)
# print(cubes_sum.__name__)
# print(cubes_sum.__doc__)

# HW Decorating func metadata

# def print_args(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Function arguments: {args}")
#         print(f"Function key-word arguments: {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper


# @print_args
# def cubes_average(*args):
#     """
#     :param args: numbers
#     :return: float which is average of number cubes
#     """
#     result = 0
#     for num in args:
#         num **= 3
#         result += num
#     print(result / len(args))
#     return result / len(args)
#
# cubes_average(2, 3, 4)
#

# Control function behavior

# def prohibit_integer_args(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         for val in args:
#             if type(val) == int:
#                 raise ValueError("Integers are prohibited")
#         for key, val in kwargs.items():
#             if type(val) == int:
#                 raise ValueError("Integers are prohibited")
#         return func(*args, **kwargs)
#     return wrapper

# HW Prohibit 2+ args

# def prohibit_more_than_2_args(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if len(args) > 2:
#             raise ValueError("Function must have less than 3 arguments!")
#         # if len(kwargs) > 2:
#         #     raise ValueError("Function must have less than 3 arguments!")
#         return func(*args, **kwargs)
#     return wrapper
#
# @prohibit_more_than_2_args
# def introduce_yourself(name, age):
#     return f"My name is {name}. I'm {age} years old"
#
# print(introduce_yourself("Aylin", 27))

# Decorators with their own args

# def check_if_first_arg_is(val):
#     def inner_decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             if args and args[0] == val:
#                 return func(*args, **kwargs)
#             # if kwargs:     # just checked if key == val in kwargs
#             #     for key in kwargs:
#             #         if kwargs[key] == val:
#             #             return func(*args, **kwargs)
#             #         else:
#             #             raise ValueError(f"First keyword argument must be {val}")
#             else:
#                 raise ValueError(f"First (keyword) argument must be {val}")
#         return wrapper
#     return inner_decorator

# Enforce types

# def enforce(*types):
#     def inner_dec(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             new_args = []
#             for a, t in zip(args, types):
#                 new_args.append(t(a))
#             return func(*new_args, **kwargs)
#         return wrapper
#     return inner_dec
#
# @enforce(int, int)
# def divide(a, b):
#     return a / b
#
# print(divide("9", "3"))

# HW Wait decorator

# wait задерживает выполнение кода функции, которую она декорирует,
# на n секунд. Аргумент n должен передаваться в декоратор.
# Воспользуйтесь функцией для задержки выполнения кода.
# Найдите информацию об использовании этой функции в интернете самостоятельно.
# Также после задержки должно выводится сообщение
# "There was a pause {количество секунд} seconds before execution {имя задекорированной функции }"

# def wait(seconds):
#     def inner_dec(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             sleep(seconds)
#             print(f"There was a pause {seconds} seconds before execution {func.__name__}")
#             return func(*args, **kwargs)
#         return wrapper
#     return inner_dec


#
# def make_compliments(func):
#     def wrapper(*args, **kwargs):
#         print("You look lovely!")
#         func(*args, **kwargs)
#         print("I admire your courage!")
#     return wrapper
#
#
# @make_compliments
# @hello_from_decorator
# @prohibit_integer_args
# @check_if_first_arg_is("Aylin")
# @wait(5)
# def introduce_yourself(name):
#     return f"My name is {name}."
#
# print(introduce_yourself("Aylin"))
