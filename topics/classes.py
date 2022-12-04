# HW Class Attributes

# class BlogPost:
#     def __init__(self, user_name, text, number_of_likes):
#         self.user_name = user_name
#         self.text = text
#         self.number_of_likes = number_of_likes
#
# insta_post = BlogPost("vasyapupkin", "Hey, guys!", 23)
# fb_post = BlogPost("maryjane", "New song is out!", 2087)
# insta_post.number_of_likes = 102
# print(insta_post.number_of_likes)
# print(fb_post.number_of_likes)

# HW Class Methods

# class BankAccount:
#     def __init__(self, client_id, client_first_name, client_last_name):
#         self.client_id = client_id
#         self.client_first_name = client_first_name
#         self.client_last_name = client_last_name
#         self.balance = 0.0   #!!!!!
#
#     def add(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         self.balance -= amount
#
# bank_account_1 = BankAccount("27800g", "Aylin", "Gyoren")
# bank_account_2 = BankAccount("86290h", "Vasya", "Pupkin")
# bank_account_1.add(500)
# print(bank_account_1.balance)
# bank_account_2.add(20.20)
# bank_account_2.withdraw(0.20)
# print(bank_account_2.balance)

# class Circle:
#     pi = 3.14
#
#     def __init__(self, radius=1):
#         self.radius = radius
#
#     def get_area(self):
#         return self.pi * (self.radius ** 2)
#
#     def get_circumference(self):
#         return 2 * self.pi * self.radius
#
# my_circle = Circle(4)
# print(my_circle.get_area())
# print(my_circle.get_circumference())
# another_circle = Circle()
# print(another_circle.get_area())
# print(another_circle.get_circumference())

class Programmer:
    number_of_programmers = 0

    @classmethod
    def get_number_of_programmers(cls):
        return Programmer.number_of_programmers

    @classmethod    # static method if no attrs used
    def create_programmer_from_data(cls, data):
        data_array = data.split(', ')
        full_name, rank, work_experience = data_array[0:3]
        stack = data_array[3:]
        return cls(full_name, rank, work_experience, stack)

    def __init__(self, full_name, rank, work_experience, stack):
        self.full_name = full_name
        self.rank = rank
        self.work_experience = work_experience
        self.stack = stack
        Programmer.number_of_programmers += 1

    def get_full_name(self):
        return self.full_name

    def get_rank(self):
        return self.rank

    def get_work_experience(self):
        return self.work_experience

    def get_stack(self):
        return self.stack

    def get_promotion(self):
        if self.rank == "junior":
            self.rank = "middle"
        elif self.rank == "middle":
            self.rank = "senior"
        elif self.rank == "senior":
            self.rank = "lead"
        else:
            print("Let's evolve with new technologies")

    def resign_from_company(self):
        Programmer.number_of_programmers -= 1

# print(Programmer.get_number_of_programmers())
# aylin_programmer = Programmer("Ailin Hioren", "middle", 2, ["Javascript", "React", "TypeScript", "Redux", "Python"])
# print(Programmer.number_of_programmers)
# aylin_programmer.get_promotion()
# print(aylin_programmer.rank)
#
# alex_programmer = Programmer.create_programmer_from_data("Alex, junior, 0.5, C++")
# print(alex_programmer.stack)
# print(Programmer.number_of_programmers)

# Inheritance

class GoogleProgrammer(Programmer):
    def __init__(self, full_name, rank, work_experience, stack, period_of_work=0):
        # super().__init__(full_name, rank, work_experience, stack)
        Programmer.__init__(self, full_name, rank, work_experience, stack)
        self.period_of_work = period_of_work

    # Polymorphism - same method functions differently

    def get_stack(self):
        if isinstance(self.stack, list):  # type check!!!!!!!
            string_stack = ""
            for tech in self.stack:
                if tech == self.stack[-1]:
                    string_stack += f"{tech}"
                else:
                    string_stack += f"{tech}, "
            self.stack = string_stack
            return self.full_name + "'s stack includes " + self.stack
        else:
            return self.full_name + "'s stack includes " + str(self.stack)


pasha = GoogleProgrammer("Pasha Jork", "senior", 6, ["C", "C++"], 4)
sasha = GoogleProgrammer.create_programmer_from_data("Sasha, middle, 3, Python, Django, Flask")
print(sasha.get_stack())

# Polymorphism

# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         raise NotImplementedError("The speak method must be implemented")
#
# class Dog(Animal):
#     kind = "dog"
#     def __init__(self, name):
#         super().__init__(name)
#     def speak(self):
#         print(f"A {self.kind} is saying woof")
#
# class Cat(Animal):
#     kind = "cat"
#     def __init__(self, name):
#         super().__init__(name)
#     def speak(self):
#         print(f"A {self.kind} is saying meow")
#
# class Duck(Animal):
#     kind = "duck"
#     def __init__(self, name):
#         super().__init__(name)
#     def speak(self):
#         print(f"A {self.kind} is saying qwak")
#
# class Fish(Animal):
#     kind = "fish"
#     def __init__(self, name):
#         super().__init__(name)
#     def speak(self):
#         print(f"A {self.kind} is saying nothing")
#
# rex = Dog('Rex')
# tom = Cat('Tom')
# donald = Duck('Donald')
# nemo = Fish('Nemo')
#
# for pet in [rex, tom, donald, nemo]:
#     pet.speak()

# HW Class Inheritance & Polymorphism

# class GameCharacter:
#     def __init__(self, name, health, level):
#         self.name = name
#         self.health = health
#         self.level = level
#
#     def speak(self):
#         print(f"Hi, my name is {self.name}")
#
#
# class Villain(GameCharacter):
#     def __init__(self, name, health, level):
#         super().__init__(name, health, level)
#
#     def speak(self):
#         print(f"Hi, my name is {self.name} and I will kill you")
#
#     def kill(self, game_character):
#         game_character.health = 0
#         print("Bang-bang, now you're dead")
#
#
# gamer_1 = GameCharacter("Vasya", 4, 15)
# gamer_2 = GameCharacter("Katya", 5, 21)
# villain_1 = Villain("Horn", 5, 34)
#
# print(gamer_1.health)
# villain_1.kill(gamer_1)
# print(gamer_1.health)

# Operator Overloading w Special Method Names (allowing classes to define their own behavior)
#
# a = "5"
# b = "3"
#
# class Add:
#     def __init__(self, first_number):
#         self.first_number = first_number
#     def __add__(self, other):
#         if isinstance(self.first_number, str):
#             self.first_number = int(self.first_number)
#         if isinstance(other.first_number, str):
#             other.first_number = int(other.first_number)
#         return self.first_number + other.first_number
#
# number_1 = Add("2")
# number_2 = Add("3")
# print(number_1 + number_2)

# HW Special Method Names

# class Chain:
#     def __init__(self, number_of_items):
#         self.number_of_items = number_of_items
#
#     def __str__(self):
#         return f"Chain with {self.number_of_items} items"
#
#     def __len__(self):
#         return self.number_of_items
#
#
# my_chain = Chain(3)
# print(my_chain)
# print(len(my_chain))
