val = "Hello"

def spanish_greeting():
    val = "Hola"
    print(val)
    def turkish_greeting():
        val = "Selam"
        # nonlocal val
        # val = "Hey"
        # global val
        print(val)
        def german_greeting():
            val = "Hallo"
            # nonlocal val
            print(val)
        german_greeting()
    turkish_greeting()

spanish_greeting()
print(val)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# HW Functions

# def odd_number_sequence(a, b):
#     start_list = list(range(a, b + 1))
#     new_list = [num for num in start_list if num % 2 != 0]
#     return new_list

# def odd_number_sequence(a, b):
#     start_list = list(range(a, b + 1))
#     new_list = []
#     for num in start_list:
#         if num % 2 != 0:
#             new_list.append(num)
#     return new_list

# *args & **kwargs

# def calculate_percentage_of_multiplied_numbers(percent, *args):
#     result = 1
#     for numb in args:
#         result *= numb
#     return result / 100 * percent
#

# print(calculate_percentage_of_multiplied_numbers(10, 2, 5, 6))

# HW *args & **kwargs

# def is_cat_here(*args):
#     for arg in args:
#         if str(arg).lower() == "cat":
#             return True
#         else:
#             return False

# def is_item_here(item, *args):
#     return item in args

# def your_favorite_color(my_color, **kwargs):
#     if "color" in kwargs:
#         return "My favorite color is {0}, but {1} is also pretty good!".format(my_color, kwargs["color"])
#     else:
#         return f"My favorite color is {my_color}, what is your favorite color?"

