def sum_of_num_digits(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num //= 10
    return sum


print(sum_of_num_digits(225))


def mult_of_num_digits(num):
    mult = 1
    while num != 0:
        mult *= num % 10
        num //= 10
    return mult


print(mult_of_num_digits(555))


def mult_of_float_digits(fl):
    mult = 1
    fl_str = str(fl).split(".")
    before_point = int(fl_str[0])
    after_point = int(fl_str[1])
    while before_point != 0:
        mult *= before_point % 10
        before_point //= 10
    while after_point != 0:
        mult *= after_point % 10
        after_point //= 10
    return mult


print(mult_of_float_digits(5.412))
