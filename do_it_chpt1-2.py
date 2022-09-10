
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
    

# Exercise 1-10
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

