def odd(n):
    return 3 * n + 1


def even(n):
    return n / 2


def step(n):
    if n % 2 == 1:
        return odd(n)
    else:
        return even(n)


def collatz(n):
    count = 0
    print(count, n)
    while n != 1:
        count += 1
        n = step(n)
        print(count, n)
    return n


collatz(1000000)
