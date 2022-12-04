def get_rainbow_color(color_number):
    color_number_list = list(range(1, 8))

    if type(color_number) is not int:
        raise TypeError("Color number should be integer")
    if color_number not in color_number_list:
        raise ValueError("Color number should be from 1 to 7")

    rainbow_colors = {
        1: "red",
        2: "orange",
        3: "yellow",
        4: "green",
        5: "blue",
        6: "navy blue",
        7: "purple"
    }

    if color_number in rainbow_colors.keys():
        print(rainbow_colors[color_number])

get_rainbow_color(5)

try:
    print({"name": "Aylin"}["last_name"])
    print([1, 2][2])
    print(int("hi"))
    print(f)
    print(len(5))
except TypeError:
    print("Something's wrong with your types")
except NameError:
    print("Does your value even exist")
except ValueError:
    print("Be careful with your values")
except IndexError:
    print("Where's that index of yours anyway?")
except KeyError:
    print("Check that key, buddy")


def divide(a, b):
    try:
        print(a / b)
    except TypeError as error:
        print("a and b must be numbers")
        print(error)
    except ZeroDivisionError:
        print("You can\'t divide by 0")
    else:
        print("Division was successful")
    finally:
        print("End of operation")


divide(1, 1)