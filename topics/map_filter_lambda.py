# def double(num):
#     return num * 2


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# double_list = list(map(double, digits))
# result = map(double, digits)
# for num in result:
# for num in map(double, digits):
#     double_list.append(num)
# print(double_list)


# def is_number_even(num):
#     return num % 2 == 0
#
#
# even_numbers = list(filter(is_number_even, digits))

print(list(map(lambda num: num * 2, digits)))
print(list(filter(lambda string: "o" in string, ["hola", "hey", "ho-ho", "hi", "hell", "ouch", "oops"])))

list_of_tuples = [('red', 5), ('blue', 2), ('green', 4), ('yellow', 1), ('white', 3), ('orange', 7), ('hazel', 6)]
list_of_tuples.sort(key=lambda item: item[1])  # sort acc. to numbers
list_of_tuples.sort(key=lambda item: item[0])  # sort acc. to colors
print(list_of_tuples)

