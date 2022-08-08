"""
Create a Least Common Multiple algorithm from scratch.
This solution uses the an adaptation of the Euclidean Algorithm.
"""

from math import prod
from typing import Callable


def any_multiples(*sample: int) -> Callable[[int], bool]:
    """
    Takes a list of numbers and returns a closure that tells if any number has multiples in the original list
    """

    def closure(n: int) -> bool:
        for i in filter(lambda x: x != n, sample):
            if i % n == 0:
                return False
        return True

    return closure


def gcd(*args: int) -> int:
    # Possible performance considerations:
    # - Check if any number or the smallest one is prime and return 1
    # - First check the smallest number, then start the loop at half it

    # The GCD will never be greater than the smallest number of the list
    for i in reversed(range(1, min(args) + 1)):
        # If `n` can divide all numbers in `args`, return it
        if all(n % i == 0 for n in args):
            return i

    return 1  # Just to please the linter


def lcm(*args: int) -> int:
    # Filter out zeroes -> 0 is divisible by anything and causes trouble
    # Remove negative numbers -> cause weird behavior and divide the same
    # Remove duplicates -> will inflate the result
    nums = set(abs(n) for n in filter(lambda n: n != 0, args))

    # Filter out numbers that have their multiples already in the list
    # Ex: [4, 6, 16] -> [6, 16] because every multiple of 16 is a multiple of 4
    nums = list(filter(any_multiples(*nums), nums))

    # The Euclidean Algorithm
    return abs(prod(set(nums))) // gcd(*nums)


if __name__ == "__main__":
    print(lcm(8, 6, 4, 2))
    print(lcm(6, 8, 4, 6, 4, 0, 4))
    print(lcm(6, 8, -4, -6, 4))
