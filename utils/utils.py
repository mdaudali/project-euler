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


def get_proper_divisors(n):
    """Gets the divisors up to but not including itself
    
    Args:
        n (int): The number to divide
    """

    divisors = set([1])
    if n <= 2:
        return divisors
    for x in range(2, int(math.ceil(math.sqrt(n)) + 1)):
        if n % x == 0:
            divisors.add(x)
            divisors.add(n // x)
    return divisors


def is_prime(n, primes):
    """Quick primality test using a given list of primes
    
    Args:
        n (int): Number to test
        primes (int list): list of primes
    """
    for x in primes:
        if n % x == 0:
            return False
    else:
        return True


def is_palindrome(x):
    return x == x[::-1]


def get_number_digits(x):
    return int(math.log10(x)) + 1