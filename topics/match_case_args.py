from enum import Enum

# before / positional args only, after * keyword args only, inbetween either

# def print_info(name, surname, /, age, *, occupation):
#     print(f"My name is {name} {surname}. I'm {age} years old and work as a(n) {occupation}.")

# print_info("Aylin", "Gyoren", age=27, occupation="software engineer")
# print_info("Aylin", "Gyoren", 27, occupation="software engineer")

# def answer_options(option: str) -> None:    # typing
#     match option:
#         case "yes" | "Yes" | "ya" | "Yeah" | "yeah":
#             print("Too positive")
#         case "no" | "No" | "nah":
#             print("Too negative")
#         case "dunno" | "I don't know":
#             print("Make up your mind already")
#         case _:
#             print("Am I talking to the wall?")
#
# answer_options("dunno")

# class Color(Enum):
#     RED = 'red'
#     BLUE = 'blue'
#     GREEN = 'green'
#
# color = Color(input("Type your color: "))
#
# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("You are green with envy.")
#     case Color.BLUE:
#         print("Not feeling blue, are you?")
#     case _:
#         print("Where's the right color?")     # ????????
