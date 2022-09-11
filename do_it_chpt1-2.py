
import math

# Exercise 1-7
def sum_of_nn(n):
    """Using while loop, return the sum of the first n positive integers."""
    total_sum = 0
    i = 1

    while i <= n:
        total_sum += i
        i += 1

    print(f'The sum of the first {n} positive integers is {total_sum}.')

    return total_sum


# Exercise 1-8
def sum_of_nn2(n):
    """Using for loop, Return the sum of the first n positive integers."""
    total_sum = 0

    for i in range(1, n+1):
        total_sum += i

    print(f'The sum of the first {n} positive integers is {total_sum}.')

    return total_sum


# Exercise 1-9
def sum_of_nn_bw(n1, n2):
    """Using for loop, return the sum of the integers between n1 and n2."""
    total_sum = 0

    if n1 == n2:
        raise ValueError('n1 and n2 must be different.')
    elif n1 > n2:
        n1, n2 = n2, n1

    for i in range(n1, n2+1):
        total_sum += i

    print(f'The sum of the integers between {n1} and {n2} is {total_sum}.')

    return total_sum


# [GitHub Copilot] Make a function that returns the sum of the integers between n1 and n2
def sum_of_nn_bw_copilot(n1, n2):
    """Return the sum of the integers between n1 and n2."""
    if n1 > n2: n1, n2 = n2, n1

    total_sum = 0

    for i in range(n1, n2 + 1):
        total_sum += i

    return total_sum
    

# Exercise 1-10, 11
def sum_of_nn_bw2(n1, n2):
    """Using while loop, return the sum of the integers between n1 and n2."""
    total_sum = 0

    if n1 == n2:
        raise ValueError('n1 and n2 must be different.')
    elif n1 > n2:
        n1, n2 = n2, n1

    for i in range(n1, n2):
        print(f'{i} + ', end='')
        total_sum += i
    
    total_sum += n2
    print(f'{n2} = {total_sum}', end='')

    return total_sum


# Exercise 1-12, 13
def print_alt_sign(n):
    
    for _ in range(n//2):
        print('+-', end='')

    if n % 2:
        print('+', end='')


# Exercise 1-14, 15
def make_star_block(n, w):
    star_line = '*' * w
    
    for _ in range(0, n//w):
        print(star_line)
    
    if n % w:
        print('*' * (n % w))


# Exercise 1-16
while True:
    n = int(input('Pick a natural number: '))
    if (isinstance(n, int)) and (n > 0):
        break
    print('Try again')

print(f'You chose {n} as your input.')


# Exercise 1-17
def square_potential_edge(area):
    for i in range(1, int(math.sqrt(area)) + 1):
        if area % i == 0:
            print(f'{i} x {area//i} = {area}')


def square_potential_edge2(area):
    for i in range(1, area + 1):
        
        if i ** 2 > area:
            break

        if area % i:
            continue

        print(f'{i} x {area//i} = {area}')

square_potential_edge2(9)


# Exercise 1-21
def print_gugudan():
    print('*' * 27)
    for i in range(1, 10):
        for j in range(1, 10):
            print(f'{i * j:<3}', end = '')
        print()
    print('*' * 27)


n = 17
id(17)
id(n)
b = 17
id(b)

# ?
id(7410)
n = 7410
id(n)
id(7410)

# In your case, Python, IIRC, the issue is that the compiler builds
# a few useful integer constants as singletons, (from -1 to 100 or so).
# The rationale is that these numbers are used so frequently that
# it makes no sense to dynamically allocate them each time they are
# needed, they are simply reused ... Python documentation explains
# it quite plainly: "The current implementation keeps an array of
# integer objects for all integers between -5 and 256,
# when you create an int in that range you actually just get back
# a reference to the existing object. "

id(3)
n = 3
id(n)
