def get_odd_or_even_numbers():
    while True:
        try:
            number = int(input("Enter any number: "))
            if number == 0:
                print("We've got a zero")
                continue
            elif number % 2 == 0:
                print("Your number is even")
            else:
                print("Your number is odd")
            continue
        except:
            print("Wrong number format")
            break


get_odd_or_even_numbers()