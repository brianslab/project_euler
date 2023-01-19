#!/usr/bin/python3

import math


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def get_largest_prime_factor(num):
    prime_factors = []
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factor = i
            if is_prime(factor):
                prime_factors.append(factor)

    return max(prime_factors)


answer = get_largest_prime_factor(600851475143)
print(answer)
