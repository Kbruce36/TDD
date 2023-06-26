# Kamugisha Bruce And Dennis Emmanuel


# define a loop function for finding factorial
def factorial_1(m):
    result = 1
    for i in range(1, m + 1):
        result = result * i
    return result


# define a recursion function for finding factorial
def factorial_2(n):
    if n == 0:
        return 1
    else:
        return n * factorial_2(n - 1)
