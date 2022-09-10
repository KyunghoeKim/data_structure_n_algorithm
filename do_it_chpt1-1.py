
from random import randint

# Exercise 1-1
n1, n2, n3 = [int(i) for i in input("Enter three integers: ").split(", ")]
maximum = n1

if n2 > maximum:
    maximum = n2

if n3 > maximum:
    maximum = n3

print(f'The maximum value is {maximum}.')


# Exercise 1-2
def max_three_num(n1, n2, n3):
    """Find maximum among three numbers"""
    maximum = n1
    if n2 > maximum: maximum = n2
    if n3 > maximum: maximum = n3
    
    return maximum

help(max_three_num)

print(f'max_three_num(2, 100, 37) = {max_three_num(2, 100, 37)}')
print(f'max_three_num(1, 8, 12) = {max_three_num(1, 8, 12)}')
print(f'max_three_num(2, 3, 3) = {max_three_num(2, 3, 3)}')


# Exercise 1C-2
def median_three_num(input_list):
    """Return the median of three numbers.
    
    Input arguments:
    input_list -- list of length 3

    Returns a scalar value.
    """
    n1, n2, n3 = [int(elem) for elem in input_list]
    if n1 >= n2:
        if n2 >= n3: return n2
        elif n1 >= n3: return n3
        else: return n1
    elif n3 >= n2: return n2
    elif n3 >= n1: return n3
    else: return n1

# [GitHub Copilot] Make a function that returns the median of three numbers
def median_copilot(n1, n2, n3):
    """Return the median of three numbers."""
    if n1 >= n2:
        if n2 >= n3: return n2
        elif n1 >= n3: return n3
        else: return n1
    elif n1 > n3: return n1
    elif n2 > n3: return n3
    else: return n2

def check_median():
    for idx in range(100):
        n1, n2, n3 = [randint(1, 9) for _ in range(3)]
        # print(f'median_three_num([{n1}, {n2}, {n3}]) = {median_three_num([n1, n2, n3])}')
        if median_three_num([n1, n2, n3]) == median_copilot(n1, n2, n3):
            if (idx + 1) % 10 == 0: print(f'({idx + 1}/100)')
        else:
            print('ERROR: The results are not equal.')
            break

# Exercise 1-3
def check_sign(n):
    if n > 0: print(f'{n} is positive.')
    elif n < 0: print(f'{n} is negative.')
    else: print(f'{n} is zero.')

for _ in range(20):
    check_sign(randint(-3, 3))

