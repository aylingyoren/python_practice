number_list = list(range(1, 11))

# OOP Iterator

# class Count:
#     def __init__(self, start=0):
#         self.num = start
#     def __iter__(self):
#         return self
#     def __next__(self):
#         num = self.num
#         self.num += 1
#         return num
#
# counter = Count()
# print(counter.__next__())
# print(counter.__next__())

# class IterBackwards:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration("Out of range")
#         self.index -= 1
#         return self.data[self.index]
#
# data_backwards = IterBackwards("turn me around")
# for l in data_backwards:
#     print(l)

def reverse_data(data):
    for index in range(len(data) - 1, - 1, - 1):
        yield data[index]
for char in reverse_data("loral"):
    print(char)

# number_list_iterator = iter(number_list)

# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())

# print(next(number_list_iterator))

# for num in number_list_iterator:
#     print(num, end="..")

# Custom For Loop

# def my_for_loop(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator.__next__(), end="__")
#         except StopIteration:
#             print("\nIteration is completed")
#             break
#
# my_for_loop(number_list)

# Custom Iterable
#
# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.current = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current <= self.end:
#             number = self.current
#             self.current += 1
#             return number
#         else:
#             raise StopIteration
#
# my_range = MyRange(1, 10)
# for num in my_range:
#     print(num)
