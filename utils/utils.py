import math


def prime_sieve(n):
    """
    Generate all the prime numbers up to n
    :param n: The ceiling for the prime number search
    :return: A list containing n elements, with False in positions that aren't prime numbers and True in those that are
    """
    primes = [True] * n
    primes[:2] = [False, False]
    if n >= 4:
        for y in range(4, n, 2):
            primes[y] = False
    for x in range(3, int(math.ceil(n / 2.0)), 2):
        for i in range(x * x, n, x):  # You don't need to do x + x as 2 * x will be covered by 2, and so on for multiples of x till x * x
            primes[i] = False
    return primes


def get_list_of_primes(n):
    """
    Generate all the prime numbers up to n
    :param n: The ceiling for the prime number search
    :return: A list containing only the prime numbers
    """
    return [ind for ind, i in enumerate(prime_sieve(n)) if i]


def get_list_of_primes_pre_calc(gen):
    """
    Same as get list of primes, but used when prime sieve is already done
    :param gen: The prime sieve
    :return: A list containing only the prime numbers
    """
    return [ind for ind, i in enumerate(gen) if i]