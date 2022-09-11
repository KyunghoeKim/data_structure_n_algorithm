
from typing import Any, Sequence

x = [1, 2, 3]
if x:
    print("Here!")

y = []
if y:
    print("Here!")


# Exercise 2-2
def max_of(a: Sequence) -> Any:
    """Returns the maximum element from a sequence."""
    maximum = a[0]

    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    
    return maximum
