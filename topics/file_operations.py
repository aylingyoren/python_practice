import shelve

# Shelve Module for Binary

# clothes = shelve.open("../shelve_dict/shelve_example1")
with shelve.open("shelve_dict/shelve_example") as clothes:
    # clothes["jeans"] = "Turkey"
    # clothes["blouse"] = "Belarus"
    # clothes["sweatshirt"] = "UK"
    # clothes["trousers"] = "Poland"

    # while True:
    #     key = input("Enter an item of clothes: ")
    #     if key == "quit" or key == "exit":
    #         break
    #     if key in clothes:
    #         country = clothes[key]
    #         print(country)
    #     else:
    #         print("There is no such item here")

    ordered_clothes_list = list(clothes.keys())
    ordered_clothes_list.sort()
    for key in ordered_clothes_list:
        print(key + ": " + clothes[key])

    # print(clothes.get("socks"))    # None if absent, w/o error

    # for key, value in clothes.items():
    #     print(key + ": " + value)

boarding_games = ["Uno", "Cards Against Humanity", "Taboo"]
cards = ["Poker"]

games = shelve.open("shelve_dict/shelve_example2")
games["boarding"] = boarding_games
games["cards"] = cards

new_cards = cards
new_cards.append("Durak")
games["cards"] = new_cards
print(list(games.items()))
games.close()

# import pickle

# Binary Data

# with open("../test_bytes.txt", "bw") as test_bytes:
#     for num in range(21):
#         test_bytes.write(bytes([num]))
#
# with open("../test_bytes.txt", "br") as test_bytes:
#     for num in test_bytes:
#         print(num)

# Pickle Module for Binary

# computer = (
#     "Apple",
#     "MacBook",
#     "Pro",
#     2020,
#     (
#         (1, "Aylin"),
#         (2, "Gyoren")
#     )
# )
#
# with open("../binary_mac.pickle", "wb") as binary_mac:
#     pickle.dump(computer, binary_mac)

# with open("../binary_mac.pickle", "rb") as binary_mac:
#     my_computer = pickle.load(binary_mac)
#
# brand, comp_type, model, year, owner_list = my_computer
# print(brand, comp_type, model, year, owner_list)

# Reading Files

# with open("test.txt", "r") as f:
#     line = f.readline()     # reading in stream
#     while line:
#         print(line, end="")
#         line = f.readline()

# with open("../test.txt") as f:
#     lines = f.readlines()
# for line in lines[::-1]:
#     print(line, end="")

# names = []

# with open("../names.txt", "r") as f:
#     for name in f:
#         names.append(name.strip("\n"))

# Writing Files

# with open("../names.txt", "a") as f:
#     print("Jill", file=f)
#     print("Joice", file=f)

# print(names)

# with open("../names.txt", "w") as f:
#     for name in names:
#         print(name, file=f)

# f = open("../names.txt", "w")
# for name in names:
#     f.write(name + "\n")
# f.close()
