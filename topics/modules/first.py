def first_func_1():
    print("first_func_1")


def first_func_2():
    print("first_func_2")


if __name__ == "__main__":    # check if we run first module
    first_func_1()
    first_func_2()
else:
    print("First is imported")