from collections import Counter, defaultdict, namedtuple
import re

# namedtuple

# jane = ("Jane", "Brown", 19, "female")
# jim = ("Jim", "Smith", 27, "male")

# Person = namedtuple("Person", ["name", "surname", "age", "sex"])
# Person = namedtuple("Person", "name surname age sex")
# Person = namedtuple("Person", "name, surname, age, sex")

# chris = ["Chris", "Hemsworth", 35, "male"]
# Person._make(chris)     # ??????
# print(chris)

# jim = Person(name="Jim", surname="Carry", age=44, sex="male")
# chris = Person("Chris", "Hemsworth", 35, "male")
# print(jim.name)
# jane = Person(name="Jane", surname="Brown", age=19, sex="female")
# print(jane)
# jane = jane._replace(surname="Davidson")
# print(jane)
# print(jane.__repr__())     # = print(jane)

# defaultdict

# my_dict = defaultdict(lambda: "Create me")

# def constant_factory(value):
#     return lambda: value
#
# my_dict = defaultdict(constant_factory("Create me"))    # constant function
# my_dict[1] = "Existing value"
# print(my_dict[3])    # returns default value (list, object, set, lambda)

string = "Mississippi"
default_dict = defaultdict(int)    # default int for counting
for key in string:
    default_dict[key] += 1
print(sorted(default_dict.items()))

list_of_tuples = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('red', 5), ('blue', 4)]
default_dict = defaultdict(set)    # set for building a dictionary of sets
for color, number in list_of_tuples:
    default_dict[color].add(number)
print(sorted(default_dict.items()))

# Counter

# number_list = [1, 1, 1, 3, 5, 5, 6, 6, 6, 6, 6]
# print(Counter(number_list))     # Counter({6: 5, 1: 3, 5: 2, 3: 1})

# words = "Hey, how are you doing, how are you, are you okay, you are tired, hey you"
# words_list = words.split(" ")
# counter_words = Counter(words_list)
# print(counter_words.most_common(3))

# words = re.findall(r"\w+", open("some_text.txt").read().lower())
# print(Counter(words).most_common(5))

# counter_numbers = Counter(number_list)
# print(sum(counter_numbers.values()))
# print(counter_numbers[7])   # no KeyError
# print(list(counter_numbers))
# counter_numbers = counter_numbers.items()
# print(Counter(dict(counter_numbers)))
# print(counter_numbers.most_common()[:-3-1:-1])
# new_counter = Counter(a=10, b=5, c=0, d=-2)
# print(sorted(new_counter.elements()))    # elements() ignores zero and negative counts
# counter_numbers.clear()
# print(counter_numbers)
