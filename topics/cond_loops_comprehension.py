reg_list = []
nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in nested_lists:
    for number in row:
        # print(f"| {number} |", end="__")
        reg_list.append(number)

reg_list.insert(0, 0)
updated_reg_list = ["zero" if num == 0 else f"odd {num}" if num % 2 != 0 else f"even {num}" for num in reg_list]

bel_dict = {"country": "Belarus", "year": 1991, "capital": "Minsk", "number of regions": 6}
sells = {"marketing": 298, "IT": 507, "retail": 326, "education": 64}
updated_bel_dict = {key: (str(value).upper()) for key, value in bel_dict.items()}
doubled_sells = {key: value * 2 if value > 100 else value for key, value in sells.items()}

default_set = set(reg_list)
updated_default_set = {num * 2 for num in default_set}

# HW Conditionals

# entered_int = int(input('Enter any number: '))
# if entered_int == 7:
#     print('7 is a lucky number! Today is your lucky day!')
# else:
#     print('Thank you! Have a nice day!')

# While Loop

# entered_num = int(input('Enter an integer number: '))
# if entered_num % 2 == 0:
#     print('The number is even')
# else:
#     print('The number is odd')

# while True:
#     if entered_num % 2 == 0:
#         print('The number is even')
#     elif entered_num == 0:
#         print('Time to exit the loop')
#         break
#     else:
#         print('The number is odd')

# HW For Loop

# range_list = []
# sum_of_even_numbers = 0
# for num in range(10, 31):
#     if num % 2 == 0:
#         sum_of_even_numbers += num
#         range_list.append(num)
# print(sum_of_even_numbers)
# print(sum(range_list))
#
# number_of_hello = int(input("Enter any number"))
# for _ in range(number_of_hello):
#     print("Hello")

# List Comprehension

# greetings = ['hello', 'hi', 'hey', 'hola']
# list_with_second_letters = []
# for word in greetings:
#     list_with_second_letters.append(word[1])
# list_with_second_letters = [word[1] for word in greetings]
# print(list_with_second_letters)

# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# odd_digits = []
# for digit in digits:
#     if digit % 2 != 0:
#         odd_digits.append(digit)
# odd_digits = [digit for digit in digits if digit % 2 != 0]
# print(odd_digits)
