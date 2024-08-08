#!/usr/bin/python3

def seive(n):
    """
    This function computes the prime numbers up to n
    using the Sieve of Eratosthenes.
    Args:
         n (int): number argument to be computed.
    Returns: A list of all prime number up to n.
    """

    is_prime = [True] * (n + 1)

    p = 2

    while (p * p <= n):
        if (is_prime[p] is True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

        p += 1

    primes = [p for p in range(2, n + 1) if is_prime[p]]

    return primes


def count_primes(n):
    """
        This function counts the lenght of primes lists of n.
        Args:
            n (list of ints): represents the list of primes
        Returns:
            The length of prime lists of n.
    """

    primes = seive(n)

    return len(primes)


def isWinner(x, nums):
    if x == 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    max_n = max(nums)
    primes_count = [0] * (max_n + 1)

    for i in range(1, max_n + 1):
        primes_count[i] = count_primes(i)

    for n in nums:
        if primes_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
