def fibonacci_with_loop(n):
    prev, cur = 1, 1
    for i in range(n-2):
        prev, cur = cur, prev + cur
    return cur


print(fibonacci_with_loop(9))


def fibonacci_with_recursion(n):
    if n > 2:
        numb = fibonacci_with_recursion(n-1) + fibonacci_with_recursion(n - 2)
    else:
        numb = 1
    return numb


print(fibonacci_with_recursion(10))


def fibonacci_with_gen():
    prev, cur = 1, 1
    while True:
        yield prev
        prev, cur = cur, prev + cur


fib_gen = fibonacci_with_gen()

for num in range(9):
    print(fib_gen.__next__())


def fibonacci_list(n):
    prev, cur = 1, 1
    for i in range(n):
        yield prev
        prev, cur = cur, prev + cur


fib_list = list(fibonacci_list(9))
print(fib_list)
