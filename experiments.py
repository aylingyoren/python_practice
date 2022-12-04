import calendar
import json

py_dict = {'here': True, 'there': False, 'arr': ['my', 'array']}
dict_json = json.dumps(py_dict)
print(dict_json)
json_data = """ {
    "ID"       : 210450,
    "login"    : "admin",
    "name"     : "John Smith",
    "password" : "root",
    "phone"    : 5550505,
    "email"    : "smith@mail.com",
    "online"   : true
} """
back_to_py_dict = json.loads(json_data)
print(back_to_py_dict)

yy = 2022
mm = 10
print(calendar.month(yy, mm))

num_list = [1, 2, 3, 4, 5, 6]
# def get_max_element(arr):
#     max_el = 0
#     for i in arr:
#         if arr[i - 1] > max_el:
#             max_el = arr[i]
#     return max_el
# get_max_element(num_list)

start_str = 'Some string here'
new_str = start_str.replace(" ", "-", 2)   # last arg - replace number of times
print(new_str)

print(start_str.title())    # capitalize
# result_str = ''
# for i in range(0, len(start_str)):
#     if i != 3:
#         result_str += start_str[i]

# result_str = '.join([start_str[i] for i in range(0, len(start_str)) if i != 3])

reversed_str = ''
index = len(start_str)
while index > 0:
    reversed_str += start_str[index - 1]
    index -= 1

print(reversed_str)

nested_list = [[j for j in range(3)]for i in range(4)]
print(nested_list)

dict_1 = {'mobile': ['+375296584520', '+375336894623']}
dict_2 = {'occupation': 'dentist'}
dict_3 = dict_1.copy()
dict_3.update(dict_2)

# dict_3 = {**dict_1, **dict_2}
print(dict_3)

def is_palindrome(value):
    if value == value[::-1]:
        print("It's a palindrome")
        return True
    else:
        print("Not a palindrome")
is_palindrome('mom')

for index, value in enumerate(range(1, 11)):
    print(f'{index}. {value}')

bool_list = [True, False, True, True]
# bool_list = [True, True, True, True]
num_list = list(range(5))

if any(bool_list):
    print('At least one is true')
if all(bool_list):
    print('All are true')
if any(bool_list) and not all(bool_list):
    print('At least one is true and one is false')

def has_duplicates(lst):
    return len(lst) != len(set(lst))

print(has_duplicates(bool_list))
